#语言合成
#播放并自动删除
import edge_tts
import asyncio
import os
import time
import asyncio
from config import VOICE, CACHE_DIR
async def _save(text, path):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(path)

def speak(text):
    folder = "VoiceAI_audio"
    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/tts_{int(time.time())}.mp3"

    async def _gen():
        communicate = edge_tts.Communicate(
            text,
            "zh-CN-XiaoxiaoNeural"
        )
        await communicate.save(filename)

    asyncio.run(_gen())

    print(f"🔊 已保存语音: {filename}")

    # 播放
    os.system(f'start "" "{filename}"')