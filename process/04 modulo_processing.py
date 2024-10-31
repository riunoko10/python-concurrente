import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    pid = current_process.pid

    logging.info(f'pid: {pid} proceso actual')
    logging.info(f'Nombre: {current_process.name} proceso actual')
