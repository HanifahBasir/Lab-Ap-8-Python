usia = int(input("masukkan usia : "))
apakah_anggota = input("apakah anda anggota (ya/tidak) : ").lower()

match usia:
    case u if 0 < u < 5:
        kategori_tiket = 0
    case u if 5 <= u <= 12:
        kategori_tiket =  50000
    case u if 13 <= u <= 59:
        kategori_tiket =  100000
    case u if u < 0:
        kategori_tiket = "usia tidak valid"
    case _:
        kategori_tiket =  70000   

jika_anggota = kategori_tiket * 0.8 if apakah_anggota == "ya" else kategori_tiket * 1 

if kategori_tiket == 0:
    print("harga tiket gratis")
else:
    print(f"harga tiket : Rp. {jika_anggota:.0f}")