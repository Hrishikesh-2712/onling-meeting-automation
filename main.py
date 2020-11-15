from datetime import datetime
import time, os, getpass, csv, webbrowser, pyautogui



#gmeet
def joinmeet(meetid,password,subject,duration):
    a=rf'https:{meetid}/{password}'
    webbrowser.open(a)
    print(datetime.now().strftime('%H:%M:%S %D'), 'launched browswe')

    time.sleep(30)
    
    #mute mic
    pyautogui.hotkey('ctrl','d')
    print(datetime.now().strftime('%H:%M:%S %D'), 'mic off')

    #turn off cam
    pyautogui.hotkey('ctrl','e')
    print(datetime.now().strftime('%H:%M:%S %D'), 'cam off')
    
    #click join
    time.sleep(2)
    for loop in range (6):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining',subject,'class')

    #waiting for class to over
    print(datetime.now().strftime('%H:%M:%S %D'),'waiting for class to over')
    time.sleep(duration)
    print(datetime.now().strftime('%H:%M:%S %D'),'time over')
    
    #hang up
    pyautogui.moveTo(620, 320, 2, pyautogui.easeOutQuad)
    pyautogui.click()
    x,y=pyautogui.size()
    x=x/2
    y=y/1.1294
    pyautogui.moveTo(x,y)
    pyautogui.click()
    pyautogui.hotkey('alt','tab')
    print(datetime.now().strftime('%H:%M:%S %D'),'left class\n\n waiting of next class to start')






#zoom
def joinzoom(meetingid,password,subject,duration):
    #start zoom
    os.system(r"TASKKILL /F /IM zoom.exe") # if previous class was running it would be closed
    user=getpass.getuser()          # get current user name
    os.startfile(rf"C:/Users/{user}/AppData/Roaming/Zoom/bin/Zoom.exe")    
    
    #join a meeting
    time.sleep(6)
    pyautogui.press('tab')
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining',subject,'class')
    

    #enter meeting id
    time.sleep(6)
    print(datetime.now().strftime('%H:%M:%S %D'),'entering id...')
    pyautogui.write(meetingid)

    #join
    pyautogui.press('enter')
    time.sleep(6)

    #meeting password
    pyautogui.write(password)
    print(datetime.now().strftime('%H:%M:%S %D'),'entering password...')

    #join meeting
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'),'entering class.')

    #join audio
    time.sleep(30)
    x,y=pyautogui.size()
    x=x/2.2
    y=y/2.4
    pyautogui.moveTo(x,y)
    pyautogui.click(button='left', clicks=3)


    #waiting for class to over
    time.sleep(duration)
    print(datetime.now().strftime('%H:%M:%S %D'),'time over')

    #closing zoom
    os.system(r"TASKKILL /F /IM zoom.exe")
    print(datetime.now().strftime('%H:%M:%S %D'),'left class\n\n waiting of next class to start')









while True:
    with open('routine.csv','r') as f:
        cs=csv.reader(f)
        for row in cs:
            now=datetime.now().strftime('%H:%M')
            if row[0] == now:
                print(now,'in timings')
                if row[1]=='meet.google.com':
                    joinmeet(row[1],row[2],row[3],int(row[4]))
                elif row[1].isdigit:
                    joinzoom(row[1],row[2],row[3],int(row[4]))
                else :
                    print('Please correct routine info data')
        ''' print(row[4],type(row),type(row[4])) '''

        f.close()
        time.sleep(10)
