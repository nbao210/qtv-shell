import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QScrollArea, QVBoxLayout,
    QMainWindow, QFrame, QSizePolicy, QTabWidget, QFrame, QTabBar, 
)
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QFontMetrics, QColor, QPen, QIcon, QLinearGradient, QPainterPathStroker
from PySide6.QtCore import QRectF, QTimer, Qt, QSize, QPropertyAnimation, QRect, QEasingCurve, QVariantAnimation, Property
from utils.iconfinder import iconPixmap
from core.NavigationManager import NavArea
from i18n import tr


def roundedPixmap(path, size, radius):
    pixmap = QPixmap(path).scaled(size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

    result = QPixmap(size)
    result.fill(Qt.transparent)

    painter = QPainter(result)
    painter.setRenderHint(QPainter.Antialiasing)

    clip = QPainterPath()
    clip.addRoundedRect(0, 0, size.width(), size.height(), radius, radius)

    painter.setClipPath(clip)
    painter.drawPixmap(0, 0, pixmap)

    painter.end()

    return result

from PySide6.QtCore import Property

class AnimLabel(QLabel):
    def __init__(self):
        super().__init__()

        self._textColor = QColor("#808080")
        self._offsetY = -3

    def setTextColor(self, color):
        self._textColor = color
        self.update()

    def getTextColor(self):
        return self._textColor

    def setOffsetY(self, value):
        self._offsetY = value
        self.update()

    def getOffsetY(self):
        return self._offsetY

    color = Property(QColor, getTextColor, setTextColor)
    offset = Property(float, getOffsetY, setOffsetY)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(self._textColor)

        metrics = QFontMetrics(self.font())
        baseline_y = self.height() - metrics.descent()

        painter.drawText(
            self.rect(),
            Qt.AlignHCenter | Qt.AlignVCenter,
            self.text()
        )

class ImageLabel(QLabel):

    def __init__(self):
        super().__init__()

        self.radius = 20
        self.focused = False
        
        self._scale = 1.0
        self.scale_animation = QPropertyAnimation(self, b"scale")
        self.scale_animation.setDuration(200)
        self.scale_animation.setEasingCurve(QEasingCurve.OutCubic)
        
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)

    def setFocused(self, focused):
        self.focused = focused
        self.update()

    def getScale(self):
        return self._scale

    def setScale(self, value):
        self._scale = value
        self.update()

    scale = Property(float, getScale, setScale)

    def paintEvent(self, event):
        super().paintEvent(event)
        
        if self._scale != 1.0 and self.pixmap() and not self.pixmap().isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
            
            pixmap = self.pixmap()
            scaled_size = pixmap.size() * self._scale

            x = (self.width() - scaled_size.width()) / 2
            y = (self.height() - scaled_size.height()) / 2
            
            scaled_pixmap = pixmap.scaledToWidth(int(scaled_size.width()), Qt.SmoothTransformation)
            painter.drawPixmap(int(x), int(y), scaled_pixmap)

            if self.focused:
                pen = QPen(QColor("#FFD54F"))
                pen.setWidth(6)
                painter.setPen(pen)
                painter.setBrush(Qt.NoBrush)

                painter.drawRoundedRect(QRectF(x + 1.5,y + 1.5,scaled_size.width() - 3,scaled_size.height() - 3),self.radius,self.radius)

            painter.end()

    def enterEvent(self, event):
        self.animateScale(1.03)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animateScale(1.0)
        super().leaveEvent(event)

    def animateScale(self, value):
        self.scale_animation.stop()
        self.scale_animation.setStartValue(self._scale)
        self.scale_animation.setEndValue(value)
        self.scale_animation.start()

