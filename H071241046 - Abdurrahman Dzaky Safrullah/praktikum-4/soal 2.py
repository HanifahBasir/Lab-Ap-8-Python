import os
os.system("cls")


def fungsi(n=0):
    jarak = 0
    bahaya = False
    while True:
        try:
            n = int(input("Masukkan jarak : "))
            if n == 0:
                break
            else:
                jarak += n
                if n > 20:
                    bahaya = True
        except :
            print("Masukkan input yang benar (hanya angka)")

    print(f"Jarak total yang ditempuh = {jarak}")
    if jarak != 50 and (bahaya or bahaya != True):
        print(f"Anda tidak bisa menggali harta karun")
    elif bahaya and jarak == 50:
        print(f"bahaya = Ya")
        print(f"Tidak aman untuk menggali harta karun. Nanti saja")
    else:
        print(f"bahaya = Tidak")
        print(f"Aman! Kamu bisa menggali harta karun dengan aman")
        
            
fungsi()      