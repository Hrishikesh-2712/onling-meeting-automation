
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

    time.sleep(25)
    #mute mic
    pyautogui.hotkey('ctrl','d')
    print(datetime.now(), 'mic off')

    #turn off cam
    pyautogui.hotkey('ctrl','e')
    print(datetime.now(), 'cam off')

    #click join
    time.sleep(2)
    # not working join_btn = pyautogui.locateCenterOnScreen('meet_join.png')
    for loop in range (5):
        pyautogui.press('tab')
        time.sleep(1)
    pyautogui.press('enter')
    print(datetime.now(), 'joining',subject,'class')

    #waiting for class to over
    time.sleep(10)

    #hang up
    pyautogui.moveTo(620, 320, 2, pyautogui.easeOutQuad)
    pyautogui.click()
    x,y=pyautogui.size()
    x=x/2
    y=y/1.1294
    pyautogui.moveTo(x,y)
    pyautogui.click()
    print(datetime.now(),'left class\n\n waiting of next class to start')
