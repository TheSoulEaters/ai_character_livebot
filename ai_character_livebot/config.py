import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()

    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "YOUTUBE_VIDEO_ID": os.getenv("YOUTUBE_VIDEO_ID"),
        "TTS_ENGINE": os.getenv("TTS_ENGINE", "pyttsx3"),
        "TTS_LANGUAGE": os.getenv("TTS_LANGUAGE", "en"),
        "OBS_ENABLED": os.getenv("USE_STREAM_CONTROL", "False").lower() == "true",
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "CHARACTER_DEFAULT_EXPRESSION": os.getenv("DEFAULT_CHARACTER_EXPRESSION", "neutral"),
        # Tambahkan konfigurasi lainnya sesuai kebutuhan
    }
