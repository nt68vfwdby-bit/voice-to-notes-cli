import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 44100


def record_audio(output_path: str, sample_rate: int = SAMPLE_RATE) -> bool:
    audio_chunks = []

    def callback(indata, frames, time, status):
        audio_chunks.append(indata.copy())

    input("\nНажмите Enter, чтобы начать запись")
    print("Запись идет (Для остановки нажмите Ctrl + C)")
    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback):
        try:
            while True:
                sd.sleep(100)
        except KeyboardInterrupt:
            print("\nЗапись остановлена")
    if not audio_chunks:
        print("Аудио не записано.")
        return False
    full_audio = np.concatenate(audio_chunks, axis=0)
    write(output_path, sample_rate, full_audio)
    print(f"Аудио сохранено: {output_path}")
    return True
