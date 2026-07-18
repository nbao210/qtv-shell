import os
import requests
from PySide6.QtCore import QObject, Signal, QThread, QTimer
import math
import random
import requests
from bs4 import BeautifulSoup

class WallpapersCraftProvider:
    def __init__(self, category="nature", resolution="1920x1080"):
        self.category = category
        self.resolution = resolution
        self.baseUrl = "https://wallpaperscraft.com"

    def getSoup(self, url):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def getWallpaperCount(self):
        url = (
            f"{self.baseUrl}/catalog/"
            f"{self.category}/downloads/"
            f"{self.resolution}"
        )

        soup = self.getSoup(url)
        categoryLink = soup.select_one(f'a[href="/catalog/{self.category}/downloads/{self.resolution}"] .filter__count')

        if not categoryLink:
            return 15

        return int(categoryLink.text.strip())

    def getWallpaperUrl(self):
        try:
            count = self.getWallpaperCount()
            totalPages = 50
            page = random.randint(1, totalPages)

            catalogUrl = (
                f"{self.baseUrl}/catalog/"
                f"{self.category}/downloads/"
                f"{self.resolution}/page{page}"
            )

            soup = self.getSoup(catalogUrl)
            wallpapers = soup.select("ul.wallpapers__list .wallpapers__link")

            if not wallpapers:
                return None

            wallpaper = random.choice(wallpapers)
            detailUrl = self.baseUrl + wallpaper["href"]

            detailSoup = self.getSoup(detailUrl)
            download = detailSoup.select_one("a.gui-button[download]")

            if not download:
                return None
            print(count, totalPages, page, detailUrl)
            return download["href"]

        except Exception as e:
            print("WallpapersCraft error:", e)
            return None

class WallpaperWorker(QThread):
    finished = Signal(bool, str)

    def __init__(self, provider, cachePath, parent=None):
        super().__init__(parent)
        self.provider = provider
        self.cachePath = cachePath

    def run(self):
        try:
            url = self.provider.getWallpaperUrl()
            image = requests.get(url, timeout=15, allow_redirects=True)
            image.raise_for_status()
            with open(self.cachePath, "wb") as file:
                file.write(image.content)

            self.finished.emit(True, self.cachePath)

        except Exception as e:
            self.finished.emit(False, str(e))


class WallpaperManager(QObject):
    wallpaperChanged = Signal(str)

    def __init__(self, cachePath):
        super().__init__()
        self.provider = WallpapersCraftProvider()
        self.cachePath = cachePath
        self.worker = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateWallpaper)

    def start(self):
        QTimer.singleShot(5000, self.updateWallpaper)
        self.timer.start(1800000)  

    def updateWallpaper(self):
        if self.worker and self.worker.isRunning():
            return

        self.worker = WallpaperWorker(self.provider, self.cachePath, self)
        self.worker.finished.connect(self.onWorkerFinished)
        self.worker.finished.connect(self.worker.deleteLater)
        
        self.worker.start()

    def onWorkerFinished(self, success, result):
        self.worker = None
        if success:
            self.wallpaperChanged.emit(result)
        else:
            print(f"[Q-TV Wallpaper Error]: {result}")

    def stop(self):
        self.timer.stop()
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()