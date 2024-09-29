import os
import subprocess
import argparse

def dl_audio(video_url: str, output_dir: str = "downloads") -> None:
    """
    Downloads audio from a specified YouTube video using yt-dlp.

    Args:
        video_url (str): The URL of the YouTube video to download.
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
        "%(title)s.%(ext)s",  # Saving video directly in the downloads folder with its title
        video_url,
    ]

    subprocess.run(command)
    os.chdir(original_cwd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download audio from a YouTube video."
    )
    parser.add_argument(
        "video_urls",
        nargs="+",
        help="One or more YouTube video URLs to download.",
    )
    parser.add_argument(
        "--output-dir",
        default="downloads",
        help="Directory where the audio files will be saved. Defaults to 'downloads'.",
    )

    args = parser.parse_args()

    for video_url in args.video_urls:
        dl_audio(video_url, output_dir=args.output_dir)

    print("All audio downloaded successfully!")
