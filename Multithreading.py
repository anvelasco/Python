#Basics (no multithread)

"""class Example:
    def run(self):
        for i in range(5):
            print("Hello from Example")

class ExampleTwo:
    def run(self):
        for i in range(5):
            print("Hello from ExampleTwo")

example = Example()
exampleTwo = ExampleTwo()
example.run()
exampleTwo.run()"""

#Basics with multithreading

from threading import*
import threading
from time import sleep

lock = threading.Lock()

class Example(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print('Lock acquired')
            print("Hello from Example")
            sleep(1)
            lock.release()

class ExampleTwo(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print('Lock acquired')
            print("Hello from ExampleTwo")
            sleep(1)
            lock.release()

example = Example()
exampleTwo = ExampleTwo()
example.start()
sleep(0.1)
exampleTwo.start()
#To make sure that the rest of main gets executed
"""example.join()
exampleTwo.join()
print("End of program")"""