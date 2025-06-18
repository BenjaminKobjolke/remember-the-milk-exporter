#!/usr/bin/env python3
"""
Remember The Milk Tag Exporter

This script connects to the Remember The Milk API and exports all tags
to a text file, with each tag on a new line prefixed with #.
"""

import os
import sys
import configparser
import logging
from pathlib import Path

# Import rtmilk package (installed via pip from GitHub)
from rtmilk.models import APIError
from rtmilk.api_sync import API
from rtmilk.authorization import AuthorizationSession

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("rtm_exporter")


class RTMExporter:
    """Class to handle exporting data from Remember The Milk."""

    def __init__(self, config_path="settings.ini"):
        """Initialize the exporter with the given configuration file."""
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        
        # Get API credentials
        self.api_key = self.config.get("rtm", "api_key", fallback="")
        self.shared_secret = self.config.get("rtm", "shared_secret", fallback="")
        self.token = self.config.get("rtm", "token", fallback="")
        
        # Get output settings
        output_dir_str = self.config.get("output", "directory", fallback="output")
        self.output_filename = self.config.get("output", "filename", fallback="rtm_tags.txt")
        self.output_filename_lists = self.config.get("output", "filename_lists", fallback="rtm_lists.txt")
        
        # Handle both absolute and relative paths
        self.output_dir = Path(output_dir_str)
        
        if not self.api_key or not self.shared_secret:
            logger.error("API key and shared secret must be set in settings.ini")
            sys.exit(1)

    def authenticate(self):
        """Authenticate with the Remember The Milk API."""
        if not self.token:
            logger.info("No authentication token found. Starting authentication flow...")
            try:
                auth_session = AuthorizationSession(self.api_key, self.shared_secret, "read")
                print(f"Please visit the following URL to authorize the application:")
                print(auth_session.url)
                input("Press Enter after you have authorized the application...")
                
                self.token = auth_session.Done()
                logger.info("Authentication successful. Token received.")
                
                # Save the token to the config file
                self.config.set("rtm", "token", self.token)
                with open(self.config_path, "w") as config_file:
                    self.config.write(config_file)
                logger.info(f"Token saved to {self.config_path}")
            except APIError as e:
                logger.error(f"Authentication error: {e}")
                sys.exit(1)
        else:
            logger.info("Using existing authentication token.")

    def export_tags(self):
        """Export all tags to a text file."""
        try:
            # Create API client
            api = API(self.api_key, self.shared_secret, self.token)
            
            # Get all tags
            logger.info("Retrieving tags from Remember The Milk...")
            tag_response = api.TagsGetList()
            
            # Check if tags exist in the response
            if not hasattr(tag_response.tags.tag, "__iter__"):
                logger.warning("No tags found in the account.")
                return
            
            # Ensure output directory exists
            self.output_dir.mkdir(exist_ok=True, parents=True)
            
            # Format tags and write to file
            output_file = self.output_dir / self.output_filename
            tag_count = 0
            
            logger.info(f"Exporting tags to {output_file}...")
            
            with open(output_file, "w", encoding="utf-8") as f:
                for tag_obj in tag_response.tags.tag:
                    tag_name = tag_obj.name
                    f.write(f"#{tag_name}\n")
                    tag_count += 1
            
            logger.info(f"Successfully exported {tag_count} tags to {output_file}")
            
        except APIError as e:
            logger.error(f"API error: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            sys.exit(1)

    def export_lists(self):
        """Export all lists to a text file."""
        try:
            # Create API client
            api = API(self.api_key, self.shared_secret, self.token)

            # Get all lists
            logger.info("Retrieving lists from Remember The Milk...")
            list_response = api.ListsGetList()

            # Check if lists exist in the response
            if not hasattr(list_response.lists.list, "__iter__"):
                logger.warning("No lists found in the account.")
                return

            # Ensure output directory exists
            self.output_dir.mkdir(exist_ok=True, parents=True)

            # Format lists and write to file
            output_file = self.output_dir / self.output_filename_lists
            list_count = 0

            logger.info(f"Exporting lists to {output_file}...")

            with open(output_file, "w", encoding="utf-8") as f:
                for list_obj in list_response.lists.list:
                    list_name = list_obj.name
                    f.write(f"{list_name}\n")
                    list_count += 1

            logger.info(f"Successfully exported {list_count} lists to {output_file}")

        except APIError as e:
            logger.error(f"API error: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            sys.exit(1)


def main():
    """Main entry point for the application."""
    logger.info("Starting Remember The Milk Tag Exporter")
    
    exporter = RTMExporter()
    exporter.authenticate()
    exporter.export_tags()
    exporter.export_lists()
    
    logger.info("Export completed successfully")


if __name__ == "__main__":
    main()
