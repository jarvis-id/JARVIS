<h1 align="center">
  <img src="assets/logo.png" alt="JARVIS Logo" width="200"/>
  <br>J.A.R.V.I.S. AI Assistant
</h1>

<p align="center">
  <em>Your personal AI assistant inspired by Iron Man's J.A.R.V.I.S.</em>
</p>

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
  ![License](https://img.shields.io/badge/License-MIT-green)
  ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

</div>

## 🚀 Features
<div>
  <ul>
    <li>🔊 Voice interaction with custom wake word</li>
    <li>💻 Modern PyQt5 GUI interface</li>
    <li>🧠 Local LLM (Llama 3 8B Instruct) support</li>
    <li>🌐 Browser and YouTube integration</li>
    <li>🎨 Multi-theme support (dark/light mode)</li>
  </ul>
</div>

## 📦 Project Structure
```plaintext
JARVIS/
├── models/               # Local AI models
│   └── Meta-Llama-3-8B-Instruct.Q4_0.gguf
├── assets/               # Image assets
├── core/                 # Core modules
│   ├── commands.py       # Command system
│   ├── hardware.py       # Hardware control
│   ├── jarvis_ai.py      # AI core
│   └── voice.py          # Voice processing
├── gui/                  # User interface
│   ├── app.py            # Main application
│   └── themes.py         # Theme system
├── config.py             # Configuration
├── main.py               # Entry point
└── requirements.txt      # Dependencies
⚙️ Installation
<div> <ol> <li><strong>Clone repository</strong>: <pre><code>git clone https://github.com/username/JARVIS.git cd JARVIS</code></pre> </li> <li><strong>Install dependencies</strong>: <pre><code>pip install -r requirements.txt</code></pre> </li> <li><strong>Download LLM model</strong>: <ul> <li>Place <code>Meta-Llama-3-8B-Instruct.Q4_0.gguf</code> in <code>models/</code> folder</li> <li>Or run: <pre><code>python -m gpt4all download Meta-Llama-3-8B-Instruct.Q4_0.gguf --path models/</code></pre> </li> </ul> </li> </ol> </div>
🖥️ Usage
bash
python main.py
⚙️ Configuration
Edit <code>config.py</code> to customize:

python
CONFIG = {
    "user_name": "Master",          # Your name
    "hotword": "jarvis",            # Wake word
    "voice_enabled": True,          # Enable voice
    "theme": "dark",                # Default theme
    "default_browser": "chrome",    # Default browser
    # ... and more
}
📌 System Requirements
<table> <tr> <th>Component</th> <th>Minimum</th> <th>Recommended</th> </tr> <tr> <td>RAM</td> <td>8GB</td> <td>16GB+</td> </tr> <tr> <td>Storage</td> <td>10GB</td> <td>20GB (for models)</td> </tr> <tr> <td>OS</td> <td colspan="2">Windows 10/11, Linux, macOS</td> </tr> </table>
🤖 Supported AI Models
<div> <ul> <li><code>Meta-Llama-3-8B-Instruct.Q4_0.gguf</code> (default)</li> <li>Other GGUF models can be added to <code>models/</code> folder</li> </ul> </div>
📄 License
This project is licensed under the <a href="LICENSE.txt">MIT License</a>.