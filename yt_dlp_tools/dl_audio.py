import os
import argparse
import yt_dlp

def dl_audio(video_url: str, output_dir: str = "downloads", filename: str = None) -> tuple[str, dict]:
    """
    Downloads audio from a specified YouTube video using yt-dlp and returns the file path and video info.

    Args:
        video_url (str): The URL of the YouTube video to download.
        output_dir (str): The directory where the audio file will be saved.
                          Defaults to "downloads".
        filename (str, optional): Custom file name for the downloaded audio file (without extension).
                                  If not provided, the video title will be used.

    Returns:
        tuple[str, dict]: The full file path of the downloaded audio and video information.
    """
    os.makedirs(output_dir, exist_ok=True)

    if filename:
        output_template = os.path.join(output_dir, f"{filename}.%(ext)s")
    else:
        output_template = os.path.join(output_dir, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(video_url, download=True)

    filename = ydl.prepare_filename(result)
    mp3_filepath = os.path.splitext(filename)[0] + '.mp3'

    return mp3_filepath, result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Download audio from a YouTube video."
    )
    parser.add_argument(
        "video_urls",
        nargs="+",
        help="One or more YouTube video URLs to download."
    )
    parser.add_argument(
        "--output-dir",
        default="downloads",
        help="Directory where the audio files will be saved. Defaults to 'downloads'."
    )
    parser.add_argument(
        "--filename",
        help="Custom file name for the downloaded audio (without extension)."
    )

    args = parser.parse_args()

    for video_url in args.video_urls:
        filepath, _ = dl_audio(video_url, output_dir=args.output_dir, filename=args.filename)
        print(f"Audio downloaded successfully: {filepath}")