import os, json
class App:

    def __init__(self,id,name,vendor,icon, version):
        self.id = id
        self.name = name
        self.vendor = vendor
        self.icon = icon
        self.ver = version

class AppManager:
    def __init__(self, apps_path):
        self.apps_path = apps_path
        self.apps = []

    def scan_apps(self):
        self.apps.clear()
        if not os.path.exists(self.apps_path):
            return []

        for folder in os.listdir(self.apps_path):
            app_folder = os.path.join(self.apps_path, folder)

            if not os.path.isdir(app_folder): continue

            json_file = os.path.join(app_folder,"app.json")

            if not os.path.exists(json_file):continue

            try:
                with open(json_file,"r",encoding="utf-8") as f:
                    data = json.load(f)

                icon_value = data.get("icon", "")
                icon_value = icon_value.replace("\\", "/")
                icon_path = os.path.normpath(os.path.join(app_folder, icon_value))
                app = App(
                    id=data["id"],
                    name=data["name"],
                    vendor=data.get("vendor", ""),
                    icon=icon_path,
                    version=data.get("version", "")
                )
                self.apps.append(app)


            except Exception as e:
                print(f"Load app {folder} failed:",e)
        return self.apps

    def get_apps(self):
        return self.apps