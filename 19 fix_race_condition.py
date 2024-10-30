import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


BALANCE = 0

lock = threading.RLock()

def deposit(value):
    global BALANCE
    logging.debug('Depositing %s', value)
    #! usando lock para evitar race condition
    with lock:
        BALANCE += value #* seccion critica
    logging.debug('Balance is %s', BALANCE)

def withdraw(value):
    global BALANCE
    logging.debug('Withdrawing %s', value)
    #! usando lock para evitar race condition
    lock.acquire()
    BALANCE -= value #* seccion critica
    lock.release()
    logging.debug('Balance is %s', BALANCE)


if __name__ == '__main__':
    for _ in range(0, 10):
        t_deposit = threading.Thread(target=deposit, args=(1,))
        t_withdraw = threading.Thread(target=withdraw, args=(1,))

        t_deposit.start()
        t_withdraw.start()

        t_deposit.join()
        t_withdraw.join()

    logging.debug('Final balance is %s', BALANCE)