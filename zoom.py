import pyautogui
import time
import execute
from datetime import datetime

def join(meetingid,password,subject,duration):
    execute.startzoom()
    #join a meeting
    execute.startzoom()
    print(datetime.now(),'launching zoom...')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    print(datetime.now(), 'joining',subject,'class')

    #enter meeting id
    time.sleep(5)
    print(datetime.now(),'entering id...')
    pyautogui.write(meetingid)

    #join
    pyautogui.press('enter')
    time.sleep(5)

    #meeting password
    pyautogui.write(password)
    print(datetime.now(),'entering password...')

    #join meeting
    pyautogui.press('enter')
    print(datetime.now(),'entering class.')

    #join audio
    time.sleep(30)
    x,y=pyautogui.size()
    x=x/2.2
    y=y/2.4
    pyautogui.moveTo(x,y)
    pyautogui.click(button='left', clicks=3)

    #waiting for class to over
    time.sleep(duration)

    #closing zoom
    execute.closezoom()
    print(datetime.now(),'left class\n\n waiting of next class to start')
