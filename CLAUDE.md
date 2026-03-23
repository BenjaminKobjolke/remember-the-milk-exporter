# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Commands

```bash
# Install dependencies
uv sync --all-extras

# Run application
uv run python main.py

# Run authentication only
uv run python main.py --auth-only

# Run tests
uv run pytest tests/ -v

# Lint and format
uv run ruff check .
uv run ruff format --check .
uv run mypy main.py
```

## Architecture

Single-file application (`main.py`) with one class:

- **RTMExporter**: Handles configuration loading, API authentication, and data export
  - `authenticate()`: Interactive OAuth flow with polling, saves token to INI
  - `export_tags()`: Retrieves tags via API, writes to output file
  - `export_lists()`: Retrieves lists via API, writes to output file
  - `_clear_token()`: Clears expired token and re-authenticates
- **main()**: Entry point, supports `--auth-only` flag

### Authentication Flow
1. Checks for existing token in `settings.ini`
2. If no token: opens browser for OAuth, polls for authorization (12 attempts, 5s intervals)
3. Saves token to `settings.ini` for future use
4. On API error code 98 (expired token): clears token and re-authenticates automatically

### Configuration
- `settings.ini` (gitignored): API credentials and output settings
- `settings_example.ini`: Template with comments
- Uses Python's `configparser` module

### Dependencies
- `rtmilk`: RTM API client (installed from GitHub via git+https)
- `pydantic`, `requests`, `aiohttp`, `listdiff`: rtmilk dependencies

## Coding Rules

### Common Rules
- Use objects/DTOs for related values instead of many parameters
- Follow TDD: write tests first, confirm they fail, implement, confirm they pass
- Include both unit and integration tests
- Test runner scripts in `tools/` directory
- Prefer type-safe values (typed DTOs, enums, generics)
- Centralize string constants in a dedicated module
- DRY: extract shared logic into reusable functions
- Confirm dependency versions with user before adding
- Centralized error handling with structured logging
- Validate data at system boundaries
- Maximum 300 lines per file
- Naming: snake_case for files/functions/variables, PascalCase for classes, UPPER_SNAKE_CASE for constants
- Never commit secrets
- No god classes (max 5 public methods, max 4 constructor dependencies)
- Self-describing classes: declare fields through contracts, not hardcoded lists

### Python Rules
- `pyproject.toml` as single source of truth (commit `uv.lock`)
- Use ruff for lint + formatting, mypy for type checking
- Type hints on all public functions/classes/methods
- Use pytest for tests
- Use `logging` module, never `print()` (except user-facing prompts)
- Use Pydantic for validation at API boundaries
- Required batch files: `start.bat`, `tools/run_tests.bat`
