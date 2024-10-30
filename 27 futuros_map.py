import time
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
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

def check_status_code(response):
    logging.info(f'El status code es {response.status_code}')


def math_operation(number1:int, number2:int):
    time.sleep(5)
    return number1 + number2

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        #* el metodo map retorna la respuesta de la funcion generate_request
        for response in executor.map(generate_request, URLS):
            check_status_code(response)

        math_future = executor.submit(math_operation, 2, 3)
        logging.info(f'El resultado de la suma es {math_future.result()}')