import logging
from gpt4all import GPT4All
from .commands import CommandSystem
from .hardware import HardwareMonitor
from .voice import VoiceSystem
from config import CONFIG

class JarvisAI:
    def __init__(self):
        self.logger = self._setup_logger()
        self.commands = CommandSystem(self)
        self.hardware = HardwareMonitor()
        self.voice = VoiceSystem()
        self.ai_model = self._initialize_ai_model()
        
    def _setup_logger(self):
        logger = logging.getLogger("JARVIS")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(CONFIG["base_dir"] / "jarvis.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
        
    def _initialize_ai_model(self):
        try:
            model = GPT4All(
                model_name=CONFIG["model_name"],
                model_path=str(CONFIG["gpt4all_path"]),
                allow_download=True
            )
            self.logger.info("AI model initialized successfully")
            return model
        except Exception as e:
            self.logger.error(f"Error initializing AI model: {e}")
            return None
    
    def process(self, input_text):
        try:
            # Check special commands first
            special_response = self.commands.check_special_commands(input_text)
            if special_response:
                return special_response
                
            # Use AI if no special command matched
            if self.ai_model:
                with self.ai_model.chat_session():
                    response = self.ai_model.generate(
                        input_text,
                        max_tokens=CONFIG["max_tokens"],
                        temp=CONFIG["temperature"]
                    )
                    return response.strip()
            return "AI model is not available."
            
        except Exception as e:
            self.logger.error(f"Processing error: {e}")
            return "Sorry, I encountered an error processing your request."