import random
import os
import sys
import time

class show():
  def money(self):
    file = open('money.txt','r')
    global uangk
    uangk = file.read()
    print(uangk)
    file.close()

# Name Class
show = show()

print("Game Taruhan By Ikhsan")
print()
print("Uangmu:",uangk)
