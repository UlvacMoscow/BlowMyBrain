import threading
import time


def sleep(n, name):
    print('sleep thread {}'.format(name))
    time.sleep(n)
    print('aaayyyyyyy')

start = time.time()
threading_list = []

for i in range(3):
    t = threading.Thread(target=sleep, name='Thread {}'.format(i), args=(3, 'thread {}'.format(i)))
    threading_list.append(t)
    t.start()
    print('start {}'.format(t.name))


for t in threading_list:
    t.join()

end = time.time()


print('finish of time {}'.format(end - start))
