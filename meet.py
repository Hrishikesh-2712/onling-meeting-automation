
''' Google Meet
'''
import webbrowser
import time
from datetime import datetime
import pyautogui
def join(meetid,password,subject,duration):
    f=open('log.txt','a')
    a=rf'https:{meetid}/{password}'
    webbrowser.open(a)
    print(datetime.now().strftime('%H:%M:%S %D'), 'launched browswe')
    n=datetime.now().strftime('%H:%M:%S %D')+'launched browswe\n'
    f.write(n)

    time.sleep(30)
    n=datetime.now().strftime('%H:%M:%S %D')+'sleeping for 25 seconds\n'
    f.write(n)
    #mute mic
    pyautogui.hotkey('ctrl','d')
    print(datetime.now().strftime('%H:%M:%S %D'), 'mic off')
    n=datetime.now().strftime('%H:%M:%S %D')+'mic off\n'
    f.write(n)

    #turn off cam
    pyautogui.hotkey('ctrl','e')
    print(datetime.now().strftime('%H:%M:%S %D'), 'cam off')
    n=datetime.now().strftime('%H:%M:%S %D')+'cam off\n'
    f.write(n)
    
    #click join
    time.sleep(2)
    n=datetime.now().strftime('%H:%M:%S %D')+'sleeping of 2 seconds\n'
    f.write(n)
    # not working join_btn = pyautogui.locateCenterOnScreen('meet_join.png')
    for loop in range (5):
        pyautogui.press('tab')
        n=datetime.now().strftime('%H:%M:%S %D')+'hit tab\n'
        f.write(n)
        time.sleep(0.1)
        n=datetime.now().strftime('%H:%M:%S %D')+'sleeping for 0.1 seconds\n'
        f.write(n)
    pyautogui.press('enter')
    n=datetime.now().strftime('%H:%M:%S %D')+'hit enter\n'
    f.write(n)
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining',subject,'class')
    n=datetime.now().strftime('%H:%M:%S %D')+'joining class\n'
    f.write(n)

    #waiting for class to over
    print(datetime.now().strftime('%H:%M:%S %D'),'waiting for class to over')
    n=datetime.now().strftime('%H:%M:%S %D')+f'going to sleep for {duration} seconds\n'
    f.write(n)
    time.sleep(duration)
    print(datetime.now().strftime('%H:%M:%S %D'),'time over')
    n=datetime.now().strftime('%H:%M:%S %D')+'time over\n'
    f.write(n)

    #hang up
    pyautogui.moveTo(620, 320, 2, pyautogui.easeOutQuad)
    pyautogui.click()
    n=datetime.now().strftime('%H:%M:%S %D')+'mouse clicked at 620, 320\n'
    f.write(n)
    x,y=pyautogui.size()
    n=datetime.now().strftime('%H:%M:%S %D')+'get display resolution\n'
    f.write(n)
    x=x/2
    y=y/1.1294
    pyautogui.moveTo(x,y)
    pyautogui.click()
    n=datetime.now().strftime('%H:%M:%S %D')+f'mouse clicked at {x} {y}\n'
    f.write(n)
    print(datetime.now().strftime('%H:%M:%S %D'),'left class\n\n waiting of next class to start')
    n=datetime.now().strftime('%H:%M:%S %D')+'left class\n\n waiting of next class to start\n'
    f.write(n)
    f.close()
