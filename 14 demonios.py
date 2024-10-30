import time 
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def daemon_thread():
    while True:
        logging.debug('Daemon thread ejecutándose')
        time.sleep(1)
    

if __name__ == '__main__':
    thread = threading.Thread(target=daemon_thread, daemon=True)
    thread.start()

    input('Presiona enter para salir\n')
    

#* Un demonio es un thread que se ejecuta en segundo plano, y no impide que el programa termine