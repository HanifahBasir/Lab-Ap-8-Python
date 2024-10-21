import random
angka_rahasia = random.randint(1, 100)

for i in range(5):
    tebakan = int(input("masukkan tebakan anda (hanya ankgka 1-100, ketik 0 untuk berhenti): "))
    
    if tebakan < 0 or tebakan > 100:
        print("hanya angka 1-100")
        break
    elif tebakan == angka_rahasia:
        print("tebakan anda benar")
        break
    elif i == 4 and tebakan != angka_rahasia:
        print(f"kesempatan menjawab anda sudah habis anda kalah jawabannya adalah {angka_rahasia}")
        break
    elif tebakan == 0:
        print(f"berhenti, jawabannya adalah {angka_rahasia}")
        break
    elif tebakan < angka_rahasia:
        print("angka terlalu kecil")
        continue
    elif tebakan > angka_rahasia:
        print("angka terlalu besar")
        continue
    else:
        print("inputan yang anda masukkan salah")