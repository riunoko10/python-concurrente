import time
import logging
import threading
import queue

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def show_elements(queue):
    while not queue.empty():
        element = queue.get()
        logging.info(f"Elemento: {element}")
        queue.task_done()
        time.sleep(1)



if __name__ == '__main__':
    queue = queue.Queue()

    for val in range(10):
        queue.put(val)
    

    logging.info(f"Queue: {queue.queue}")

    for _ in range(3):
        t = threading.Thread(target=show_elements, args=(queue,))
        t.start()

