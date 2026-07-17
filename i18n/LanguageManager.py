import json
from i18n.translator import Translator
from utils.resourcepath import spath

class LanguageManager:
    def __init__(self, SettingsManager):
        self.settings = SettingsManager
        self.settings.get("ui.lang", "en")   

        self.translator = Translator()
        self.translator.load(self.getLanguage())
    
    def tr(self, key):
        return self.translator.tr(key)

    def getLanguage(self):
        return self.settings.get("ui.lang", "en")

    def setLanguage(self, language):
        self.settings.set("ui.lang", language)
        self.translator.load(language)