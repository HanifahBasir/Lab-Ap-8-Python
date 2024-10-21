n = int(input("Masukkan Jumlah Baris: "))
for i in range(n+1):
    if i%2!=1:
        continue
    if i==n:
        continue
    bintang = " * "*i
    hasil = bintang.center(n*3," ")
    print(hasil)
for i in range(n,0,-1):
    if i%2==0:
        continue
    bintang = " * "*i
    hasil = bintang.center(n*3," ")
    print(hasil)        