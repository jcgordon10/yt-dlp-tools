import os
import pytest
import subprocess
from unittest.mock import patch
from yt_dlp_tools.dl_audio import dl_audio


@pytest.fixture(autouse=True)
def mock_subprocess_run(mocker):
    mocker.patch("subprocess.run", return_value=None)


def test_dl_audio_creates_directory():
    # Arrange
    output_dir = "test_downloads"
    video_url = "https://www.youtube.com/watch?v=TEST_VIDEO"

    # Act
    dl_audio(video_url, output_dir=output_dir)

    # Assert
    assert os.path.exists(output_dir)

    # Cleanup
    os.rmdir(output_dir)


def test_dl_audio_calls_subprocess():
    # Arrange
    video_url = "https://www.youtube.com/watch?v=TEST_VIDEO"

    # Act
    dl_audio(video_url)

    # Assert
    subprocess.run.assert_called_once()


def test_dl_audio_command_structure():
    # Arrange
    video_url = "https://www.youtube.com/watch?v=TEST_VIDEO"

    # Act
    dl_audio(video_url)

    # Assert
    command_called = subprocess.run.call_args[0][
        0
    ]
    expected_command = [
        "yt-dlp",
        "-f",
        "bestaudio[ext=m4a]",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "0",
        "--metadata-from-title",
        "%(title)s",
        "-o",
        "%(title)s.%(ext)s",
        video_url,
    ]
    assert (
        command_called == expected_command
    ), f"Expected {expected_command}, but got {command_called}"