from threading import *
from time import sleep

class hi(Thread):
  def run(self):
    for i in range (8):
      print ('Hi')
      sleep(1)

class hello(Thread):
  def run(self):
    for i in range (8):
      print ('Hello')
      sleep(1)

a = hi()
b = hello()

a.start()
sleep(0.2)
b.start()

a.join()
b.join()
print ('bye')