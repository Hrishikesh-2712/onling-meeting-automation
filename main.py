from time import sleep
from datetime import datetime
from selenium import webdriver
import csv, getpass, os, pyautogui, requests
from selenium.webdriver.chrome.options import Options
import mysql.connector

user = getpass.getuser()  # get current user name
folder = ''
date = ''


# gmeet
def joinmeet(password, subject, screenshot):
    print(datetime.now().strftime('%H:%M:%S %D'), 'launched browswe')

    join_meet(password)

    ending(screenshot, row[1], subject)
    home()
    print('qutting')
    print(datetime.now().strftime('%H:%M:%S %D'), 'left class\n\n waiting of next class to start')


def gmail_login(mail_address, password):
    global driver
    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1})

    driver = webdriver.Chrome(options=opt)

    # Login Page 
    driver.get(f'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://meet.google.com')
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(100)

    # input Password
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(100)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(100)
    driver.minimize_window()
    sleep(2)


def join_meet(meetid):
    # turn off Microphone
    global driver
    driver.get(f'https://meet.google.com/{meetid}')
    driver.maximize_window()
    driver.implicitly_wait(900)
    sleep(2)
    driver.find_element_by_css_selector(
        '#yDmH0d > c-wiz > div > div > div:nth-child(9) > div.crqnQb > div > div > div.vgJExf > div > div.KieQAe > '
        'div.ZUpb4c > div.oORaUb.NONs6c > div > div.EhAUAc > div.ZB88ed > div > div > div > span > span > div > '
        'div.IYwVEf.HotEze.uB7U9e.nAZzG > div > svg').click()
    driver.implicitly_wait(600)

    # turn off camera 
    sleep(1)
    driver.find_element_by_css_selector(
        '#yDmH0d > c-wiz > div > div > div:nth-child(9) > div.crqnQb > div > div > div.vgJExf > div > div.KieQAe > '
        'div.ZUpb4c > div.oORaUb.NONs6c > div > div.EhAUAc > div.GOH7Zb > div > div > span > span > div > div > '
        'svg').click()
    driver.implicitly_wait(600)

    # Join meet
    sleep(5)
    driver.implicitly_wait(600)
    driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    pyautogui.press('f11')


def home():
    global driver
    driver.get('https://meet.google.com')
    driver.implicitly_wait(60)
    sleep(1)
    pyautogui.press('f11')
    sleep(1)
    driver.minimize_window()


def launch_zoom():
    try:
        os.startfile(rf"C:/Users/{user}/AppData/Roaming/Zoom/bin/Zoom.exe")
    except FileNotFoundError:
        print('zoom software is not installed, please wait till installation')
        print('Download Starting...')

        url = 'https://www.zoom.us/client/latest/ZoomInstaller.exe'
        r = requests.get(url)
        filename = url.split('/')[-1]
        with open(filename, 'wb') as output_file:
            output_file.write(r.content)
        print('Download Completed!!!')
        os.startfile(os.getcwd() + '\\' + '\\' + filename)
        sleep(15)
        os.startfile(rf"C:/Users/{user}/AppData/Roaming/Zoom/bin/Zoom.exe")


# zoom
def joinzoom(end_time, meetingid, password, subject, screenshot='y'):
    # start zoom
    os.system(r"TASKKILL /F /IM zoom.exe")  # if previous class was running it would be closed

    launch_zoom()

    print('starting')
    # join a meeting
    sleep(12)
    pyautogui.press('tab')
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'joining', subject, 'class')

    # enter meeting id
    sleep(6)
    print(datetime.now().strftime('%H:%M:%S %D'), 'entering id...')
    pyautogui.write(meetingid)

    # join
    pyautogui.press('enter')
    sleep(6)

    # meeting password
    pyautogui.write(password)
    print(datetime.now().strftime('%H:%M:%S %D'), 'entering password...')

    # join meeting
    pyautogui.press('enter')
    print(datetime.now().strftime('%H:%M:%S %D'), 'entering class.')

    # join audio
    sleep(15)
    x, y = pyautogui.size()
    x = x / 2.2
    y = y / 2.4
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left', clicks=3)

    ending(screenshot, end_time, subject)

    print(datetime.now().strftime('%H:%M:%S %D'), 'time over')

    # closing zoom
    os.popen("TASKKILL /F /IM zoom.exe")
    print(datetime.now().strftime('%H:%M:%S %D'), 'left class\n\n waiting of next class to start')


