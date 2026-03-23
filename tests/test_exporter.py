"""Tests for RTMExporter."""

import pytest

from main import RTMExporter


def test_exporter_init_missing_credentials(tmp_path: str) -> None:
    """RTMExporter should exit if API credentials are missing."""
    config_path = tmp_path / "test_settings.ini"
    config_path.write_text("[rtm]\napi_key = \nshared_secret = \ntoken = \n\n[output]\ndirectory = output\n")

    with pytest.raises(SystemExit):
        RTMExporter(config_path=str(config_path))


def test_exporter_init_with_credentials(tmp_path: str) -> None:
    """RTMExporter should initialize successfully with valid credentials."""
    config_path = tmp_path / "test_settings.ini"
    config_path.write_text(
        "[rtm]\napi_key = test_key\nshared_secret = test_secret\ntoken = test_token\n\n"
        "[output]\ndirectory = output\nfilename = tags.txt\nfilename_lists = lists.txt\n"
    )

    exporter = RTMExporter(config_path=str(config_path))
    assert exporter.api_key == "test_key"
    assert exporter.shared_secret == "test_secret"
    assert exporter.token == "test_token"
