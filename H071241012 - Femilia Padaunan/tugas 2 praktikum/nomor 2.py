usia = int(input("masukkan usia: "))
anggota = input("apakah anda anggota?(ya/tidak): ")

if usia <5:
    harga_tiket = 0
elif 5 <= usia <= 12:
    harga_tiket = 50000
elif 13 <= usia <= 59:
    harga_tiket = 100000
else:
    harga_tiket = 70000

harga_tiket_akhir = harga_tiket-(harga_tiket*20/100) if anggota=="ya" else harga_tiket

print(f"harga tiket:Rp{harga_tiket_akhir}")