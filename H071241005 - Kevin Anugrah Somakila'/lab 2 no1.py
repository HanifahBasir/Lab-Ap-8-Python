a = int(input("Masukkan panjang sisi pertama: "))
b = int(input("Masukkan panjang sisi kedua: "))
c = int(input("Masukkan panjang sisi ketiga: "))

# jenis segitiga
if a + b <= c or b + c <= a or c + a <=b:
    print("Tidak dapat membuat segitiga yang valid")
elif a == b == c:
    print("Segitiga sama sisi")
elif a == b != c or c==b != a or b==c != a:
    print("segitiga sama kaki")
else :
    print("segitiga sembarang")

