import openai
from config import load_config
from ai.memory_manager import recall_memory, save_memory

config = load_config()
openai.api_key = config["OPENAI_API_KEY"]

def respond_to_message(user_message):
    memory = recall_memory()
    system_prompt = load_persona()

    messages = [{"role": "system", "content": system_prompt}]
    messages += memory
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.8,
        )
        ai_reply = response.choices[0].message.content.strip()
        save_memory({"role": "user", "content": user_message})
        save_memory({"role": "assistant", "content": ai_reply})
        return ai_reply
    except Exception as e:
        return "Maaf, ada kesalahan teknis dalam menjawab."

def load_persona():
    import json
    with open("ai/persona.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("prompt", "You are a helpful assistant.")
