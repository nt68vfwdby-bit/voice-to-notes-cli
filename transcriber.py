import os
import whisper

os.environ["PATH"] = os.getcwd() + os.pathsep + os.environ["PATH"]


def transcribe_audio(audio_path: str, model_name: str = "base") -> str:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, fp16=False)
    raw_text = result["text"].strip()
    print("Текст получен")
    return raw_text
