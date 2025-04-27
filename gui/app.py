from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, 
                            QLineEdit, QPushButton, QVBoxLayout, 
                            QWidget, QLabel, QHBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QTimer
from core.jarvis_ai import JarvisAI
from .tray_icon import TrayIcon
from .themes import apply_theme
from config import CONFIG
import sys

class JarvisGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis = JarvisAI()
        self._init_ui()
        self.tray_icon = TrayIcon(self)
        apply_theme(self, CONFIG["theme"])
        
    def _init_ui(self):
        self.setWindowTitle("J.A.R.V.I.S.")
        self.setMinimumSize(600, 500)
        
        # Main widget
        main_widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(str(CONFIG["logo_path"])).scaled(64, 64, Qt.KeepAspectRatio))
        header.addWidget(self.logo)
        
        self.status_label = QLabel("Ready")
        header.addWidget(self.status_label)
        layout.addLayout(header)
        
        # Chat area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)
        
        # Input area
        input_layout = QHBoxLayout()
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Type your command...")
        self.user_input.returnPressed.connect(self._process_input)
        input_layout.addWidget(self.user_input)
        
        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self._process_input)
        input_layout.addWidget(self.send_btn)
        
        self.mic_btn = QPushButton(QIcon(str(CONFIG["mic_icon_path"])), "")
        self.mic_btn.clicked.connect(self._voice_input)
        input_layout.addWidget(self.mic_btn)
        
        layout.addLayout(input_layout)
        
        # Status bar
        self.status_bar = QLabel()
        self._update_status()
        layout.addWidget(self.status_bar)
        
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        
        # Status update timer
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self._update_status)
        self.status_timer.start(5000)
        
        # Initial greeting
        self._add_message("J.A.R.V.I.S.", "Initializing systems...")
        self._add_message("J.A.R.V.I.S.", f"Hello {CONFIG['user_name']}, how can I assist you today?")
        self.jarvis.voice.speak(f"Hello {CONFIG['user_name']}, J.A.R.V.I.S. at your service.")
    
    def _process_input(self):
        text = self.user_input.text().strip()
        if text:
            self._add_message("You", text)
            self.user_input.clear()
            response = self.jarvis.process(text)
            self._add_message("J.A.R.V.I.S.", response)
            self.jarvis.voice.speak(response)
    
    def _voice_input(self):
        self._add_message("System", "Listening...")
        command = self.jarvis.voice.listen()
        self._add_message("You (Voice)", command)
        response = self.jarvis.process(command)
        self._add_message("J.A.R.V.I.S.", response)
        self.jarvis.voice.speak(response)
    
    def _add_message(self, sender, message):
        self.chat_display.append(f"<b>{sender}:</b> {message}")
        self.chat_display.ensureCursorVisible()
    
    def _update_status(self):
        self.status_bar.setText(self.jarvis.hardware.get_short_status())
    
    def closeEvent(self, event):
        self.hide()
        event.ignore()