import random
import time 
import logging
import threading
import requests

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def get_name(future: Future):
    response = future.result()
    if response.status_code != 200:
        logging.error(f"Error en la petición: {response.status_code}")
        return
    response_json = response.json()
    name = response_json.get("forms")[0].get("name")
    logging.info(f"Nombre del pokemon: {name}")


def generate_request(url):
    future = Future()

    thread = threading.Thread(
        target=(
            lambda: future.set_result(requests.get(url))
        )
    )
    thread.start()

    return future


if __name__ == '__main__':
    random_number = random.randint(1, 100)
    future = generate_request(f'https://pokeapi.co/api/v2/pokemon/{random_number}/')
    future.add_done_callback(get_name)

    while not future.done():
        logging.info('Haciendo otra cosa')
    else:
        logging.info('Terminé')