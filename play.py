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

# Add Money
class kondisi():
   def addmoney(self,n):
    file1 = open('money.txt','r')
    uangk = file1.read()
    uangkint = int(uangk)
    file1.close()
    file2 = open('money.txt','w')
    tambah = uangkint + n
    strtambah = str(tambah)
    file2.write(strtambah)
    file2.close()

# Name Class
show = show()
kondisi = kondisi()

os.system("clear")
print("Game Taruhan By Ikhsan")
print()
show.money()
print()
print("1. Mulai")
print("2. Tambah Uang")
print("3. Kurangi Uang")

pil = input("\nPilihan: ")

if pil == "2":
  brp = int(input("Berapa: "))
  kondisi.addmoney(brp)

