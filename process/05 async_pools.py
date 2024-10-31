import time
import logging


from multiprocessing import Pool


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def is_even(number:int):
    time.sleep(5)
    return number % 2 == 0, number



if __name__ == '__main__':

    with Pool(processes=2) as pool:

        result = pool.apply_async(is_even, (2,))

        logging.info('Esperando a que termine el proceso')

        result.wait(timeout=5)

        logging.info('Proceso terminado')

        logging.info(f'El numero 2 es par? {result.get()}')

        logging.info('Proceso terminado')