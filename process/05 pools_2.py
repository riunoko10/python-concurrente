import time
import logging


from multiprocessing import Pool


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def is_even(number:int):
    return number % 2 == 0, number


def show_result(results):
    for result, number in results:
        logging.info(f'El numero {number} es par? {result}')


if __name__ == '__main__':

    with Pool(processes=2) as pool:

        result = pool.apply(is_even, (2,))
        logging.info(f'El numero 2 es par? {result}')

        #* map recibe una funcion y un iterable, y retorna una lista con los resultados de la funcion
        numbers = [i for i in range(1, 11)]

        #* map_async retorna un objeto de tipo mapresult, el cual tiene el metodo get() para obtener los resultados
        map_result = pool.map_async(is_even, numbers, callback=show_result)

        logging.info('Esperando a que termine el proceso')

        logging.info('Haciendo otras cosas......')

        map_result.wait() #* Espera a que termine el proceso map_async

        logging.info('Fin del programa')