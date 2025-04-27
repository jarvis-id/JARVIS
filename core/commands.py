import webbrowser
from datetime import datetime
from config import CONFIG

class CommandSystem:
    def __init__(self, jarvis):
        self.jarvis = jarvis
        
    def check_special_commands(self, command):
        command_lower = command.lower()
        
        commands = {
            "id": {
                "buka youtube": self._open_youtube,
                "buka browser": self._open_browser,
                "info sistem": self._system_info,
                "jam berapa": self._current_time,
                "matikan": self._shutdown,
                "siapa anda": "Saya J.A.R.V.I.S., asisten AI Anda",
                "kemampuan anda": self._capabilities_id
            },
            "en": {
                "open youtube": self._open_youtube,
                "open browser": self._open_browser,
                "system info": self._system_info,
                "what time is it": self._current_time,
                "shutdown": self._shutdown,
                "who are you": "I am J.A.R.V.I.S., your AI assistant",
                "your capabilities": self._capabilities_en
            }
        }
        
        for lang, lang_commands in commands.items():
            for cmd, func in lang_commands.items():
                if cmd in command_lower:
                    return func(command) if callable(func) else func
        return None
    
    def _open_youtube(self, command):
        query = command.lower().replace("buka youtube", "").replace("open youtube", "").strip()
        webbrowser.get(CONFIG["default_browser"]).open(f"{CONFIG['youtube_url']}{query}")
        return "Membuka YouTube..." if self._detect_language(command) == "id" else "Opening YouTube..."
    
    def _open_browser(self, command):
        webbrowser.get(CONFIG["default_browser"]).open("https://www.google.com")
        return "Browser dibuka" if self._detect_language(command) == "id" else "Browser opened"
    
    def _system_info(self, command):
        return self.jarvis.hardware.get_full_info(self._detect_language(command))
    
    def _current_time(self, command):
        now = datetime.now()
        if self._detect_language(command) == "id":
            days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
            return f"Sekarang hari {days[now.weekday()]}, jam {now.strftime('%H:%M')}"
        return f"It's {now.strftime('%A, %H:%M')}"
    
    def _shutdown(self, command):
        self.jarvis.voice.speak("Mematikan sistem" if self._detect_language(command) == "id" else "Shutting down")
        exit(0)
    
    def _capabilities_id(self, command=None):
        return (
            "Saya dapat:\n"
            "- Membuka aplikasi dan browser\n"
            "- Mencari di YouTube\n"
            "- Memberikan informasi sistem\n"
            "- Menjawab pertanyaan umum\n"
            "- Beroperasi secara offline"
        )
    
    def _capabilities_en(self, command=None):
        return (
            "I can:\n"
            "- Open applications and browsers\n"
            "- Search on YouTube\n"
            "- Provide system information\n"
            "- Answer general questions\n"
            "- Operate offline"
        )
    
    def _detect_language(self, text):
        return "id" if any(keyword in text.lower() for keyword in ["apa", "siapa", "bagaimana"]) else "en"