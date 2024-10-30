import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def thread1():
    logging.info('Thread 1 iniciado')
    event.wait()
    logging.info('Thread 1 finalizado')


def thread2():
    while not event.is_set():
        logging.info('Thread 2 esperando')
        time.sleep(1)


if __name__ == '__main__':

    event = threading.Event()
    

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()

    logging.info('Esperando 5 segundos')
    time.sleep(5)

    logging.info('Notificando a los threads')
    event.set()
