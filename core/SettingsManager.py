import json
from utils.resourcepath import spath

defaultConfiguration = {
    "ui": {
        "lang": "en"
    },
}

class SettingsManager:
    def __init__(self):
        self.configFilePath = spath("data","config.json")
        self.load()
        
    def load(self):
        try:
            with open(self.configFilePath, 'r') as f:
                config = json.load(f)
                self.currentConfig = config
        except FileNotFoundError:
            self.reset()
        except json.JSONDecodeError:
            print("Error: Invalid JSON in configuration file.")
            self.reset()

    def reset(self):
        self.currentConfig = defaultConfiguration
        self.save()

    def save(self):
        with open(self.configFilePath, 'w') as f:
            json.dump(self.currentConfig, f, indent=4)

    def get(self, key, default=None):
        keys = key.split('.')
        value = self.currentConfig

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key, value):
        keys = key.split('.')
        config = self.currentConfig

        for k in keys[:-1]:
            if k not in config or not isinstance(config[k], dict):
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value
        self.save()

    
    