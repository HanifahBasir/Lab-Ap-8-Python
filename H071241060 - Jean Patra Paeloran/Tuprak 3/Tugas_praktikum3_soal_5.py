A = int(input("masukkan populasi awal Serangga A: "))
B = int(input("masukkan populasi awal Serangga B: "))

Hari = int(input("Masukkan jumlah hari: "))
for i in range (1,Hari+1):
    if i%5==0:
        print(f"Hari {i}: Predator memakan 10% populasi")
        A = A//(10/9)*1.3
        B = B//(10/9)*1.5
    elif i%2==0:
        A*=0.8
        B*=0.6
    else:
        A*=1.3
        B*=1.5
    print(f"Hari {i}: Serangga = {int(A)}, Serangga B = {int(B)}")