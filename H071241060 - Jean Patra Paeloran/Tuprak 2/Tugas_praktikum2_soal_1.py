a = int(input("Masukan panjang sisi pertama : "))
b = int(input("Masukan panjang sisi kedua : "))
c = int(input("Masukan panjang sisi kedua : "))
if a>0 and b>0 and c>0:
    miring = a
    alas = b
    tinggi = c
    if b>a:
        miring = b
        alas = a
        tinggi = c
        if c>b:
            miring = c
            alas = a
            tinggi = b
    elif c>a:
        miring = c
        alas = a
        tinggi = b
    if a==b:
        if b==c:
            print("Segitiga Sama Sisi")
        else:
            print("Segitiga Sama Kaki")
    elif b==c:
        print("Segitiga Sama Kaki")
    elif a==c:
        print("Segitiga sama kaki")
    elif alas**2+tinggi**2==miring**2:
        print("Segitiga Siku-Siku")
    else:
        print("Segitiga sembarang")
else:
    print("Bukan sebuah segitiga")