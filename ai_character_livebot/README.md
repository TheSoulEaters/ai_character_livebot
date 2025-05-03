# AI Karakter 2D Live Stream Bot

## Deskripsi

Proyek ini adalah bot **AI Karakter 2D** yang dapat **membaca komentar di live stream** (misalnya YouTube), **merespons secara otomatis** dengan **jawaban dari AI** (menggunakan ChatGPT), dan **berbicara** menggunakan **Text-to-Speech** (TTS). Selain itu, karakter 2D dapat **berubah ekspresi** berdasarkan konten komentar, memberikan pengalaman interaktif yang menyenangkan.

## Fitur

- **Membaca komentar live** dari YouTube menggunakan `pytchat`.
- **Menjawab komentar** secara otomatis menggunakan OpenAI GPT (ChatGPT).
- **Text-to-Speech (TTS)**: Mengubah jawaban AI menjadi suara menggunakan `pyttsx3` atau `gTTS`.
- **Karakter 2D**: Karakter akan **berubah ekspresi** sesuai dengan emosi komentar.
- **Integrasi OBS/VTube Studio**: Karakter 2D dapat dikendalikan dalam OBS atau VTube Studio untuk digunakan dalam live stream.

## 📁 Struktur Folder

```bash
ai_character_livebot/
├── main.py                        # Entry point program utama
├── config.py                      # Pengaturan umum dan loader konfigurasi
├── .env                           # File konfigurasi rahasia (API Key, dsb)
├── .gitignore                     # File/folder yang diabaikan Git
├── requirements.txt               # Daftar dependency Python
├── README.md                      # Dokumentasi proyek

├── ai/
│   ├── chatgpt_responder.py       # Modul komunikasi dengan OpenAI ChatGPT
│   ├── memory_manager.py          # Pengelola memori percakapan
│   └── persona.json               # Deskripsi kepribadian karakter AI

├── chat/
│   └── youtube_listener.py        # Modul pembaca komentar dari YouTube Live

├── voice/
│   ├── tts_engine.py              # Modul Text-to-Speech
│   ├── voice_config.py            # Konfigurasi suara
│   ├── sounds/                    # Folder suara hasil TTS
│   └── icons/                     # Ikon suara atau notifikasi
│ 
├── character/
│   ├── character_controller.py    # Kendali karakter dan ekspresi
│   ├── emotion_detector.py        # Deteksi emosi berdasarkan teks
│   └── assets/                    # Gambar ekspresi karakter (png/gif)
├── controller/
│   └── stream_control.py          # Pengontrol OBS/VTube Studio
│ 
├── logs/
│   ├── chat_log.txt               # Log komentar yang dibaca
│   ├── ai_responses.txt           # Log respons dari AI
│   └── errors.log                 # Log error aplikasi
│ 
├── utils/
│   ├── logger.py                  # Konfigurasi logging
│   └── helpers.py                 # Fungsi bantu umum
├── memory/
│   ├── user_sessions.json         # Data sesi pengguna
│   └── recent_messages.txt        # Riwayat pesan terakhir
├── tests/
│   ├── test_ai.py                 # Unit test untuk AI responder
│   ├── test_chat.py               # Unit test pembaca komentar
│   ├── test_voice.py              # Unit test TTS
│   ├── test_emotion.py            # Unit test emosi
│   └── test_character.py          # Unit test ekspresi karakter
└── docs/
    ├── architecture_diagram.png   # Diagram arsitektur sistem
    ├── setup_guide.md             # Panduan instalasi
    └── roadmap.md                 # Perencanaan fitur mendatang


## Instalasi

### 1. Clone Repositori

Clone repositori ini ke komputer Anda:

```bash
git clone https://github.com/username/ai-character-livebot.git
cd ai-character-livebot
```

#### 2. Install dependencys

```bash
  pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
python main.py
```
