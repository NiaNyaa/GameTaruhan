import random
import os
import sys
import time

class show():
  def money(self):
    file = open('money.txt','r')
    read1 = file.read()
    print(read1)
    file.close()

# Name Class
show = show()

show.money()
