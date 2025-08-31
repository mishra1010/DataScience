import whisper
import json

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/1.mp3", language="hi",task="translate", word_timestamps=False )

print(result["text"])


# Use openAI wrapper for online API if local usage takes a lot of resource and time
chunks = []
for segment in result["segments"]:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks,f)