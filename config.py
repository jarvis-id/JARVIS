import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

CONFIG = {
    "user_name": "Master",
    "hotword": "jarvis",
    "voice_enabled": True,
    "theme": "dark",
    "default_browser": "chrome",
    "youtube_url": "https://www.youtube.com/results?search_query=",
    
    # Path configuration
    "base_dir": BASE_DIR,
    "assets_dir": BASE_DIR / "assets",
    "gpt4all_path": BASE_DIR / "gpt4all",
    "model_name": "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    
    # AI Settings
    "max_tokens": 1024,
    "temperature": 0.7,
    
    # File paths
    "icon_path": BASE_DIR / "assets" / "icon.png",
    "logo_path": BASE_DIR / "assets" / "logo.png",
    "mic_icon_path": BASE_DIR / "assets" / "mic.png"
}

# Create required directories
CONFIG["gpt4all_path"].mkdir(parents=True, exist_ok=True)
CONFIG["assets_dir"].mkdir(parents=True, exist_ok=True)