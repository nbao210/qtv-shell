import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtGui import QPainter, QBrush, QPixmap
from core.NavigationManager import NavManager, NavArea
import os
import i18n
from qtvui.home.HomeBack import HomeBack
from qtvui.home.HomeBar import HomeBar
from core.AppsManager import AppManager
from utils.resourcepath import spath
from core.SettingsManager import SettingsManager
from i18n.LanguageManager import LanguageManager

settings = SettingsManager()    
manager = AppManager(spath("program"))
i18n.initialize(settings)


apps = manager.scan_apps()
for app in apps:
    print(app.name, app.icon)

class NavArea(QObject):

    requestChangeArea = Signal(str)

    def handleKey(self, key):
        pass

class mainWindow(QWidget):
    MARGIN = 30
    BAR_HEIGHT_RATIO = 0.36

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q-TV")
        self.back = HomeBack(self)
        self.bar = HomeBar(apps=apps, parent=self)

        self.nav = NavManager()
        self.nav.registerArea("HomeBar", self.bar)
        self.nav.setArea("HomeBar")

        self.showFullScreen()

    def closeEvent(self, event):
        self.back.wp_manager.stop() 
        event.accept() 

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = self.width()
        h = self.height()
        m = self.MARGIN

        self.back.setGeometry(0, 0, w, h)

        bar_h = int(h * self.BAR_HEIGHT_RATIO)
        bar_w = w - 2 * m
        bar_x = m
        bar_y = h - bar_h - m  

        self.bar.setGeometry(bar_x, bar_y, bar_w, bar_h)

    def keyPressEvent(self, event):
        self.nav.handleKey(event.key())
        event.accept()
    

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    