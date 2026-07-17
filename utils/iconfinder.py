from PySide6.QtGui import QPixmap, QPainter, QColor, QFont, QFontDatabase, QFontMetrics
from PySide6.QtCore import Qt
from utils.resourcepath import spath

def iconPixmap(unicodeChar, fontSize, color):
    fontPath = spath("resources", "icon.otf")
    fontId = QFontDatabase.addApplicationFont(fontPath)
    if fontId == -1:
        raise RuntimeError(f"Cannot load font: {fontPath}")

    family = QFontDatabase.applicationFontFamilies(fontId)[0]
    font = QFont(family)
    font.setPixelSize(fontSize)

    metrics = QFontMetrics(font)
    rect = metrics.boundingRect(unicodeChar)

    pixmap = QPixmap(rect.width(), rect.height())
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setRenderHint(QPainter.TextAntialiasing)

    painter.setFont(font)
    painter.setPen(QColor(color))
    painter.drawText(-rect.left(), -rect.top(), unicodeChar)

    painter.end()

    return pixmap