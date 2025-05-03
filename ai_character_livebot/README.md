# AI Karakter 2D Live Stream Bot

## Deskripsi

Proyek ini adalah bot **AI Karakter 2D** yang dapat **membaca komentar di live stream** (misalnya YouTube), **merespons secara otomatis** dengan **jawaban dari AI** (menggunakan ChatGPT), dan **berbicara** menggunakan **Text-to-Speech** (TTS). Selain itu, karakter 2D dapat **berubah ekspresi** berdasarkan konten komentar, memberikan pengalaman interaktif yang menyenangkan.

## Fitur

- **Membaca komentar live** dari YouTube menggunakan `pytchat`.
- **Menjawab komentar** secara otomatis menggunakan OpenAI GPT (ChatGPT).
- **Text-to-Speech (TTS)**: Mengubah jawaban AI menjadi suara menggunakan `pyttsx3` atau `gTTS`.
- **Karakter 2D**: Karakter akan **berubah ekspresi** sesuai dengan emosi komentar.
- **Integrasi OBS/VTube Studio**: Karakter 2D dapat dikendalikan dalam OBS atau VTube Studio untuk digunakan dalam live stream.

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
