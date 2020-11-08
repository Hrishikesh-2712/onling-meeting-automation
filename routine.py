#f=with(open('routine.csv','r'))
from datetime import datetime
a=datetime.now().strftime('%H:%M')
def timings():
    return ('08:00','09:00','09:53','09:40','11:41',a)

def meetids():
    return ('73263794809','73955949894','7462732282','5487512685','meet.google.com','meet.google.com')

def passwords():
    return ('Organic','3z70kv','dks654','dhdr66','nwj-tusp-sir','fxd-vffe-xuw')

def subjects():
    return ('Chemistry Tuition','Chemistry School','Physics','Maths','Computer','Trail')


def durations():
    return (2400,2400,2400,2400,2400,2400)
