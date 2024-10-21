import random as rd

angka_rahasia = rd.randint(1, 100)

tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))

kesempatan = 4
while kesempatan > 0 and tebakan != 0:
    if tebakan == angka_rahasia:
        print("Selamat! Tebakanmu benar.")
        break
    elif tebakan < angka_rahasia:
        print("Tebakanmu terlalu rendah.")
    else:
        print("Tebakanmu terlalu tinggi.")
    
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    kesempatan -= 1
    
    if tebakan == 0:
        break
if kesempatan == 0:
    print(f"Kesempatan habis. Angka rahasia adalah {angka_rahasia}")
