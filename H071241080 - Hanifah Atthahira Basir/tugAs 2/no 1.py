""" Program untuk mengidentifikasi jenis segitiga berdasarkan panjang sisi-sisinya """

a = int(input("Masukkan panjang sisi pertama: "))
b = int(input("Masukkan panjang sisi kedua: "))
c = int(input("Masukkan panjang sisi ketiga: "))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or b == c or a == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid.")


