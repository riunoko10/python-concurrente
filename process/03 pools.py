import os
import time
import logging
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def add(x, y):
    logging.info(f'pid: {os.getpid()}')
    time.sleep(5)
    return x + y

def reduce(x, y):
    logging.info(f'pid: {os.getpid()}')
    time.sleep(5)
    return x - y

def math_operation(number1:int, number2:int, operation):
    time.sleep(5)
    return operation(number1, number2)

def print_result(future):
    logging.info(f'El resultado es {future.result()}')


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        add_future = executor.submit(math_operation, 2, 3, add)
        logging.info(f'El resultado de la suma es {add_future.result()}')

        reduce_future = executor.submit(math_operation, 2, 3, reduce)
        reduce_future.add_done_callback(print_result)