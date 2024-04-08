import json
from pydub import AudioSegment
from os import path


class Splitter:
    def __init__(self, audio_file, working_dir) -> None:
        self.working_dir = working_dir
        self.audio_file = audio_file

    def create_audio_segments(self):
        print("Creating audio segments...")

        diarization = []
        with open(path.join(self.working_dir, "diarization.json"), "r") as f:
            diarization = json.loads(f.read())

        counter = 1
        for segment in diarization:
            start = segment["start"] * 1000  # Convert to milliseconds
            end = segment["end"] * 1000
            newAudio = AudioSegment.from_wav(self.audio_file)
            newAudio = newAudio[start:end]
            filename = path.join(self.working_dir, f"{str.zfill(str(counter), 5)}.wav")
            newAudio.export(
                filename,
                format="wav",
            )  # Exports to a wav file in the current path.

            print(f"Audio segment created '{filename}'")

            counter += 1
