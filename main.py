'''
main

'''

import zoom
import meet
from datetime import datetime
import time
#import csv
'''x = datetime.datetime.now()'''
'''
print(x.hour,x.minute)
print(x.strftime("%A"))'''
while True:
    import routine
    t = datetime.now().strftime("%H:%M")
    tim=routine.timings()
    mt=routine.meetids()
    pss=routine.passwords()
    sub=routine.subjects()
    dur=routine.durations()
    if t in tim:
        print(datetime.now(), 'in timings')
        dex=tim.index(t)
        meetid=mt[dex]
        password=pss[dex]
        subject=sub[dex]
        duration=dur[dex]
        if meetid=='meet.google.com':
            print('launching google meet')
            meet.join(meetid, password, subject,duration)
        else:
            zoom.join(meetid, password, subject,duration)
