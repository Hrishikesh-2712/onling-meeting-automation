import os


def startzoom():
    os.startfile(r"C:/Users/Administrator/AppData/Roaming/Zoom/bin/Zoom.exe")
    return ""


def closezoom():
    os.system(r"TASKKILL /F /IM zoom.exe")
    return ""
