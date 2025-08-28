import whisper

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/1.mp3", language="hi",task="translate")
print(result["text"])


# Use openAI wrapper for online API if local usage takes a lot of resource and time
