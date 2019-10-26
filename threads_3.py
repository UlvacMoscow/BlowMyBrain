import threading
import time


def ping(voi):
    while True:
        time.sleep(0.1)
        print('{}'.format(voi))

po = threading.Thread(target=ping, args=['ping'])
pi = threading.Thread(target=ping, args=['pong'])
#
po.start()
pi.start()