class AppCard(QWidget):
    def __init__(self, app):
        super().__init__()


        self.app = app
        self.focused = False

        self.padding = 5
        self.radius = 20
        self.labelHeight = 30
        self.spacing = 0

        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(self.padding, self.padding, self.padding, self.padding)
        layout.setSpacing(self.spacing)

        self.icon = ImageLabel()
        self.icon.setAlignment(Qt.AlignCenter)

        self.nameLabel = AnimLabel()
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.nameLabel.setFixedHeight(self.labelHeight)
        self.nameLabel.setStyleSheet("color: white; font-size: 23px; font-family: Segoe UI;")

        layout.addWidget(self.icon)
        layout.addWidget(self.nameLabel)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        iconPath = getattr(self.app, "icon", None)

        if not iconPath or not os.path.exists(iconPath):
            self.icon.setPixmap(QPixmap())
            self.icon.setText("No image")
            return

        bannerHeight = self.height() - self.padding * 2 - self.labelHeight - self.spacing
        bannerHeight = max(120, bannerHeight)
        bannerWidth = max(200, int(bannerHeight * 16 / 9))

        self.icon.setFixedSize(bannerWidth, bannerHeight)

        if iconPath and os.path.exists(iconPath):
            small_size = self.icon.size() - QSize(15, 15)
            self.icon.setPixmap(roundedPixmap(iconPath, small_size, self.radius))
            self.icon.setText("")
            self.icon.setStyleSheet("")
        else:
            self.icon.setPixmap(QPixmap())
            self.icon.setText("No image")
            self.icon.setStyleSheet("color: white; font-size: 18px;")

        self.setFixedWidth(bannerWidth + self.padding * 2)
        self.nameLabel.setFixedWidth(bannerWidth)
        name = getattr(self.app, "name", "") or ""
        metrics = QFontMetrics(self.nameLabel.font())
        elided = metrics.elidedText(name, Qt.ElideRight, bannerWidth)
        self.nameLabel.setText(elided)

    def setFocused(self, focused):
        self.focused = focused

        self.icon.setFocused(focused)

        colorAnim = QPropertyAnimation(self.nameLabel, b"color")
        offsetAnim = QPropertyAnimation(self.nameLabel, b"offset")

        colorAnim.setDuration(150)
        offsetAnim.setDuration(150)

        if focused:
            colorAnim.setStartValue(QColor("#808080"))
            colorAnim.setEndValue(QColor("#FFFFFF"))

            offsetAnim.setStartValue(-3)
            offsetAnim.setEndValue(0)

            self.icon.animateScale(1.03)

        else:
            colorAnim.setStartValue(QColor("#FFFFFF"))
            colorAnim.setEndValue(QColor("#808080"))

            offsetAnim.setStartValue(0)
            offsetAnim.setEndValue(-3)

            self.icon.animateScale(1.0)

        colorAnim.start()
        offsetAnim.start()

        self.colorAnim = colorAnim
        self.offsetAnim = offsetAnim


    def enterEvent(self, event):
        self.setFocused(True)
        super().enterEvent(event)


    def leaveEvent(self, event):
        self.setFocused(False)
        super().leaveEvent(event)

class FadeOverlay(QWidget):
    def __init__(self, side="right", parent=None):
        super().__init__(parent)

        self.side = side
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), 35, 35)

        painter.setClipPath(path)

        gradient = QLinearGradient(0, 0, self.width(), 0)

        if self.side == "right":
            gradient.setColorAt(0, QColor(30,31,28,0))
            gradient.setColorAt(1, QColor(30,31,28,255))
        else:
            gradient.setColorAt(0, QColor(30,31,28,255))
            gradient.setColorAt(1, QColor(30,31,28,0))

        painter.fillRect(self.rect(), gradient)

class TabBarWithHighlight(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFocusPolicy(Qt.NoFocus)  
        self._highlightRect = QRect()
        self.anim = QPropertyAnimation(self, b"highlightRect")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)

        self.focused = False

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down):
            event.accept()
            return
        super().keyPressEvent(event)

    def getHighlightRect(self):
        return self._highlightRect

    def setHighlightRect(self, rect):
        self._highlightRect = rect
        self.update()

    highlightRect = Property(QRect, getHighlightRect, setHighlightRect)

    def moveHighlightTo(self, rect, animate=True):
        self.anim.stop()

        if animate:
            self.anim.setStartValue(self._highlightRect)
            self.anim.setEndValue(rect)
            self.anim.start()
        else:
            self.setHighlightRect(rect)

    def focus(self):
        self.focused = True
        self.update()

    def unfocus(self):
        self.focused = False
        self.update()

    def handleKey(self, key):
        oldIndex = self.currentIndex()

        if key == Qt.Key_Right:
            self.setCurrentIndex(min(self.currentIndex() + 1, self.count() - 1))

        elif key == Qt.Key_Left:
            self.setCurrentIndex(max(self.currentIndex() - 1, 0))

        if self.currentIndex() != oldIndex:
            self.updateHighlight()

    def updateHighlight(self):
        rect = self.tabRect(self.currentIndex())
        self.moveHighlightTo(rect)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)

        if self.focused:
            painter.setBrush(QColor("#686868"))
        else:
            painter.setBrush(QColor("#3A3A3A"))

        painter.drawRoundedRect(self._highlightRect, 15, 15)

        painter.end()

        super().paintEvent(event)    
            
