import time
import logging
import threading

from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def math_operation(number1:int, number2:int):
    time.sleep(2)

    result = number1 + number2
    logging.info(f'The result is {result}')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='test-thread') as executor:
        executor.submit(math_operation, 2, 3)
        executor.submit(math_operation, 3, 4)
        executor.submit(math_operation, 4, 5)
        executor.submit(math_operation, 5, 6)
        executor.shutdown(wait=True)