data = float(input("Masukkan penggunaan data per bulan (GB): "))
waktu = input("Apakah mayoritas penggunaan di jam sibuk (Peak) atau luar jam sibuk (Offpeak)? ").lower()
tipe = input("Apakah Anda pengguna 'Personal' atau 'Bisnis'? ").lower()

# Membuat kategori
kategori_data = "ringan" if data < 10 else "sedang" if data <= 50 else "berat"
kategori_waktu = "peak" if waktu == "peak" else "offpeak"
kategori_pengguna = "personal" if tipe == "personal" else "bisnis"

def paket_internet(kategori_data, kategori_waktu, kategori_pengguna):
    if (kategori_data, kategori_waktu, kategori_pengguna) == ("ringan", "offpeak", "personal"):
        return "Paket A"
    elif (kategori_data, kategori_waktu, kategori_pengguna) == ("sedang", "peak", "personal"):
        return "Paket B"
    elif (kategori_data, kategori_waktu) == ("berat", "peak") and kategori_pengguna in ["personal", "bisnis"]:
        return "Paket C"
    elif (kategori_data, kategori_waktu, kategori_pengguna) == ("berat", "offpeak", "bisnis"):
        return "Paket D"
    return "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket_internet(kategori_data, kategori_waktu, kategori_pengguna)}")