class HomeBar(QTabWidget, NavArea):
    def __init__(self, apps, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setTabPosition(QTabWidget.South)   
        self.setFocusPolicy(Qt.StrongFocus)

        self.currentArea = "AppList"

        self._customTabBar = TabBarWithHighlight(self)
        self.setTabBar(self._customTabBar)
        self.tabBar().setFocusPolicy(Qt.NoFocus)

        #self.setDocumentMode(True)
        self.tabBar().setDrawBase(False)

        self.setStyleSheet("""
            QTabWidget::pane {
                background-color: rgba(30,31,28,220);
                border-top-left-radius: 35px;
                border-top-right-radius: 35px;
                border-bottom-right-radius: 35px;
                border: none;
                border-bottom-left-radius: 0px;
            }
            QTabBar {
                background-color: rgba(30,31,28,220);
                border-bottom-left-radius: 20px;
                outline: 0px;
                border: none;
                border-bottom-right-radius: 20px;
            }
            QTabBar::tab {
                background: transparent;
                color: white;
                padding: 20px 30px;
                border: none;
                outline: 0px;
                font-size: 21px;
                font-family: Segoe UI;
            }
            QTabBar::tab:selected {
                font-weight: bold;
                outline: 0px;
            }
        """)

        self.AppList = AppList(apps)
        self.AppList.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.AppList.setFocusPolicy(Qt.NoFocus)

        settings_label = Settings()

        self.addTab(self.AppList, QIcon(iconPixmap("\uf015", 50, "#FFFFFF")), tr("Home"))
        self.addTab(settings_label, QIcon(iconPixmap("\uf013", 50, "#FFFFFF")), tr("Settings"))
        self.addTab(Wallpaper(), QIcon(iconPixmap("\uf302", 50, "#FFFFFF")), tr("Wallpaper"))
        self.setIconSize(QSize(22, 22))

        self.currentChanged.connect(self.onTabChanged)

        QTimer.singleShot(0, lambda: self.animateTab(0, animate=False))

    def onTabChanged(self, index):
        QTimer.singleShot(0, lambda: self.animateTab(index, animate=True))


    def animateTab(self, index, animate=True):
        rect = self.tabBar().tabRect(index)
        rect.adjust(5, 5, -5, -5)
        self.tabBar().moveHighlightTo(rect, animate=animate)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "_customTabBar"):
            self.animateTab(self.currentIndex(), animate=False)

    def handleKey(self, key):
        if self.currentArea == "AppList":
            if key == Qt.Key_Down:
                self.AppList.unfocus()
                self._customTabBar.focus()
                self.currentArea = "TabBar"
            else:
                self.AppList.handleKey(key)
            
        elif self.currentArea == "TabBar":
            if key == Qt.Key_Up:
                self.AppList.focus()
                self._customTabBar.unfocus()
                self.currentArea = "AppList"
            elif key == Qt.Key_Left or key == Qt.Key_Right:
                self._customTabBar.handleKey(key)
                # Stay in TabBar area when navigating left/right
            else:
                self._customTabBar.handleKey(key)
    
    def focus(self):
        self.currentArea = "AppList"
        self.AppList.focus()
        self._customTabBar.unfocus()
        self._customTabBar.setCurrentIndex(self.currentIndex())

    def unfocus(self):
        if self.currentArea == "AppList":
            self.AppList.unfocus()
        elif self.currentArea == "TabBar":
            self._customTabBar.unfocus()

    

