from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGraphicsDropShadowEffect, QSizePolicy
from PySide6.QtCore import Qt, QTimer, QTime, QSize
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QFont, QLinearGradient



class HomeOverlay(QWidget):
    def __init__(self, parent=None, settings=None, timemgr=None):
        super().__init__(parent)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.settings = settings
        self.timemgr = timemgr

        self.DigitalClock = DigitalClockOverlay(self, settings, timemgr)

    def resizeEvent(self, event):
        w = self.width()
        h = self.height()

        clock_width = 280
        clock_height = 100

        clock_x = 30
        clock_y = 30

        self.DigitalClock.setGeometry(clock_x, clock_y, clock_width, clock_height)



class DigitalClockOverlay(QWidget):
    def __init__(self, parent=None, settings=None, timemgr=None):
        super().__init__(parent)
        self.settings = settings    
        self.width = 280
        self.height = 100
        self.setFixedSize(self.width, self.height)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timemgr = timemgr
        self.setupUi()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.updateTime()

    def setupUi(self):
        self.card = QWidget(self)
        self.card.setGeometry(0, 0, self.width, self.height)
        self.card.setAttribute(Qt.WA_TranslucentBackground)

        shadow = QGraphicsDropShadowEffect(self.card)
        shadow.setBlurRadius(28)
        shadow.setOffset(0, 8)
        shadow.setColor(QColor(0, 0, 0, 140))
        self.card.setGraphicsEffect(shadow)

        layout = QVBoxLayout(self.card)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(0)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(4)
        row.setAlignment(Qt.AlignCenter)

        self.timeLabel = QLabel("--:--", self.card)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("""
            QLabel {
                color: rgba(225, 190, 110, 245);
                font-family: 'Inter', 'Segoe UI Light';
                font-size: 70px;
                font-weight: 145;
                letter-spacing: 0px;
                background: transparent;
            }
        """)
        self.timeLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.timeLabel.setFixedHeight(82)
        row.addWidget(self.timeLabel, 0, Qt.AlignCenter)
        
        if self.settings.get("time.24h", False) == False:
            self.ampmLabel = QLabel("", self.card)
            self.ampmLabel.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
            self.ampmLabel.setStyleSheet("""
                QLabel {
                    color: rgba(225, 190, 110, 245);
                    font-family: 'Inter', 'Segoe UI Light';
                    font-size: 35px;
                    font-weight: 150;
                    letter-spacing: 0px;
                    background: transparent;
                    padding: 0px;
                    margin-bottom: 0px;
                }
            """)
            self.ampmLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            self.ampmLabel.setFixedHeight(45)
            row.addWidget(self.ampmLabel, 0, Qt.AlignBottom)

        layout.addLayout(row)
        layout.addStretch(1)

        self.setStyleSheet("""
            DigitalClockOverlay {
                background: transparent;
            }
        """)

    def updateTime(self):
        if not self.settings.get("time.24h",False):
            self.ampmLabel.setText(self.timemgr.getAmPm())
            self.timeLabel.setText(self.timemgr.getShortTime(showAP=False))
        else:
            self.timeLabel.setText(self.timemgr.getShortTime())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.card.geometry().adjusted(1, 1, -1, -1)

        grad = QLinearGradient(rect.topLeft(), rect.bottomRight())
        grad.setColorAt(0.0, QColor(30, 30, 35, 125))
        grad.setColorAt(0.45, QColor(25, 25, 30, 105))
        grad.setColorAt(1.0, QColor(15, 15, 20, 90))

        painter.setBrush(QBrush(grad))
        painter.setPen(QPen(QColor(255, 255, 255, 35), 1))
        painter.drawRoundedRect(rect, 18, 18)

        inner = rect.adjusted(1, 1, -1, -1)
        painter.setPen(QPen(QColor(255, 255, 255, 18), 1))
        painter.drawRoundedRect(inner, 16, 16)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    clock_overlay = DigitalClockOverlay()
    clock_overlay.show()
    sys.exit(app.exec())