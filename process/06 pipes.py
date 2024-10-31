import time
import logging
import multiprocessing


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

class Publisher(multiprocessing.Process):
    def __init__(self, pipe):
        self.pipe = pipe
        
        multiprocessing.Process.__init__(self)
        

    def run(self):
        logging.debug('Publisher started')

        for x in range(10):
            self.pipe.send(x)
            time.sleep(1)
        
        self.pipe.send(None)
        self.pipe.close()
        logging.debug('Publisher finished')


class Subscriber(multiprocessing.Process):
    def __init__(self, pipe):
        self.pipe = pipe
        self.is_alive = True
        multiprocessing.Process.__init__(self)
        

    def run(self):
        logging.debug('Subscriber started')

        while self.is_alive:
            result = self.pipe.recv()
            
            self.is_alive = result is not None
            logging.debug(f"Received: {result}")
        else:
            self.pipe.close()
        
        logging.debug('Subscriber finished')



if __name__ == '__main__':

    pipe1, pipe2 = multiprocessing.Pipe()

    publisher = Publisher(pipe1)
    subscriber = Subscriber(pipe2)
    publisher.start()
    subscriber.start()

    publisher.join()
    subscriber.join()
    logging.debug('Publisher finished')