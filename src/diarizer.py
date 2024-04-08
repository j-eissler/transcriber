from pyannote.audio import Pipeline
import torch
import json
from os import path


class Diarizer:
    def __init__(self, hf_auth_token, audio_file, working_dir) -> None:
        self.hf_auth_token = hf_auth_token
        self.audio_file = audio_file
        self.working_dir = working_dir

    def diarize(self):
        print("Running diarization...")

        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1", use_auth_token=self.hf_auth_token
        )
        pipeline.to(torch.device("cuda"))  # Try sending model to GPU
        diarization = pipeline(self.audio_file)

        # Format result into json string and combine consecutive segments
        result = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            start = round(turn.start, 1)
            end = round(turn.end, 1)

            # Check if the speaker changed in the current segment. If not then just use the new end time to combine the segments
            if len(result) > 0:
                last = result[-1]
                if last["speaker"] == speaker:
                    last["end"] = end
                    continue
            result.append({"start": start, "end": end, "speaker": speaker})

        with open(path.join(self.working_dir, "diarization.json"), "w") as f:
            f.write(json.dumps(result))

        print("Diarization complete. Segments:")
        for r in result:
            print(f'{r["start"]} - {r["end"]} : {r["speaker"]}')