class AppList(QWidget):
    def __init__(self, apps, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            AppList {
                background-color: transparent;
            }
            """
        )
        self.apps = apps
        self.setContentsMargins(8,8,8,8)
        self.setFocusPolicy(Qt.NoFocus)

        self.currentIndex = 0

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setFocusPolicy(Qt.NoFocus)

        self.scroll.setStyleSheet("background: transparent; border: none;")

        self.container = QWidget()
        self.container.setStyleSheet("background: transparent;")
        self.container.setFocusPolicy(Qt.NoFocus)

        self.layout = QHBoxLayout(self.container)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.container.setLayout(self.layout)

        self.scroll.setWidget(self.container)
        self.leftFade = FadeOverlay("left", self)
        self.rightFade = FadeOverlay("right", self)

        self.leftFade.hide()
        self.rightFade.hide()
                

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(5,5,5,5)
        main_layout.addWidget(self.scroll)
        self.setLayout(main_layout)

        self.scroll.horizontalScrollBar().valueChanged.connect(lambda: self.updateFade())

        self.cards = []
        self.initUI()
        QTimer.singleShot(0, self.updateFade)

    def initUI(self):
        for app in self.apps:
            card = AppCard(app)
            self.cards.append(card)
            self.layout.addWidget(card)
        self.layout.addStretch()

        if self.cards:
            self.cards[0].setFocused(True)

    def keyPressEvent(self, event):
        self.handleKey(event.key())
        event.accept()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        size = 100
        self.leftFade.setGeometry(0,0,size,self.height())
        self.rightFade.setGeometry(self.width() - size,0,size,self.height())
        

    def updateFade(self):
        bar = self.scroll.horizontalScrollBar()
        self.leftFade.setVisible(bar.value() > bar.minimum())
        self.rightFade.setVisible(bar.value() < bar.maximum())
    
    def handleKey(self, key):
        if not self.cards:
            return

        oldIndex = self.currentIndex

        if key == Qt.Key_Left:
            self.currentIndex = max(0, self.currentIndex - 1)

        elif key == Qt.Key_Right:
            self.currentIndex = min(len(self.cards) - 1, self.currentIndex + 1)

        if self.currentIndex != oldIndex:
            self.cards[oldIndex].setFocused(False)
            self.cards[self.currentIndex].setFocused(True)
            self.scroll.ensureWidgetVisible(self.cards[self.currentIndex], xmargin=50, ymargin=0)

    def focus(self):
        if self.cards:
            self.cards[self.currentIndex].setFocused(True)

    def unfocus(self):
        if self.cards:
            self.cards[self.currentIndex].setFocused(False)


class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            Settings {
                background-color: transparent;
            }
            """
        )
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        iconlbl = QLabel()
        iconlbl.setPixmap(QPixmap(iconPixmap("\uF7D9", 80, "#FFFFFF")).scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        iconlbl.setAlignment(Qt.AlignCenter)

        lbl = QLabel(tr("oops, under construction"))
        lbl.setStyleSheet("color: white; font-size: 25px; font-family: Segoe UI;")

        smllbl = QLabel(tr("back here soon..."))
        smllbl.setStyleSheet("color: white; font-size: 15px; font-family: Segoe UI;")
        smllbl.setAlignment(Qt.AlignCenter) 

        self.layout.addStretch()
        self.layout.addWidget(iconlbl)
        self.layout.addWidget(lbl)
        self.layout.addWidget(smllbl)
        self.layout.addStretch()


        lbl.setAlignment(Qt.AlignCenter)

class Wallpaper(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            """
            Settings {
                background-color: transparent;
            }
            """
        )
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        iconlbl = QLabel()
        iconlbl.setPixmap(QPixmap(iconPixmap("\uF7D9", 80, "#FFFFFF")).scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        iconlbl.setAlignment(Qt.AlignCenter)

        lbl = QLabel(tr("oops, under construction"))
        lbl.setStyleSheet("color: white; font-size: 25px; font-family: Segoe UI;")

        smllbl = QLabel(tr("back here soon...") + "\n " + tr("Special thanks to ") + "WallpapersCraft")
        smllbl.setStyleSheet("color: white; font-size: 15px; font-family: Segoe UI;")
        smllbl.setAlignment(Qt.AlignCenter) 

        self.layout.addStretch()
        self.layout.addWidget(iconlbl)
        self.layout.addWidget(lbl)
        self.layout.addWidget(smllbl)
        self.layout.addStretch()


        lbl.setAlignment(Qt.AlignCenter)
