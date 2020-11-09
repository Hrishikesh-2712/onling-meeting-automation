import pyautogui
import time
import execute
from datetime import datetime

def join(meetingid,password,subject,duration):
    f=open('log.txt','a')
    #join a meeting
    execute.startzoom()
    n=datetime.now().strftime('%H:%M:%S %D')+'launched zoom\n'
    f.write(n)
    time.sleep(6)
    pyautogui.press('tab')
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining',subject,'class')
    n=datetime.now().strftime('%H:%M:%S %D')+'joining'+subject+'class\n'
    f.write(n)
    

    #enter meeting id
    time.sleep(6)
    print(datetime.now().strftime('%H:%M:%S %D'),'entering id...')
    n=datetime.now().strftime('%H:%M:%S %D')+'entering id...\n'
    f.write(n)
    pyautogui.write(meetingid)

    #join
    pyautogui.press('enter')
    time.sleep(6)

    #meeting password
    pyautogui.write(password)
    print(datetime.now().strftime('%H:%M:%S %D'),'entering password...')
    n=datetime.now().strftime('%H:%M:%S %D')+'entering password...\n'
    f.write(n)

    #join meeting
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'),'entering class.')
    n=datetime.now().strftime('%H:%M:%S %D')+'entering class.\n'
    f.write(n)

    #join audio
    time.sleep(30)
    x,y=pyautogui.size()
    x=x/2.2
    y=y/2.4
    pyautogui.moveTo(x,y)
    pyautogui.click(button='left', clicks=3)
    n=datetime.now().strftime('%H:%M:%S %D')+'joined audio\n'
    f.write(n)

    #waiting for class to over
    n=datetime.now().strftime('%H:%M:%S %D')+f'going to sleep for {duration} seconds\n'
    f.write(n)
    time.sleep(duration)
    print(datetime.now().strftime('%H:%M:%S %D'),'time over')
    n=datetime.now().strftime('%H:%M:%S %D')+'time over\n'
    f.write(n)

    #closing zoom
    execute.closezoom()
    n=datetime.now().strftime('%H:%M:%S %D')+'left class\n\n waiting of next class to start\n'
    f.write(n)
    f.close()
    print(datetime.now().strftime('%H:%M:%S %D'),'left class\n\n waiting of next class to start')
