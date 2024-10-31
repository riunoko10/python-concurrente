import os
import time
import logging
import multiprocessing


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def nuevo_proceso():
    logging.info(f'Proceso hijo con PID: {os.getpid()}')
    time.sleep(20)
    logging.info('Fin del proceso hijo')




if __name__ == '__main__':
    logging.info(f'Proceso padre con PID: {os.getpid()}')
    p = multiprocessing.Process(target=nuevo_proceso)
    p.start()

    time.sleep(5)

    #* Verificar si el proceso hijo sigue vivo
    if p.is_alive():
        logging.info('El proceso hijo sigue vivo')
        p.terminate()
        logging.info('El proceso hijo ha sido terminado antes de tiempo')

    logging.info('Fin del programa')