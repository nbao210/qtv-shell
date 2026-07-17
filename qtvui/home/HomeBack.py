import sys
import os
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QVariantAnimation, QEasingCurve
from PySide6.QtGui import QPainter, QPixmap

from services.WallpaperManager import WallpaperManager
from utils.resourcepath import spath

class HomeBack(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._old_pixmap = QPixmap(spath("resources", "background", "back.png"))
        self._new_pixmap = QPixmap()
        self._opacity = 0.0 

        self.fade_anim = QVariantAnimation(self)
        self.fade_anim.setDuration(800)  
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.setEasingCurve(QEasingCurve.InOutQuad)  
        self.fade_anim.valueChanged.connect(self._update_opacity)
        self.fade_anim.finished.connect(self._on_fade_finished)

        cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
        os.makedirs(cache_dir, exist_ok=True)
        self.cache_path = os.path.join(cache_dir, "bing_wallpaper.jpg")
        
        self.wp_manager = WallpaperManager(self.cache_path)
        self.wp_manager.wallpaperChanged.connect(self.fadeToNewWallpaper)

        self.wp_manager.start()

    def fadeToNewWallpaper(self, path):
        base = QPixmap(path)
        overlay = QPixmap(spath("resources", "background", "logo.png"))

        painter = QPainter(base)
        painter.drawPixmap(0, 0, overlay)
        painter.end()

        if not base.isNull():
            self._new_pixmap = base
            self.fade_anim.start()  

    def _update_opacity(self, value):
        self._opacity = value
        self.update()  

    def _on_fade_finished(self):
        self._old_pixmap = self._new_pixmap
        self._opacity = 0.0 
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        rect = self.rect()
        if not self._old_pixmap.isNull():
            scaled_old = self._old_pixmap.scaled(rect.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled_old)
        else:
            painter.fillRect(rect, Qt.gray)

        if self.fade_anim.state() == QVariantAnimation.Running and not self._new_pixmap.isNull():
            scaled_new = self._new_pixmap.scaled(rect.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            
            painter.setOpacity(self._opacity)
            painter.drawPixmap(0, 0, scaled_new)
            painter.setOpacity(1.0)  