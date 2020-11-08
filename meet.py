
''' Google Meet
'''
import webbrowser
import time
from datetime import datetime
import pyautogui
def join(meetid,password,subject,duration):
    a=rf'https:{meetid}/{password}'
    webbrowser.open(a)
    print(datetime.now(), 'launched browswe')

    time.sleep(20)
    #mute mic
    pyautogui.hotkey('ctrl','d')
    print(datetime.now(), 'mic off')

    #turn off cam
    pyautogui.hotkey('ctrl','e')
    print(datetime.now(), 'cam off')

    #click join
    time.sleep(2)
    # not working join_btn = pyautogui.locateCenterOnScreen('meet_join.png')
    x, y= pyautogui.size()
    a=x/1.32
    a=y/1.75
    pyautogui.moveTo(a,b)
    pyautogui.click()
    print(datetime.now(), 'joining',subject,'class')

    #waiting for class to over
    time.sleep(10)

    #hang up
    pyautogui.moveTo(620, 320, 2, pyautogui.easeOutQuad)
    pyautogui.click()
    join_btn = pyautogui.moveTo(x/2,y)
    pyautogui.moveTo(join_btn)
    pyautogui.click()
