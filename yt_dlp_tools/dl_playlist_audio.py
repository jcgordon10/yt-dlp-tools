import os
import yt_dlp

def dl_playlist_audio(playlist_url: str, output_dir: str = "downloads") -> None:
    """
    Downloads audio from a specified YouTube playlist using yt-dlp.

    Args:
        playlist_url (str): The URL of the YouTube playlist to download.
        output_dir (str): The directory where the audio files will be saved.
                          Defaults to "downloads".
    """
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(playlist_title)s/%(playlist_index)s %(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Download audio from a YouTube playlist."
    )
    parser.add_argument(
        "playlist_urls",
        nargs="+",
        help="One or more YouTube playlist URLs to download."
    )
    parser.add_argument(
        "--output-dir",
        default="downloads",
        help="Directory where the audio files will be saved. Defaults to 'downloads'."
    )

    args = parser.parse_args()

    for playlist_url in args.playlist_urls:
        dl_playlist_audio(playlist_url, output_dir=args.output_dir, filename=args.filename)

    print("All playlist audio downloaded successfully!")
