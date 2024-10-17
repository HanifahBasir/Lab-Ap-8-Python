"""Program untuk mencetak pola bintang dalam bentuk belah ketupat""" 

x = int(input("Masukkan jumlah baris: "))

if x % 2 == 0 : #genap
    for i in range (x//2): #bagian atas belah ketupat
        print(" " * (x//2 - i - 1) + "*" * (2 * i + 1))
    for i in range (x//2 -1, -1, -1): #bagian bawah belah ketupat
        print(" " * (x//2 - i - 1) + "*" * (2 * i + 1))
else: #ganjil
    for i in range (x//2 + 1): #bagian atas belah ketupat
        print(" " * (x//2 - i) + "*" * (2 * i + 1))
    for i in range (x//2): #bagian bawah belah ketupat
        print(" " * (i+1) + "*" * (x-2 * (i+1)))
    