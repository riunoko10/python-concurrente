import time
import threading
import logging



logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
    
    def run(self):
        logging.info("Thread %s: starting", self.name)
        time.sleep(2)
        logging.info("Thread %s: finishing", self.name)


if __name__ == '__main__':
    my_thread = MyThread("MyThread")
    my_thread.start()
