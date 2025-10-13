import pytest
from unittest.mock import patch, MagicMock
import random

# Import your function (adjust the import path to match your project)
from lib.main.features import *


@pytest.fixture
def mock_db_cursor():
    """Creates a mock database cursor for testing"""
    cursor = MagicMock()
    return cursor


@pytest.fixture
def mock_response():
    """Mock response object with cannot_understand_user list"""
    return type(
        "MockResponse", (), {"cannot_understand_user": ["Sorry, I didn’t get that."]}
    )


@patch("lib.main.features.speak")
@patch("lib.main.features.webbrowser.open")
@patch("lib.main.features.os.startfile")
@patch("lib.main.features.os.system")
def test_open_command_system_app(
    mock_system,
    mock_startfile,
    mock_web,
    mock_speak,
    mock_db_cursor,
    mock_response,
    monkeypatch,
):
    """Test when the system command exists in sys_command table"""

    # Mock sys_command table result
    mock_db_cursor.fetchall.side_effect = [
        [("C:\\Program Files\\App\\app.exe",)],  # sys_command result
    ]

    monkeypatch.setattr("lib.main.features.cursor", mock_db_cursor)
    monkeypatch.setattr("lib.main.features.response", mock_response)

    open_command("open app")

    mock_startfile.assert_called_once_with("C:\\Program Files\\App\\app.exe")
    mock_speak.assert_any_call("Opening app")


@patch("lib.main.features.speak")
@patch("lib.main.features.webbrowser.open")
@patch("lib.main.features.os.startfile")
@patch("lib.main.features.os.system")
def test_open_command_web(
    mock_system,
    mock_startfile,
    mock_web,
    mock_speak,
    mock_db_cursor,
    mock_response,
    monkeypatch,
):
    """Test when the app is found in web_command table"""

    # First query returns no sys_command, second query returns web_command
    mock_db_cursor.fetchall.side_effect = [
        [],  # sys_command
        [("https://example.com",)],  # web_command
    ]

    monkeypatch.setattr("lib.main.features.cursor", mock_db_cursor)
    monkeypatch.setattr("lib.main.features.response", mock_response)

    open_command("open google")

    mock_web.assert_called_once_with("https://example.com")
    mock_speak.assert_any_call("Opening google")


@patch("lib.main.features.speak")
@patch("lib.main.features.os.system")
def test_open_command_fallback(
    mock_system, mock_speak, mock_db_cursor, mock_response, monkeypatch
):
    """Test when app not found in both sys_command and web_command"""

    mock_db_cursor.fetchall.side_effect = [[], []]  # sys_command  # web_command

    monkeypatch.setattr("lib.main.features.cursor", mock_db_cursor)
    monkeypatch.setattr("lib.main.features.response", mock_response)

    open_command("open unknown")

    mock_system.assert_called_once()
    mock_speak.assert_any_call("Opening unknown")
