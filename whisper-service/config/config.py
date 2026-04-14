import os


class Config:
    WHISPER_API_KEY = os.getenv("WHISPER_API_KEY")
    WHISPER_HOST = os.getenv("WHISPER_HOST")
    WHISPER_PORT = int(os.getenv("WHISPER_PORT"))