import threading
import time


def ping():
    time.sleep(1)
    print('ping')
    return 1

    # while True:
        # print('ping')

def pong():
    print('pong')
    return 1

    # while True:
    # time.sleep(1)
        # print('pong')


# po = threading.Thread(target=ping)
# pi = threading.Thread(target=pong)
#
# po.start()
# pi.start()

def run():
    while True:
        ping()
        # time.sleep(2)
        pong()


t = threading.Thread(target=run)
t.start()
# run()
# ping()
# pong()
#
