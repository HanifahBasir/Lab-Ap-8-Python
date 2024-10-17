"""Program permainan menebak angka"""

import random

print("Selamat datang di permainan tebak angka!")
print("Tebaklah angka antara 1 hingga 100.")
print("Anda memiliki maksimal 5 kali percobaan.")
print("Jika ingin berhenti, ketik '0'.\n")

angka_rahasia = random.randint(1, 100)  
percobaan = 5  

for i in range(percobaan):
    tebakan = int(input(f"Percobaan {i+1}: Masukkan angka tebakan Anda: "))

    if tebakan == 0:
        print("Anda telah keluar dari permainan.")
    elif percobaan == i+1:
        print(f"Percobaan telah habis, angka yang benar adalah {angka_rahasia}")
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    elif tebakan < angka_rahasia:
        print("Angka terlalu kecil.")
    elif tebakan == angka_rahasia:
        print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar.")
        break
   
        


