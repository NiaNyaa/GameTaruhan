# Created By Ikhsan
import random
import os
import sys
import time

# Show Tanpa Class
file = open('money.txt','r')
uangshow = file.read()
intuangshow = int(uangshow)
file.close()

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

# Tampilan Program
print("Game Taruhan By Ikhsan")
print()
print("Rp.",intuangshow)
print()
print("1. Mulai")
print("2. Tambah Uang")
print("3. Kurangi Uang")

pil = input("\nPilihan: ")

if pil == "1":
  if intuangshow < 1:
    print("Maaf, Uang Anda Habis")
    sys.exit()

  thn = int(input("Taruhan: "))
  if thn > intuangshow:
    print("Maaf, Uang Anda Tidak Cukup")
    sys.exit()

  data = int(random.randint(1,2))
  if data == 1:
    print("Kamu Menang")
    kondisi.addmoney(thn)
    time.sleep(2)
    os.system('clear && python play.py')
  else:
    print("Kamu Kalah")
    time.sleep(2)
    os.system('clear && python play.py')
  

elif pil == "2":
  brp = int(input("Berapa: "))
  kondisi.addmoney(brp)
  print("Berhasil Menambah:",brp)

