import os
os.system("cls")


import random

# n = int(input("masukkan tebankan : "))
acak = random.randint(1,100)

kesempatan = 5

while kesempatan > 0:
    n = int(input(f"\nmasukkan tebakan (ketik '0' untuk surend): "))
    kesempatan -= 1
    if n == 0:
        break
    if n > acak:
        print(f"angka terlalu besar, sisa kesempatan ({kesempatan})")
        
    elif n < acak:
        print(f"angka terlalu kecil, sisa kesempatan ({kesempatan})")
    else:
        print(f"ANDA BENAR")
        break
    

    
print(f"Tebakan yang benar yaitu = {acak}")
    