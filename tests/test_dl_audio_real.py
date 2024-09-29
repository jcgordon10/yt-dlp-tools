import os
import pytest
import subprocess
from unittest.mock import patch
from yt_dlp_tools.dl_audio import dl_audio


def test_dl_audio_downloads_real_video():
    # Arrange
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    output_dir = "test_downloads"
    output_file = os.path.join(output_dir, "Rick Astley - Never Gonna Give You Up (Official Music Video).mp3")

    # Act
    dl_audio(video_url, output_dir=output_dir)

    # Assert
    assert os.path.exists(output_file), "The MP3 file was not created."
    file_size = os.path.getsize(output_file)  # Get size in bytes
    file_size_mb = file_size / (1024 * 1024)  # Convert to MB
    print(f"Downloaded file size: {file_size_mb:.2f} MB ({file_size} bytes)")
    assert file_size_mb > 5, "The downloaded file size is less than expected."

    # Cleanup
    os.remove(output_file)  # Optionally clean up the downloaded file