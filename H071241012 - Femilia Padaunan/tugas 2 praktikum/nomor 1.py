 # input panjang sisi segitiga
a=int(input("masukkan panjang sisi pertama: "))
b=int(input("masukkan panjang sisi kedua: "))
c=int(input("masukkan panjang sisi ketiga: "))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or b == c or a == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid.")