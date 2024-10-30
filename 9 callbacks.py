import logging
import requests
import threading


logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def generate_request(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback(response)


def get_name(response_json:dict):
    name = response_json.get("forms")[0].get("name")
    logging.info(f"Nombre del pokemon: {name}")

def error(response):
    logging.error(f"Error en la petición: {response.status_code}")


def get_name_person(response_json:dict):
    name = response_json.get("results")[0].get("name").get("first")
    logging.info(f"Nombre de la persona: {name}")

if __name__ == "__main__":
    thread1 = threading.Thread(
        target=generate_request,
        kwargs={
            "url": "https://pokeapi.co/api/v2/pokemon/1/",
            "success_callback": get_name,
            "error_callback": error,
        }
    )
    thread1.start()

    thread2 = threading.Thread(
    target=generate_request,
    kwargs={
        "url": "https://randomuser.me/api/",
        "success_callback": get_name_person,
        "error_callback": error,
    }
    )
    thread2.start()