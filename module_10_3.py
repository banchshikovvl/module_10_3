import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()
        for transaction in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rand = randint(0, 500)
            self.balance += rand
            print(f'Пополнение:\t{rand}$, \tтекущий баланс: {self.balance}$ ')
            sleep(0.01)

    def take(self):
        for transaction in range(100):
            rand = randint(0, 500)
            print(f'Запрос на: \t{rand}$ ')
            if self.balance >= rand:
                self.balance -= rand
                print(f'Снятие: \t{rand}$, \tтекущий баланс: {self.balance}$ ')
                sleep(0.01)
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.01)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
