# tebak angka

print("selamat datang pada permainan tebak angka")
print("masukkan angka antara 1-100")


import random
angka = random.randint(1, 100)

max_percobaan = 5

while max_percobaan:
    tebak = int(input("masukkan tebakan Anda (0 untuk berhenti): "))
    if angka == tebak:
        print("selamat! Anda menebak angka dengan benar.")
        break
    elif angka < tebak:
        print("Angka terlalu besar")
        max_percobaan -=1

    elif angka > tebak:
        print("Angka terlalu kecil")
        max_percobaan -=1

    elif max_percobaan==0:
        print("percobaan habis")
    
else:
    print(f"percobaan telah habis, angka yang benar adalah {angka}")