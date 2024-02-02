from threading import *
from time import sleep

class Thread1(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hello")


class Thread2(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hi")      


t1 = Thread1()
t2 = Thread2()

t1.start()
t2.start()