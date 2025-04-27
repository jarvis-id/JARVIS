import sys
from PyQt5.QtWidgets import QApplication
from gui.app import JarvisGUI

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("J.A.R.V.I.S.")
    app.setApplicationDisplayName("J.A.R.V.I.S. AI Assistant")
    
    window = JarvisGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()