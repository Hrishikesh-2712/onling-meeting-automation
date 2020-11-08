import os
import getpass
user=getpass.getuser()

def startzoom():
    os.startfile(rf"C:/Users/{user}/AppData/Roaming/Zoom/bin/Zoom.exe")
    return ""


def closezoom():
    os.system(r"TASKKILL /F /IM zoom.exe")
    return ""
