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
    print("Uangmu: ",uangk)
    file.close()

# Name Class
show = show()

os.system("clear")
print("Game Taruhan By Ikhsan")
print()
show.money()
print()
print("1. Mulai")
print("2. Tambah Uang")
print("3. Kurangi Uang")

pil = input("\nPilihan: ")

