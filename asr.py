#语言识别模块
import whisper
print("🔄 加载 Whisper...")
model = whisper.load_model("base")
def speech_to_text(filename="input.wav"):
    print("🔍 正在识别语音...")
    result = model.transcribe(filename)
    text = result["text"]
    print(f"🧑 你说: {text}")
    return text