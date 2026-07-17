from .LanguageManager import LanguageManager
from .translator import Translator

languageManager = None

def initialize(settings):
    global languageManager

    languageManager = LanguageManager(settings)

def tr(key):
    return languageManager.tr(key)