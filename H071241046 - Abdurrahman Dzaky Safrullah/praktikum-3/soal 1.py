import os
os.system("cls")

tinggi = int(input("masukkan tinggi : "))

panjang = 1

while True:
    print(("+"*panjang).center(tinggi))
    panjang += 2
    if panjang > tinggi:
        break

panjang = tinggi -2 if tinggi % 2 != 0 else tinggi - 1
    
while True:
    print(("+"*panjang).center(tinggi))
    panjang -= 2
    if panjang <= 0:
        break
    
    

