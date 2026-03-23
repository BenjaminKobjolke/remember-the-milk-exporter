# Remember The Milk Tag Exporter

A Python application that exports all tags and lists from your Remember The Milk account to text files.

## Features

- Connects to the Remember The Milk API
- Exports all tags to a text file (prefixed with #)
- Exports all lists to a text file
- Handles authentication flow with automatic token refresh
- Saves authentication token for future use

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)
- Git (for installing packages from GitHub)
- Remember The Milk API key and shared secret

## Setup

1. **Get API Credentials**

   - Go to [Remember The Milk API Keys](https://www.rememberthemilk.com/services/api/keys.rtm)
   - Create a new API key
   - Note down the API key and shared secret

2. **Configure the Application**

   - Copy `settings_example.ini` to `settings.ini`
   - Add your API key and shared secret:

     ```ini
     [rtm]
     api_key = your_api_key
     shared_secret = your_shared_secret
     ```

   - Optionally, configure the output directory and filename:
     ```ini
     [output]
     directory = path/to/output/directory
     filename = rtm_tags.txt
     filename_lists = rtm_lists.txt
     ```
     The directory can be an absolute path (e.g., `D:\path\to\directory`) or a relative path (e.g., `output`).

3. **Install Dependencies**
   - Run `install.bat` to set up the environment and install dependencies

## Usage

1. Run `run.bat` (or `start.bat`) to start the application
2. If this is your first time running the application, you will be prompted to authorize it:
   - A URL will be displayed
   - Open the URL in your web browser
   - Log in to your Remember The Milk account if necessary
   - Authorize the application
   - Return to the command prompt and press Enter
3. The application will export all tags and lists to the configured output location

## File Structure

- `main.py` — Main application code
- `pyproject.toml` — Project metadata, dependencies, and tool configuration
- `uv.lock` — Locked dependency versions
- `settings.ini` — Configuration file for API credentials and output settings (gitignored)
- `settings_example.ini` — Example configuration file with comments
- `install.bat` — Install dependencies via uv
- `run.bat` / `start.bat` — Run the exporter
- `sign_in.bat` — Run authentication only
- `update.bat` — Pull latest code and sync dependencies
- `tools/run_tests.bat` — Run test suite
- `tools/run_integration_tests.bat` — Run integration tests

## Development

```bash
# Install all dependencies (including dev tools)
uv sync --all-extras

# Run linting
uv run ruff check .

# Run formatting check
uv run ruff format --check .

# Run type checking
uv run mypy main.py

# Run tests
uv run pytest tests/ -v
```

## Troubleshooting

- If you encounter authentication errors, check your API key and shared secret
- If the application fails to retrieve tags, ensure you have authorized it with the correct permissions
- If you need to re-authenticate, delete the token line from `settings.ini` or run `sign_in.bat`
- If you encounter import errors, make sure Git is installed and your internet connection is working

## License

See the LICENSE file for details.
