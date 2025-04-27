from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from config import CONFIG

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        self.setIcon(QIcon(str(CONFIG["icon_path"])))
        
        menu = QMenu()
        
        show_action = QAction("Show", self)
        show_action.triggered.connect(self.parent.show)
        menu.addAction(show_action)
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.parent.close)
        menu.addAction(exit_action)
        
        self.setContextMenu(menu)
        self.show()