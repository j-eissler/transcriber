import json
import os
from os import path
import glob
import whisper


class Transcriber:
    def __init__(self, working_dir, audio_file, language) -> None:
        self.working_dir = working_dir
        self.audio_file = audio_file
        self.language = language

    def transcribe_segments(self):
        print("Running transcription...")

        diarization = []
        with open(path.join(self.working_dir, "diarization.json"), "r") as f:
            diarization = json.loads(f.read())

        audio_segments = glob.glob(path.join(self.working_dir, "*.wav"))

        # Transcribe segments and combine them into a single file with timestamp and speaker information
        # Place in same directory as audio file
        transcript_path = self.audio_file + "_transcript.txt"
        if path.exists(transcript_path):
            os.remove(transcript_path)

        model = whisper.load_model("medium", device="cuda")
        for i in range(len(audio_segments)):
            print(f"Transcribing '{audio_segments[i]}'...")
            result = model.transcribe(audio_segments[i], language=self.language)
            print(result["text"])

            hours = int(diarization[i]["start"] / 3600)
            minutes = int(diarization[i]["start"] % 3600 / 60)
            seconds = int(diarization[i]["start"] % 3600 % 60)

            transcript = f"{str.zfill(str(hours), 2)}:{str.zfill(str(minutes), 2)}:{str.zfill(str(seconds), 2)} - {diarization[i]['speaker']}\n"
            transcript += result["text"].lstrip()
            transcript += "\n\n"

            # Encode to prevent errors if special characters are recognized by the model
            with open(transcript_path, "a", encoding="utf-8") as f:
                f.write(transcript)
