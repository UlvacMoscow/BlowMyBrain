import threading
import time



def sleep(n, name):
    print('sleep thread {}'.format(name))
    time.sleep(n)
    print('aaayyyyyyy')

t = threading.Thread(target=sleep, name='Thread1', args=(5, 'Thread1'))

t.start()

print('thread main')
