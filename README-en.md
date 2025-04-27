```markdown
# J.A.R.V.I.S. AI Assistant
```
![JARVIS Logo](assets/logo.png)

<p align="center">
  <a href="./README-en.md">
    <img src="https://img.shields.io/badge/Terjemahkan%20ke %20Versi%20Indonesia-%E2%86%92-blue" alt="Translate English Version">
  </a>
</p>

A voice and GUI-based AI assistant inspired by Iron Man's J.A.R.V.I.S., built with Python and local language models (LLMs).

## 🚀 Key Features
- Voice interaction with wake word "Jarvis"
- Modern GUI interface using PyQt5
- Local model support (Meta-Llama-3-8B-Instruct.Q4_0)
- Browser and YouTube integration
- Multi-theme support (dark/light mode)

## 📦 Project Structure
```
JARVIS/
├── models/               # Local AI models
│   └── Meta-Llama-3-8B-Instruct.Q4_0.gguf
├── assets/               # Image assets and icons
├── core/                 # Core modules
│   ├── commands.py       # Command system
│   ├── hardware.py       # Hardware control
│   ├── jarvis_ai.py      # AI core
│   └── voice.py          # Voice processing
├── gpt4all/              # download Meta-Llama-3-8B-Instruct.Q4_0.gguf in this folder
├── gui/                  # User interface
│   ├── app.py            # Main application
│   └── themes.py         # Theme system
├── config.py             # Configuration
├── main.py               # Entry point
└── requirements.txt      # Dependencies
```

## ⚙️ Installation
1. **Clone repository**:
   ```bash
   git clone https://github.com/jarvis-id/JARVIS.git
   cd JARVIS
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download LLM model**:
   - Place `Meta-Llama-3-8B-Instruct.Q4_0.gguf` in the `gpt4all/` folder
   - Or run:
     ```bash
     python -m gpt4all download Meta-Llama-3-8B-Instruct.Q4_0.gguf --path models/
     ```

## 🖥️ Running the Application
```bash
python main.py
```

## ⚙️ Configuration
Modify settings in `config.py`:
```python
CONFIG = {
    "user_name": "Master",          # User name
    "hotword": "jarvis",            # Wake word
    "voice_enabled": True,          # Enable voice
    "theme": "dark",                # Default theme
    "default_browser": "chrome",    # Default browser
    # ... and other settings
}
```

## 📌 System Requirements
- Python 3.10+
- 8GB+ RAM (16GB recommended)
- CUDA-supported GPU (optional)
- Operating System: Windows/Linux/macOS

## 🤖 Supported AI Models
- Meta-Llama-3-8B-Instruct.Q4_0.gguf (default)
- Additional GGUF models can be added to the `gpt4all/` folder

## 📄 License
This project is licensed under the [MIT License](LICENSE.txt).

---

> **Note**: This project is under active development. Contributions are welcome!
```
Key improvements made:
1. Natural English phrasing while maintaining technical accuracy
2. Consistent terminology (e.g., "local models" instead of "model lokal")
3. Proper capitalization and punctuation
4. Maintained all the original structure and functionality
5. Kept the same visual style with emojis and code blocks
```
