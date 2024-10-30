import time
import requests
from concurrent.futures import ThreadPoolExecutor
import logging


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


URLS = [
    'https://codigofacilito.com/',
    'https://twitter.com/home',
    'https://www.google.com/',
    'https://es.stackoverflow.com/',
    'https://stackoverflow.com/',
    'https://about.gitlab.com/',
    'https://github.com/',
    'https://www.youtube.com/'
]

def generate_request(url:str):
    return requests.get(url)

def check_status_code(futuro):
    logging.info(f'El status code es {futuro.result().status_code}')


def math_operation(number1:int, number2:int):
    time.sleep(5)
    return number1 + number2

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        #* el metodo submit retorna un objeto futuro
        futures = [executor.submit(generate_request, url) for url in URLS]
        for future in futures:
            future.add_done_callback(check_status_code)

        math_future = executor.submit(math_operation, 2, 3)
        logging.info(f'El resultado de la suma es {math_future.result()}')