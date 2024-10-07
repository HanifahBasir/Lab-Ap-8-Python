import random
angka_acak = random.randint(1,100)
kesempatan = 5
while kesempatan!=0:
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    if tebakan==0:
        break
    elif tebakan<angka_acak:
        print("Angka terlalu kecil")
        kesempatan-=1
    elif tebakan>angka_acak:
        print("Angka terlalu besar")
        kesempatan-=1
    else:
        print("Selamat! Anda menebak angka dengan benar.")
        break