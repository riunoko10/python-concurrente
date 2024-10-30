import time 
import logging
import threading

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

"""
Este módulo demuestra el uso de futuros en Python para la programación concurrente.
Los futuros en Python son objetos que representan una operación que puede completarse en el futuro. 
Son utilizados principalmente en programación concurrente para manejar tareas asincrónicas. 
Un futuro puede estar en uno de los siguientes estados: pendiente, completado o cancelado. 
Permiten verificar si una tarea ha sido completada, obtener su resultado o manejar excepciones que 
puedan haber ocurrido durante su ejecución.
"""

def callback_futuro(futuro):
    logging.info('Futuro completado: %s', futuro.result())

if __name__ == '__main__':

    future = Future()


    future.add_done_callback(callback_futuro)


    time.sleep(2)

    logging.info('Estableciendo resultado del futuro')
    
    future.set_result('Hola desde el futuro')

"""
Funcionamiento:
1. Se crea un objeto Future.
2. Se añade un callback al futuro.
3. Se espera un tiempo de 2 segundos.
si el futuro se completa, se ejecuta el callback.
"""