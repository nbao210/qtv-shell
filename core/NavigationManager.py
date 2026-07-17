from PySide6.QtCore import QObject, Signal

class NavManager(QObject):
    areaChanged = Signal(str)
    def __init__(self):
        super().__init__()
        self.areas = {}
        self.currentArea = None

    def registerArea(self, name, area):
        self.areas[name] = area
        area.requestChangeArea.connect(self.changeArea)

    def setArea(self, name):
        if name not in self.areas:
            return
        if self.currentArea:
            self.currentArea.unfocus()

        self.currentArea = self.areas[name]
        self.currentArea.focus()

        self.areaChanged.emit(name)

    def handleKey(self, key):
        if self.currentArea:
            self.currentArea.handleKey(key)

    def changeArea(self, name):
        self.setArea(name)

class NavArea:

    requestChangeArea = Signal(str)

    def handleKey(self, key):
        pass

    def focus(self):
        pass

    def unfocus(self):
        pass