from datetime import datetime
from time import sleep
import os, getpass, csv, webbrowser, pyautogui

user=getpass.getuser()          # get current user name
folder='' 
date=''
#gmeet
def joinmeet(end_time,meetid,password,subject,screenshot):
    a=rf'https:{meetid}/{password}'
    webbrowser.open(a)
    print(datetime.now().strftime('%H:%M:%S %D'), 'launched browswe')

    sleep(20)

    #mute mic
    pyautogui.hotkey('ctrl','d')
    print(datetime.now().strftime('%H:%M:%S %D'), 'mic off')
    sleep(1)

    #turn off cam
    pyautogui.hotkey('ctrl','e')
    print(datetime.now().strftime('%H:%M:%S %D'), 'cam off')
    
    #join
    sleep(2)
    
    x,y=pyautogui.size()
    x/=2
    y/=2
    '''pyautogui.click(x,y)'''
    for loop in range (6):
        pyautogui.press('tab')
        sleep(0.3)
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining',subject,'class')

    #fullscreen entered
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=2)
    
    ending(screenshot,row[1],subject)
    print('qutting')

    #left full screen
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=2)
    
    #for hang up either use

    ''' this'''
    x,y=pyautogui.size()
    x/=2
    y1=y/1.129411764705882
    y/=2
    pyautogui.moveTo(x, y+100, 2, pyautogui.easeOutQuad)
    pyautogui.moveTo(x,y1)
    sleep(2)
    pyautogui.click()
    sleep(2)

    '''

    #or         it's not performing well
         
    #left full screen
    pyautogui.moveTo(x,y)
    pyautogui.click(clicks=2)
    sleep(2)
    for loop in range (7):            #this one to hang up
        pyautogui.press('tab')
        sleep(0.3)
    pyautogui.press('enter')   in the next release I'll use selenuim stay tuned ;)'''
    pyautogui.hotkey('alt','tab')
    print(datetime.now().strftime('%H:%M:%S %D'),'left class\n\n waiting of next class to start')

    
#zoom
def joinzoom(end_time,meetingid,password,subject,screenshot='y'):
    #start zoom
    os.system(r"TASKKILL /F /IM zoom.exe") # if previous class was running it would be closed
    os.startfile(rf"C:/Users/{user}/AppData/Roaming/Zoom/bin/Zoom.exe")    
    
    #join a meeting
    sleep(12)
    pyautogui.press('tab')
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining',subject,'class')
    

    #enter meeting id
    sleep(6)
    print(datetime.now().strftime('%H:%M:%S %D'),'entering id...')
    pyautogui.write(meetingid)

    #join
    pyautogui.press('enter')
    sleep(6)

    #meeting password
    pyautogui.write(password)
    print(datetime.now().strftime('%H:%M:%S %D'),'entering password...')

    #join meeting
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'),'entering class.')

    #join audio
    sleep(15)
    x,y=pyautogui.size()
    x=x/2.2
    y=y/2.4
    pyautogui.moveTo(x,y)
    pyautogui.click(button='left', clicks=3)


    ending(screenshot,end_time,subject)

    print(datetime.now().strftime('%H:%M:%S %D'),'time over')

    #closing zoom
    os.system(r"TASKKILL /F /IM zoom.exe")
    print(datetime.now().strftime('%H:%M:%S %D'),'left class\n\n waiting of next class to start')


def ending(screenshot,end_time,sub):
    h=int(end_time[:2])
    m=int(end_time[3:5])
    if screenshot=='n': # sleeping till class gets over
        print('waiting for class to over')
        print('end time',end_time)
        t=(h*3600)+(m*60)
        ch=int(datetime.now().strftime('%H'))
        cm=int(datetime.now().strftime('%M'))
        s=int(datetime.now().strftime('%S'))
        ct=(ch*3600)+(cm*60)+s
        e=t-ct
        print('calculated',e,'s')
        sleep(e)
        print('out')
    else:
        shots(screenshot,h,m,sub)


#taking screenshots
def shots(s,h,m,sub):
    check(sub) #creating folders
    global folder
    print('taking screenshots')
    while h >=int(datetime.now().strftime('%H')) and m >int(datetime.now().strftime('%M')):
        now=datetime.now().strftime('%H %M %S %d %M %Y')
        pyautogui.screenshot().save(f'C://Users//{user}//Pictures//Screenshots//{sub}//{folder}//{now}.png')
        print(now,'took a screenshot')
        sleep(s)
        
    print(f'Screenshots for this class was saved in the following directory ->\n C://Users//{user}//Pictures//Screenshots//{sub}//{date} \n')

#creating folder
def check(sub):
    sub=row[4]
    global date
    global folder
    base_dir=f'C://Users//{user}//Pictures//'
    if os.path.isdir(base_dir):
        print('good going')
        if os.path.isdir(base_dir+r'Screenshots//'):
            print('keep up')
            if os.path.isdir(base_dir+f'Screenshots//{sub}//'):
                print('alright')
                now=datetime.now().strftime('%H %M %d %M %Y')
                if os.path.isdir(base_dir+f'Screenshots//{sub}//{now}//'):
                    print('check passed')
                    folder=now
                    return True
                else:
                    now=datetime.now().strftime('%H %M %d %M %Y')
                    os.mkdir(base_dir+f'Screenshots//{sub}//{now}')
                    check(sub)
            else:
                os.mkdir(base_dir+f'Screenshots//{sub}//')
                check(sub)
        else:
            os.mkdir(base_dir+'Screenshots//')
            check(sub)
    else:
        os.mkdir(base_dir)
        check(sub)
        

'''screenshots
    check()
    intervel=5
    hour=10
    minute=48-1
    shots(intervel,hour,minute)
'''
def se(a):
    if 'y' in a:
        return 10
    elif 'n' in a:
        return 'n'
    elif a.isdigit():
        return int(a)
    else:
        return 10
    

print(datetime.now().strftime('%H:%M:%S %D'),'reading routine file for upcoming class')


# starter
while True:
    with open('routine.csv','r') as f:
        c=csv.reader(f)
        for row in c:
            now=datetime.now().strftime('%H:%M')
            if row[0] == now:
                print(now,'in timings')
                if row[2]=='meet.google.com':
                    joinmeet(row[1],row[2],row[3],row[4],se(row[5]))
                elif row[2].isdigit:
                    joinzoom(row[1],row[2],row[3],row[4],se(row[5]))
                else :
                    print('Please correct routine info data')
        ''' print(row[4],type(row),type(row[4])) '''
        f.close()
        sleep(2)
