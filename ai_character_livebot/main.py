from config import load_config
from chat.youtube_listener import start_listening
from ai.chatgpt_responder import respond_to_message
from voice.tts_engine import speak
from character.character_controller import set_expression
from utils.logger import setup_logger

import threading

# Setup logging
logger = setup_logger()

# Load configuration
config = load_config()

def process_comment(comment):
    logger.info(f"Menerima komentar: {comment}")
    ai_response = respond_to_message(comment)
    logger.info(f"Respons AI: {ai_response}")

    set_expression("speaking")
    speak(ai_response)
    set_expression("neutral")

def main():
    logger.info("Memulai AI Karakter 2D LiveBot...")

    # Jalankan listener komentar dalam thread terpisah
    chat_thread = threading.Thread(target=start_listening, args=(process_comment,))
    chat_thread.start()

if __name__ == "__main__":
    main()
