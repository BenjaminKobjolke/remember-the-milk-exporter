# Remember The Milk Tag Exporter

A Python application that exports all tags from your Remember The Milk account to a text file, with each tag on a new line prefixed with #.

## Features

- Connects to the Remember The Milk API
- Exports all tags to a text file
- Formats tags with # prefix
- Handles authentication flow
- Saves authentication token for future use

## Requirements

- Python 3.6 or higher
- Git (for installing packages from GitHub)
- Remember The Milk API key and shared secret
- Python packages (installed automatically by install.bat):
  - rtmilk (installed directly from GitHub)
  - pydantic
  - requests
  - aiohttp
  - listdiff

## Setup

1. **Get API Credentials**

   - Go to [Remember The Milk API Keys](https://www.rememberthemilk.com/services/api/keys.rtm)
   - Create a new API key
   - Note down the API key and shared secret

2. **Configure the Application**

   - Edit `settings.ini` and add your API key and shared secret:
     ```ini
     [rtm]
     api_key = your_api_key
     shared_secret = your_shared_secret
     ```

3. **Install Dependencies**
   - Run `install.bat` to set up the virtual environment and dependencies

## Usage

1. Run `run.bat` to start the application
2. If this is your first time running the application, you will be prompted to authorize it:
   - A URL will be displayed
   - Open the URL in your web browser
   - Log in to your Remember The Milk account if necessary
   - Authorize the application
   - Return to the command prompt and press Enter
3. The application will export all tags to `output/rtm_tags.txt`

## File Structure

- `main.py`: Main application code
- `settings.ini`: Configuration file for API credentials
- `output/rtm_tags.txt`: Exported tags
- `install.bat`: Installation script
- `run.bat`: Execution script
- `requirements.txt`: Lists dependencies including rtmilk from GitHub

## Troubleshooting

- If you encounter authentication errors, check your API key and shared secret
- If the application fails to retrieve tags, ensure you have authorized it with the correct permissions
- If you need to re-authenticate, delete the token line from `settings.ini`
- If you encounter import errors, make sure Git is installed and your internet connection is working

## License

See the LICENSE file for details.
