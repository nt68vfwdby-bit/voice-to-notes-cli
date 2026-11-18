import ollama


def create_notes(raw_text: str, note_path: str, llm_model: str = "qwen2.5:7b") -> None:
    print(f"\nНейросеть ({llm_model}) составляет конспект")
    prompt = f"""
    Ты — помощник по созданию конспектов.
    Прочитай расшифровку аудиозаписи и сделай из неё структурированный конспект.
    Пиши на том же языке, на котором сделана запись.
    Выдели главную тему.
    Оформи главные мысли в виде маркированного списка.
    Если в тексте есть задачи или выводы, вынеси их в отдельный блок в конце.
    Убери воду, оставь только суть.
    Текст записи:
    {raw_text}
    """
    response = ollama.chat(
        model=llm_model,
        messages=[{"role": "user", "content": prompt}],
    )
    summary = response["message"]["content"]
    with open(note_path, "w", encoding="utf-8") as file:
        file.write("# Конспект записи\n\n")
        file.write(summary)
        file.write("\n\n---\n### Расшифровка (оригинал):\n")
        file.write(raw_text)
    print(f"Конспект сохранён в {note_path}")
