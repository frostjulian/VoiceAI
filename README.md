# 🎙 VoiceAI - Local Speech AI Assistant
> A real-time voice conversation system powered by Whisper + Ollama + Edge-TTS
---
## 🚀 Project Overview
VoiceAI is a local AI voice assistant that enables **end-to-end voice conversation**:
🎤 Speech → 🧠 AI Understanding → 🤖 LLM Response → 🔊 Voice Output
It integrates:
- Whisper for speech recognition (ASR)
- Ollama (Qwen-7B) for local LLM reasoning
- Edge-TTS for high-quality speech synthesis
---
## 🧠 System Architecture

Microphone Input
↓
Whisper (Speech-to-Text)
↓
Ollama LLM (Qwen:7B)
↓
Edge-TTS (Text-to-Speech)
↓
Audio Playback

---
## ⚙️ Features
- 🎤 Real-time voice input
- 🧠 Offline LLM inference (Ollama)
- 🔊 Natural speech synthesis (Edge-TTS)
- 💬 Continuous voice conversation loop
- 📁 Local execution, no cloud dependency
---
## 🛠 Tech Stack
- Python 3.10+
- OpenAI Whisper
- Ollama (Qwen:7B)
- Edge-TTS
- SoundDevice + SciPy
---
## 📦 Installation
```bash
git clone https://github.com/frostjulian/VoiceAI.git
cd VoiceAI
pip install -r requirements.txt

⸻

▶️ Usage

1️⃣ Start Ollama

ollama run qwen:7b

⸻

2️⃣ Run project

python main.py

⸻

💡 Example

User: 你好
AI: 你好！有什么可以帮助你的？

⸻

📌 Key Highlights

* Fully local AI voice assistant
* No cloud API required
* Modular architecture
* Real-time interaction pipeline

⸻

🧩 Future Improvements

* Wake word detection (“Hey AI”)
* Streaming voice response
* GUI interface (ChatGPT-style UI)
* Memory-based conversation history
👨‍💻 Author

FrostJulian

Software Engineering Student
Focus: AI Applications & Voice Systems
