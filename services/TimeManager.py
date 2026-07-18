from datetime import datetime
from zoneinfo import ZoneInfo
from utils.resourcepath import spath
from pathlib import Path
import json


class TimeManager:
    def __init__(self,settings):
        self.settings = settings
        self.loadConfig()

    def loadConfig(self):
        self.zone = self.settings.get("time.zone","Asia/Ho_Chi_Minh")
        self.manual = self.settings.get("time.manual",False)
        self.is24h = self.settings.get("time.24h",False)
        self.region = self.settings.get("time.regionformat","en")

        self.firstDay = self.settings.get("time.format.first_day",0)
        self.shortDateFormat = self.settings.get("time.format.short_date","dd/MM/yyyy")
        self.longDateFormat = self.settings.get("time.format.long_date","dddd, MMMM d, yyyy")
        self.shortTimeFormat = self.settings.get("time.format.short_time","HH:mm")
        self.longTimeFormat = self.settings.get("time.format.long_time","HH:mm:ss")
        self.amSym = self.settings.get("time.format.am_sym","AM")
        self.pmSym = self.settings.get("time.format.pm_sym","PM")

        self.regionData = self.loadRegionData()

    def loadRegionData(self):
        filePath = Path(spath("i18n","regionformat",f"{self.region}.json"))

        try:
            with open(filePath,"r",encoding="utf-8") as f:
                return json.load(f).get("time",{})
        except Exception as e:
            print(f"Error loading region data: {e}")
            return {}

    def now(self):
        if self.manual:
            return datetime.now()

        try:
            return datetime.now(ZoneInfo(self.zone))
        except Exception as e:
            print(f"Error loading timezone '{self.zone}': {e}")
            return datetime.now()

    def getDateTime(self):
        return self.now()

    def getYear(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.year

    def getMonth(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.month

    def getDay(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.day

    def getWeekday(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.weekday()

    def getHour(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.hour

    def getMinute(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.minute

    def getSecond(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.second

    def getDayName(self,dateTime=None):
        dateTime = dateTime or self.now()
        dayList = self.regionData.get("dayweek",[])

        if not dayList:
            return ""

        return dayList[dateTime.weekday()]

    def getMonthName(self,dateTime=None):
        dateTime = dateTime or self.now()
        monthList = self.regionData.get("month",[])

        if not monthList:
            return ""

        return monthList[dateTime.month - 1]

    def getAmPm(self,dateTime=None):
        dateTime = dateTime or self.now()

        if dateTime.hour < 12:
            return self.amSym

        return self.pmSym

    def getShortTime(self,dateTime=None,showAP=False):
        dateTime = dateTime or self.now()
        result = self.formatDateTime(dateTime,self.shortTimeFormat)

        if showAP:
            result = f"{result} {self.getAmPm(dateTime)}"

        return result

    def getLongTime(self,dateTime=None,showAP=False):
        dateTime = dateTime or self.now()
        result = self.formatDateTime(dateTime,self.longTimeFormat)

        if showAP:
            result = f"{result} {self.getAmPm(dateTime)}"

        return result

    def getShortDate(self,dateTime=None):
        dateTime = dateTime or self.now()
        return self.formatDateTime(dateTime,self.shortDateFormat)

    def getLongDate(self,dateTime=None):
        dateTime = dateTime or self.now()
        return self.formatDateTime(dateTime,self.longDateFormat)

    def getDayOfYear(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.timetuple().tm_yday

    def getWeekNumber(self,dateTime=None):
        dateTime = dateTime or self.now()
        return dateTime.isocalendar().week

    def formatDateTime(self,dateTime,formatString):
        tokens = [
            "dddd",
            "MMMM",
            "yyyy",
            "YYYY",
            "hh",
            "HH",
            "dd",
            "mm",
            "ss",
            "yy",
            "MM",
            "dd",
            "d",
            "M",
            "h",
            "H"
        ]

        result = formatString

        replacements = {
            "dddd": self.getDayName(dateTime),
            "MMMM": self.getMonthName(dateTime),
            "yyyy": f"{dateTime.year:04d}",
            "YYYY": f"{dateTime.year:04d}",
            "yy": f"{dateTime.year % 100:02d}",
            "dd": f"{dateTime.day:02d}",
            "d": str(dateTime.day),
            "MM": f"{dateTime.month:02d}",
            "M": str(dateTime.month),
            "hh": f"{dateTime.hour % 12 or 12:02d}",
            "h": str(dateTime.hour % 12 or 12),
            "HH": f"{dateTime.hour:02d}",
            "H": str(dateTime.hour),
            "mm": f"{dateTime.minute:02d}",
            "ss": f"{dateTime.second:02d}"
        }

        for token in tokens:
            result = result.replace(token,replacements[token])

        return result