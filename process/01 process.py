import os
import time
import logging
import multiprocessing


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def nuevo_proceso():
    logging.info(f'Proceso hijo con PID: {os.getpid()}')
    time.sleep(2)
    logging.info('Fin del proceso hijo')


def nombre_persona(nombre):
    logging.info(f'Hola {nombre}')

if __name__ == '__main__':
    logging.info(f'Proceso padre con PID: {os.getpid()}')
    p = multiprocessing.Process(target=nuevo_proceso)

    #! se puede usar args o kwargs
    p2 = multiprocessing.Process(
        target=nombre_persona,
        args=('Cristian',) #* Se debe pasar una tupla
    )
        
    p.start()
    p2.start()

    #* permite esperar a que el proceso termine
    p.join()
    p2.join()
    logging.info('Fin del proceso padre')