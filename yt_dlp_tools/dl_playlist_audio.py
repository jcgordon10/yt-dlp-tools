import os
import subprocess
import argparse


def dl_playlist_audio(playlist_url: str, output_dir: str = "downloads") -> None:
    """
    Downloads audio from a specified YouTube playlist using yt-dlp.

    Args:
        playlist_url (str): The URL of the YouTube playlist to download.
        output_dir (str): The directory where the audio files will be saved.
                          Defaults to "downloads".
    """
    os.makedirs(output_dir, exist_ok=True)
    original_cwd = os.getcwd()
    os.chdir(output_dir)

    command = [
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
        playlist_url,
    ]

    subprocess.run(command)
    os.chdir(original_cwd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download audio from a YouTube playlist."
    )
    parser.add_argument(
        "playlist_urls",
        nargs="+",
        help="One or more YouTube playlist URLs to download.",
    )
    parser.add_argument(
        "--output-dir",
        default="downloads",
        help="Directory where the audio files will be saved. Defaults to 'downloads'.",
    )

    args = parser.parse_args()

    for playlist_url in args.playlist_urls:
        dl_playlist_audio(playlist_url, output_dir=args.output_dir)

    print("All playlist audio downloaded successfully!")
