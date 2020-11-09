'''
main

'''

import zoom
import meet
from datetime import datetime
import time
f=open('log.txt','a')
#import csv
'''x = datetime.datetime.now()'''
'''
print(x.hour,x.minute)
print(x.strftime("%A"))'''
print('\n\n\n',datetime.now().strftime('%H:%M:%S %D'),'\t\twaiting for class to start\n')
n=datetime.now().strftime('%H:%M:%S %D')+'\nwaiting for class to start\n'
f.write(n)
f.close()
while True:
    import routine
    t = datetime.now().strftime("%H:%M")
    tim=routine.timings()
    mt=routine.meetids()
    pss=routine.passwords()
    sub=routine.subjects()
    dur=routine.durations()
    if t in tim:
        f=open('log.txt','a')
        print(datetime.now().strftime('%H:%M:%S %D'), 'in timings\n')
        n=datetime.now().strftime('%H:%M:%S %D')+'in timings\n'
        f.write(n)
        dex=tim.index(t)
        meetid=mt[dex]
        password=pss[dex]
        subject=sub[dex]
        duration=dur[dex]
        if meetid=='meet.google.com':
            print(datetime.now().strftime('%H:%M:%S %D'),'')
            n=datetime.now().strftime('%H:%M:%S %D')+'launching google meet'
            f.write(n)
            f.close()
            meet.join(meetid, password, subject, duration)
            
        elif meetid.isdigit():
            print(datetime.now().strftime('%H:%M:%S %D'),'launching zoom')
            n=datetime.now().strftime('%H:%M:%S %D')+'launching zoom'
            f.write(n)
            f.close()
            zoom.join(meetid, password, subject,duration)
