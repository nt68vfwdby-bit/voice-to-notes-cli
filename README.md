
A privacy-focused command-line tool for macOS that records voice notes via microphone, transcribes speech locally using **OpenAI Whisper**, and generates structured Markdown summaries using a local LLM via **Ollama**.
## Project Architecture
```text
voice_project/
├── main.py            # CLI argument parsing (argparse) and pipeline orchestration
├── recorder.py        # Real-time microphone audio stream capture (sounddevice)
├── transcriber.py     # Local speech-to-text transcription (Whisper)
├── summarizer.py      # Structured note generation via local LLM (Ollama)
└── requirements.txt   # Project dependencies
```

## Setup and Installation

### 1. Prerequisites
Install and launch [Ollama](https://ollama.com), then pull the summarization model:
```bash
ollama pull qwen2.5:7b
```

### 2. Clone and Install Dependencies
```bash
git clone https://github.com/nt68vfwdby-bit/voice-to-notes-cli
cd voice-to-notes-cli

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Link Local FFmpeg (macOS)
```bash
ln -sf $(python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())") ./ffmpeg
```

## Usage

**Prompts for file name and folder:**
```bash
python main.py
```

**CLI mode with flags:**
```bash
python main.py --name lecture_1 --output ~/Desktop/Notes --whisper base --model qwen2.5:7b
```

**View all available options:**
```bash
python main.py --help
```

