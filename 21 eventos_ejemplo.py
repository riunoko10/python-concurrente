import time
import logging
import threading
import requests


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

user = dict()


def generate_request(url:str, event:threading.Event):
    global user
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()
        user = response_json.get('results')[0]
        event.set()

def show_user_name(event:threading.Event):
    event.wait()
    name = user.get('name').get('first')
    logging.info(f"El nombre del usuario es: {name}")


if __name__ == '__main__':

    event = threading.Event()

    t_request = threading.Thread(target=generate_request, args=('https://randomuser.me/api/',event))
    t_show_user = threading.Thread(target=show_user_name, args=(event,))

    t_request.start()
    t_show_user.start()

    