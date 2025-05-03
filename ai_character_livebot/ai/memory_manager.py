import json
import os

MEMORY_FILE = "memory/user_sessions.json"

def recall_memory(limit=5):
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
    return messages[-limit:]

def save_memory(message):
    messages = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            messages = json.load(f)
    messages.append(message)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
