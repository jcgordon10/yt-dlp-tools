import os
import pytest
import subprocess
from unittest.mock import patch
from yt_dlp_tools.dl_playlist_audio import dl_playlist_audio


@pytest.fixture(autouse=True)
def mock_subprocess_run(mocker):
    mocker.patch("subprocess.run", return_value=None)


def test_dl_playlist_audio_creates_directory():
    output_dir = "test_downloads"
    video_url = "https://www.youtube.com/watch?v=TEST_VIDEO"
    dl_playlist_audio(video_url, output_dir=output_dir)
    assert os.path.exists(output_dir)
    os.rmdir(output_dir)


def test_dl_playlist_audio_calls_subprocess():
    video_url = "https://www.youtube.com/watch?v=TEST_VIDEO"
    dl_playlist_audio(video_url)
    subprocess.run.assert_called_once()


def test_dl_playlist_audio_command_structure():
    video_url = "https://www.youtube.com/watch?v=TEST_VIDEO"
    dl_playlist_audio(video_url)
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
        "%(playlist_title)s/%(playlist_index)s %(title)s.%(ext)s",
        video_url,
    ]
    assert (
        command_called == expected_command
    ), f"Expected {expected_command}, but got {command_called}"