# transcriber
Python program that uses AI to transcribe audio.
It uses the [pyannote-audio](https://github.com/pyannote/pyannote-audio) library for diarization (detecting speakers) and [openai-whisper](https://github.com/openai/whisper) for transcription.

# Examples
See [examples](examples/) for an english and a german transcription of a short YouTube video. Generally speaking the results will best in english but the results are still very impressive in other languages.

# System requirements
This project was tested on the following hardware:
- CPU: AMD Ryzen 7 5800H
- GPU: Nvidia RTX 3060 6GB (Laptop)
- RAM: 16 GB

The Whisper AI model (medium) requires at least 5GB of VRAM. There is a larger model available which should perform even better but it's 10GB exceeded the size of my GPU VRAM.

# Installation
1. Create a virtual environment (check https://docs.python.org/3/library/venv.html)
1. Install dependencies
    ```
    pip install -r requirements.txt
    ```
3. Visit https://github.com/pyannote/pyannote-audio and check the installation instructions. The pyannote.audio library should be already installed but it uses gated models so you need to go to huggingface.co and accept their conditions.
4. Take the huggingface.co access token you created in the previous step and paste it into [main.py](src/main.py).
5. Setup working directory (temp). This is where temporary files will be stored during the transcription process. You don't need to worry about this aside from debugging. Be aware that this directory will be emptied from time to time so don't store anything important here. I recommend the following project structure to keep the project organized:

        .
        ├── .venv                   # Python virtual environment
        ├── recordings              # Place audio files here
        ├── src                     # Source files
        ├── temp                    # Working directory (keep this empty, don't place anything here)    
        ├── .gitignore              
        ├── README.md
        └── requirements.txt
6. Only .wav files can be transcribed. Use ffmpeg if you want to convert files to .wav.
    ```
    ffmpeg -i /path/to/audio_file.mp4 ./recordings/audio_file.wav
    ```

# Usage
Once you adjusted all settings in [main.py](src/main.py) you can start the transcription by running [main.py](src/main.py). The resulting transcript file will be placed alongside the audio file.