import pyautogui
import time
import execute
import datetime

def join(meetingid,password,subject,duration):
    execute.startzoom()
    #join a meeting
    execute.startzoom()
    print(datetime.datetime.now(),'launching zoom...')
    time.sleep(2)
    join_btn = pyautogui.locateCenterOnScreen('joinameet.png')
    print(datetime.datetime.now(),'launching...')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print(datetime.datetime.now(), 'joining',subject,'class')

    #enter meeting id
    join_btn = pyautogui.locateCenterOnScreen('enter_id.png')
    pyautogui.moveTo(join_btn)
    print(datetime.datetime.now(),'entering id...')
    pyautogui.write(meetingid)

    #join
    join_btn = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    #meeting password
    join_btn = pyautogui.locateCenterOnScreen('password.png')
    pyautogui.moveTo(join_btn)
    pyautogui.write(password)
    print(datetime.datetime.now(),'entering password...')

    #join meeting
    join_btn = pyautogui.locateCenterOnScreen('join_meeting.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print(datetime.datetime.now(),'entering class.')

    #join audio
    time.sleep(35)
    pyautogui.moveTo(620, 320, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='left', clicks=3)

    #waiting for class to over
    time.sleep(duration)

    #closing zoom
    execute.closezoom()
