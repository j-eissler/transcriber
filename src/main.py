from diarizer import Diarizer
from splitter import Splitter
from transcriber import Transcriber
import os
import glob


def main():
    ############### Edit these variables ###############
    # Audio file to be transcribed. Must be a .wav file
    audio = "path/to/audio_file.wav"

    # This is the place where temporary files like diarization info, audio segment files etc. are stored during the transcription process.
    # !!! Be careful: Everything inside this directory will be deleted !!!
    working_dir = "temp"

    # Spoken language in the audio file. Check https://github.com/openai/whisper for supported languages.
    language = "de"

    # Access token to use certain hugging face models. Create one at https://huggingface.co/settings/tokens
    hugging_face_auth_token = "<ADD TOKEN HERE>"
    ####################################################

    # Initialize working dir
    if os.path.exists(working_dir):
        files = glob.glob(os.path.join(working_dir, "*"))
        for f in files:
            os.remove(f)
    else:
        os.makedirs(working_dir)

    diarizer = Diarizer(
        hf_auth_token=hugging_face_auth_token,
        audio_file=audio,
        working_dir=working_dir,
    )
    diarizer.diarize()

    splitter = Splitter(audio_file=audio, working_dir=working_dir)
    splitter.create_audio_segments()

    transcriber = Transcriber(
        working_dir=working_dir, audio_file=audio, language=language
    )
    transcriber.transcribe_segments()


if __name__ == "__main__":
    main()
