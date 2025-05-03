import pytchat
import time

from config import load_config
from utils.logger import setup_logger

logger = setup_logger()
config = load_config()

def start_listening(callback):
    video_id = config["YOUTUBE_VIDEO_ID"]
    logger.info(f"Memulai listener YouTube Live untuk video ID: {video_id}")

    chat = pytchat.create(video_id=video_id)
    while chat.is_alive():
        try:
            for c in chat.get().sync_items():
                message = f"{c.author.name}: {c.message}"
                logger.info(f"Komentar: {message}")
                callback(c.message)  # Kirim pesan ke AI
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error saat membaca komentar: {e}")
            time.sleep(5)
