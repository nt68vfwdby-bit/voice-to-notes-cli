from __future__ import annotations
import argparse
import os
from recorder import record_audio
from transcriber import transcribe_audio
from summarizer import create_notes


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CLI-инструмент для записи голоса и создания конспектов через Whisper и Ollama."
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        default=None,
        help="Название выходного файла (без расширения)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Папка для сохранения аудио и конспекта (по умолчанию: ~/Desktop)",
    )
    parser.add_argument(
        "-w",
        "--whisper",
        type=str,
        default="base",
        choices=["tiny", "base", "small", "medium"],
        help="Размер модели Whisper (по умолчанию: base)",
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="qwen2.5:7b",
        help="Название модели Ollama для генерации конспекта (по умолчанию: qwen2.5:7b)",
    )
    return parser.parse_args()


def get_save_paths(cli_name: str | None, cli_folder: str | None) -> tuple[str, str]:
    if cli_name:
        file_name = cli_name.strip()
    else:
        file_name = input(
            "Введите название для этой записи (например, lecture_1): "
        ).strip()
        if not file_name:
            file_name = "untitled_note"
    if cli_folder:
        folder_path = os.path.expanduser(cli_folder.strip())
    else:
        folder_input = input(
            "Куда сохранить? (нажмите Enter для сохранения на Рабочий стол): "
        ).strip()
        folder_path = (
            os.path.expanduser(folder_input)
            if folder_input
            else os.path.expanduser("~/Desktop")
        )
    os.makedirs(folder_path, exist_ok=True)
    audio_path = os.path.join(folder_path, f"{file_name}.wav")
    note_path = os.path.join(folder_path, f"{file_name}_конспект.md")
    return audio_path, note_path


def main():
    args = parse_arguments()
    audio_file, note_file = get_save_paths(args.name, args.output)
    if record_audio(audio_file):
        text = transcribe_audio(audio_file, model_name=args.whisper)
        if text:
            create_notes(text, note_file, llm_model=args.model)
        else:
            print("Речь не распознана")


if __name__ == "__main__":
    main()
