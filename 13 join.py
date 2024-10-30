import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def conexion_base_datos():
    logging.debug('Conectando a la base de datos')
    time.sleep(2)
    logging.debug('Conectado a la base de datos')


def consulta_servidor_web():
    logging.debug('Consultando el servidor web')
    time.sleep(6)
    logging.debug('Consulta realizada')


if __name__ == '__main__':
    t1 = threading.Thread(target=conexion_base_datos)
    t2 = threading.Thread(target=consulta_servidor_web)

    t1.start()
    t2.start()

    #* Esperamos a que los threads terminen
    t1.join()
    t2.join()

    #* En este caso, el programa no terminará hasta que los threads t1 y t2 hayan terminado

    logging.debug('Final del programa, los threads han finalizado')