from PyQt5.QtGui import QColor

def apply_theme(window, theme):
    if theme == "dark":
        window.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QTextEdit, QLineEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 1px solid #444;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #333;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #444;
            }
            QLabel {
                color: #ffffff;
            }
        """)
    else:
        window.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTextEdit, QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #e0e0e0;
                color: black;
                border: none;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)