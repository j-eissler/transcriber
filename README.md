# transcriber
Python program that uses AI to transcribe audio.

It uses the [pyannote-audio](https://github.com/pyannote/pyannote-audio) library for diarization (detecting speakers) and [openai-whisper](https://github.com/openai/whisper) for transcription.


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

# Usage
Once you adjusted all settings in [main.py](src/main.py) you can start the transcription by running [main.py](src/main.py). The resulting transcript file will be placed alongside the audio file.
