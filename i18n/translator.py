import json
from utils.resourcepath import spath


class Translator:
    def __init__(self):
        self.translations = {}

    def load(self, language="en"):
        filePath = spath("i18n", "languages", f"{language}.json")

        try:
            with open(filePath, "r", encoding="utf-8") as f:
                self.translations = json.load(f)

        except FileNotFoundError:
            print(f"Language file not found: {language}.json")
            self.translations = {}

        except json.JSONDecodeError:
            print(f"Invalid JSON in language file: {language}.json")
            self.translations = {}

    def tr(self, key):
        if key in self.translations:
            return self.translations[key]

        normalized = key.strip().lower()
        if normalized in self.translations:
            return self.translations[normalized]

        return key