def ending(screenshot, end_time, sub):
    h = int(end_time[:2])
    m = int(end_time[3:5])
    if screenshot == 'n':  # sleeping till class gets over
        print('waiting for class to over')
        print('end time', end_time)
        t = (h * 3600) + (m * 60)
        ch = int(datetime.now().strftime('%H'))
        cm = int(datetime.now().strftime('%M'))
        s = int(datetime.now().strftime('%S'))
        ct = (ch * 3600) + (cm * 60) + s
        e = abs(t - ct)
        print('calculated', e, 's')
        sleep(e)
        print('out')
    else:
        shots(screenshot, h, m, sub)


# taking screenshots
def shots(s, h, m, sub):
    check(sub)  # creating folders
    global folder
    print('taking screenshots')
    while h > int(datetime.now().strftime('%H')) or h == int(datetime.now().strftime('%H')) and m > int(
            datetime.now().strftime('%M')):
        now = datetime.now().strftime('%H %M %S %d %M %Y')
        pyautogui.screenshot().save(f'C://Users//{user}//Pictures//Screenshots//{sub}//{folder}//{now}.png')
        print(now, 'took a screenshot')
        sleep(s)

    print(f'Screenshots for this class was saved in the following directory ->\n C://Users//{user}//Pictures'
          f'//Screenshots//{sub}//{date} \n')


# creating folder
def check(sub):
    sub = row[4]
    global date
    global folder
    base_dir = f'C://Users//{user}//Pictures//'
    if os.path.isdir(base_dir):
        print('good going')
        if os.path.isdir(base_dir + r'Screenshots//'):
            print('keep up')
            if os.path.isdir(base_dir + f'Screenshots//{sub}//'):
                print('alright')
                now = datetime.now().strftime('%H %M %d %M %Y')
                if os.path.isdir(base_dir + f'Screenshots//{sub}//{now}//'):
                    print('check passed')
                    folder = now
                    return True
                else:
                    now = datetime.now().strftime('%H %M %d %M %Y')
                    os.mkdir(base_dir + f'Screenshots//{sub}//{now}')
                    check(sub)
            else:
                os.mkdir(base_dir + f'Screenshots//{sub}//')
                check(sub)
        else:
            os.mkdir(base_dir + 'Screenshots//')
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


print('loading...')


def mpass():
    global ps
    os.popen('attrib -h .t')
    if os.path.exists(r'.t'):
        with open('.t', 'r') as f:
            c = f.read()
            if len(c) < 4:
                with open('.t', 'w') as fg:
                    ps = pyautogui.password('please enter mysql password')
                    fg.write(ps)
            else:
                ps = c
                print(ps)
    else:
        with open('.t', 'w') as f:
            ps = pyautogui.password('please enter mysql password')
            f.write(ps)

    os.popen('attrib +h .t')


gpass = ''
gid = ''


def database():
    global gpass
    global gid
    db = mysql.connector.connect(host="localhost", user="root", passwd=ps)
    cur = db.cursor()
    cur.execute('SHOW DATABASES;')
    d = cur.fetchall()
    print(d)
    if ('creed',) in d:
        cur.execute('USE creed;')
        cur.execute('SELECT * FROM c;')
        d = cur.fetchall()[0]
        print(d, type(d), '\n\n\n')
        print(d[0] + '\n' + d[1] + '\n\n')
        gid = d[0]
        gpass = d[1]

    else:
        gid = pyautogui.prompt('please enter gmail address')
        gpass = pyautogui.password('please enter gmail password')
        i = gid
        p = gpass
        print(i, p)
        cur.execute('CREATE DATABASE creed;')
        cur.execute('USE creed;')
        cur.execute('CREATE TABLE c(i varchar(200) not null, p varchar(200) not null);')
        cur.execute("INSERT INTO c VALUES('{}','{}');".format(gid, gpass))
        db.commit()

    print(gid, gpass)


mpass()
database()

gmail_login(gid, gpass)
print('loaded')
os.system('cls')
print(datetime.now().strftime('%H:%M:%S %D'), 'reading routine file for upcoming class')

# starter
while True:
    with open('routine.csv', 'r') as f:
        c = csv.reader(f)
        for row in c:
            now = datetime.now().strftime('%H:%M')
            if row[0] == now:
                print(now, 'in timings')
                if row[2] == 'meet.google.com':
                    joinmeet(row[3], row[4], se(row[5]))
                elif row[2].isdigit:
                    joinzoom(row[1], row[2], row[3], row[4], se(row[5]))
                else:
                    print('Please correct routine info data')
        f.close()
        sleep(2)
