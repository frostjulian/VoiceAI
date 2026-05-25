#录音模块
import sounddevice as sd
from scipy.io.wavfile import write
def record_audio(filename="input.wav", duration=5, fs=44100):
    print("\n🎤 请开始说话...")
    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )
    sd.wait()
    write(filename, fs, recording)
    print("✅ 录音完成")