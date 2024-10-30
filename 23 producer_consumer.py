import time
import queue
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

"""
El problema del productor-consumidor es un clásico problema de sincronización en la programación concurrente. Se trata de coordinar dos tipos de procesos: productores y consumidores, que comparten un recurso común, típicamente una cola o buffer.

Descripción del Problema
Productores: Generan datos y los colocan en el buffer.
Consumidores: Toman datos del buffer y los procesan.
Reglas y Restricciones
Buffer Limitado: El buffer tiene una capacidad limitada. Si está lleno, los productores deben esperar hasta que haya espacio disponible.
Buffer Vacío: Si el buffer está vacío, los consumidores deben esperar hasta que haya datos disponibles.
Sincronización: Se necesita asegurar que los productores y consumidores no accedan al buffer de manera concurrente, lo que podría causar condiciones de carrera.
"""

queue = queue.Queue(10)

def producer():
    while True:
        if not queue.full():
            item = random.randint(1, 10)
            queue.put(item)
            logging.debug(f'Produced {item}')
            time.sleep(1)

def consumer():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            logging.debug(f'Consumed {item}')
            time.sleep(1)


if __name__ == '__main__':

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    