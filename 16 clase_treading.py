import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def nueva_tarea():
    current_thread = threading.current_thread()
    name = current_thread.name
    id = current_thread.ident
    logging.info(f'El hilo {name} ha comenzado')
    logging.info(f'El id del hilo es {id}')


if __name__ == '__main__':
    thread = threading.Thread(target=nueva_tarea, name='mi-hilo')
    thread.start()

    # logging.info('los hilos vivos son {}'.format(threading.enumerate()))
    for thread in threading.enumerate():
        if thread == threading.main_thread():
            logging.info('Hilo principal')

        logging.info(thread)