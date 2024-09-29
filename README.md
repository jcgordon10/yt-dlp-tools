# yt-dlp-tools

A Python-based utility for downloading and processing audio from YouTube videos and playlists using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
  - [Download Audio from a Single Video](#download-audio-from-a-single-video)
  - [Download Audio from a Playlist](#download-audio-from-a-playlist)
- [Running Tests](#running-tests)
- [Important Notes](#important-notes)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Download audio from YouTube videos in MP3 format.
- Download entire playlists and organize the files based on playlist order and title.
- Supports high-quality audio extraction with automatic metadata from YouTube.

---

## Setup

### Prerequisites
1. **Python 3.7+**: You can download it from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jcgordon10/yt-dlp-tools.git
    cd yt-dlp-tools
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate
    ```

    or on Windows
    ```bash
    python -m venv env
    env/bin/activate
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Download Audio from a Single Video
You can download the audio of a YouTube video by running the following command:

```bash
python -m yt_dlp_tools.dl_audio https://www.youtube.com/watch?v=your_video_id
```

#### Optional: Specify the output directory
You can also specify where you want to save the audio files using the --output-dir option (default is downloads):

```bash
python -m yt_dlp_tools.dl_audio https://www.youtube.com/watch?v=your_video_id --output-dir custom_directory
```

### Download Audio from a Playlist
To download the audio from an entire playlist, use:

```bash
python -m yt_dlp_tools.dl_playlist_audio https://www.youtube.com/playlist?list=your_playlist_id
```

#### Optional: Specify the output directory
You can also specify a custom output directory:

```bash
python -m yt_dlp_tools.dl_playlist_audio https://www.youtube.com/playlist?list=your_playlist_id --output-dir custom_directory
```

---

## Running Tests
This repository includes unit tests that mock the yt-dlp subprocess and some real download tests .

### Running All Tests
1. Ensure pytest is installed:
```bash
pip install pytest pytest-mock
```

2. Run the tests using pytest:
```bash
pytest tests/
```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.