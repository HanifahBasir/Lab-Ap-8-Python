""" Program untuk menentukan harga tiket """


usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota? (ya/tidak): ")


if usia < 5:
    harga_tiket = 0
elif 5 <= usia <= 12:
    harga_tiket = 50000
elif 13 <= usia <= 59:
    harga_tiket = 100000
else:
    harga_tiket = 70000


harga_final = harga_tiket * 0.8 if anggota == "ya" else harga_tiket


print(f"Harga tiket: Rp{int(harga_final)}")
