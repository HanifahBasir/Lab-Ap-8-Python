sisi_pertama = int(input("masukkan panjang sisi pertama : "))
sisi_kedua = int(input("masukkan panjang sisi kedua : "))
sisi_ketiga = int(input("masukkan panjang sisi ketiga : "))

if sisi_pertama <= 0 or sisi_kedua <= 0 or sisi_ketiga <= 0:
    print("tidak dapat membentuk segitiga yang valid")
elif sisi_pertama == sisi_kedua == sisi_ketiga:
    print("segitiga sama sisi")
elif sisi_pertama + sisi_kedua <= sisi_ketiga or sisi_pertama + sisi_ketiga <= sisi_kedua or sisi_kedua + sisi_ketiga <= sisi_pertama:
    print("tidak dapat membentuk segitiga yang valid")
elif sisi_pertama == sisi_kedua or sisi_pertama == sisi_ketiga or sisi_kedua == sisi_ketiga:
    print("segitiga sama kaki")
else:
    print("segitiga sembarang")