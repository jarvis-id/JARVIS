import pyttsx3
import speech_recognition as sr
from config import CONFIG

class VoiceSystem:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = self._init_tts()
        
    def _init_tts(self):
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)  # English male voice
            engine.setProperty('rate', 150)
            return engine
        except Exception as e:
            print(f"Error initializing TTS: {e}")
            return None
    
    def speak(self, text):
        if CONFIG["voice_enabled"] and self.engine:
            self.engine.say(text)
            self.engine.runAndWait()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5)
        
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Recognition service unavailable"