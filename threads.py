import threading
import time



class Thread:

    def call_one(self):
        print('one')
        self.call_two()

    def call_two(self):
        print('two')
        self.call_one()


a = Thread()
x = threading.Thread(target=a.call_one())
x.start()
