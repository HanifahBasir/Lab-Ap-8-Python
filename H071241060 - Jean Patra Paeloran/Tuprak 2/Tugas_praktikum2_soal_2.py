Harga = "gratis"
usia = int(input("Masukkan usia: "))
if usia>=5:
    keanggotaan = str(input("Apakah Anda anggota(ya/tidak): "))
    if 5<=usia<=12:
        Harga = "Rp. 40.000" if keanggotaan=="ya" else "Rp. 50.000"
    elif 13<=usia<=59:
        Harga = "Rp. 80.000" if keanggotaan=="ya" else "Rp. 100.000"
    else:
        Harga = "Rp. 56.000" if keanggotaan=="ya" else "Rp. 70.000"
    print(f"Harga tiket: {Harga}")
else:
    print(f"Harga tiket: {Harga}")