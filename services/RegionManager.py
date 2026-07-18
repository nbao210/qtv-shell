import json
from utils.resourcepath import spath
from pathlib import Path

class RegionManager:
    def __init__(self,settings):
        self.settings = settings
        self.currentRegion = self.settings.get("time.regionformat", "non")

        self.regionConfig = self.loadRegionConfig()
        self.validateAndFix()

    def loadRegionConfig(self):
        file_path = Path(spath("i18n", "regionformat", f"{self.currentRegion}.json"))
        if not file_path.exists():
            print(f"Region '{self.currentRegion}' not found, fallback to en")
            self.currentRegion = "en"
            self.settings.set("time.regionformat", "en")
            file_path = Path(spath("i18n", "regionformat", "en.json"))
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)["time"]["format"]
        except Exception as e:
            print(f"Error loading region: {e}")
            return {}

    def validateAndFix(self):
        format_mapping = {
            "first_day": ("first_day", True),
            "short_date": ("short_date", False),
            "long_date": ("long_date", False),
            "short_time": ("short_time_24h" if self.settings.get("time.24h") else "short_time_12h", False),
            "long_time": ("long_time_24h" if self.settings.get("time.24h") else "long_time_12h", False),
            "am_sym": ("am_sym", False),
            "pm_sym": ("pm_sym", False)
        }

        for config_key, (region_key, is_index_mode) in format_mapping.items():
            current_value = self.settings.get(f"time.format.{config_key}")
            available_options = self.regionConfig.get(region_key, [])

            if is_index_mode:
                if not isinstance(current_value, int) or current_value < 0 or current_value >= len(available_options):
                    print(f"Invalid index for {config_key}, resetting to 0")
                    self.settings.set(f"time.format.{config_key}", 0)
            else:
                if current_value not in available_options:
                    print(f"Invalid value '{current_value}' for {config_key}, resetting to default.")
                    if available_options:
                        self.settings.set(f"time.format.{config_key}", available_options[0])