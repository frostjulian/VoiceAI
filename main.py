
from audio import record_audio
from asr import speech_to_text
from llm import ask_ollama
from tts import speak
print("\n🎙 AI语音聊天启动成功")
while True:
    try:
        record_audio()
        user_text = speech_to_text()
        if not user_text.strip():
            continue
        if "退出" in user_text:
            print("\n👋 已退出")
            break
        reply = ask_ollama(user_text)
        speak(reply)
    except KeyboardInterrupt:
        print("\n👋 已退出")
        break
    except Exception as e:
        print("❌ 出错:", e)