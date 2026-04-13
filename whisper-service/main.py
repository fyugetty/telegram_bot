from fastapi import FastAPI, UploadFile
import whisper

app = FastAPI()
model = whisper.load_model("base")

@app.post("/audio")
async def transcribe(audio: UploadFile):
    contents = await audio.read()
    with open ("temp.ogg", "wb") as f:
        f.write(contents)
    result = model.transcribe("temp.ogg")
    return {result["text"]}

