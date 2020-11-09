import os
import getpass
from datetime import datetime
user=getpass.getuser()
f=open('log.txt','a')
n=str('\n'+datetime.now().strftime('%H:%M:%S %D')+'killed zoom.exe\n')
f.write(n)
f.close()
def startzoom():
    os.startfile(rf"C:/Users/{user}/AppData/Roaming/Zoom/bin/Zoom.exe")
    f=open('log.txt','a')
    n=datetime.now().strftime('%H:%M:%S %D')+'started zoom.exe\n'
    f.write(n)
    f.close()
    return ""


def closezoom():
    os.system(r"TASKKILL /F /IM zoom.exe")
    f=open('log.txt','a')
    n=datetime.now().strftime('%H:%M:%S %D')+'killed zoom.exe\n'
    f.write(n)
    f.close()
    return ""
