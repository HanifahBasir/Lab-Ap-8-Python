usia = int(input("Masukkan Usia: "))
anggota = input("Apakah anda anggota (ya/tidak): ")

# rekomendasi harga tiket
if usia < 5:
    harga_tiket= 0
elif 5<= usia <=12:
    harga_tiket= 50000
elif 13<= usia <=59:
    harga_tiket= 100000
else:
    harga_tiket= 70000

harga_diskon = harga_tiket-(harga_tiket*20/100) if anggota=="ya" else harga_tiket

print("Harga tiket: Rp",int(harga_diskon))
