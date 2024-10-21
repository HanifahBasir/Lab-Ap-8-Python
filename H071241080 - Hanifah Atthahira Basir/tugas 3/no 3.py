"""Program untuk mengontrol pergerakan robot"""

N = int(input("N: "))
M = int(input("M: "))

for i in range(N):
    if i % 2 == 0: # Baris genap, kiri ke kanan
        for j in range(M):
            print(f"MOVE to ({i},{j})")
    else:  # Baris ganjil, kanan ke kiri
        for j in range(M-1, -1, -1):
            print(f"MOVE to ({i},{j})")