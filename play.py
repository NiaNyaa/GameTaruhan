# Created By Ikhsan
import random
import os
import sys
import time

# Show
class show():
  def money(self):
    file = open('money.txt','r')
    uangk = file.read()
    print(uangk)
    file.close()

# Name Class
show = show()

os.system("clear")
print("Game Taruhan By Ikhsan")
print()
print("Uangmu:"), "Rp. " + show.money()
