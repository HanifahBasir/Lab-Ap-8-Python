""" Program untuk menentukan layanan paket yang sesuai """


penggunaan_data = float(input("Masukkan penggunaan data per bulan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)?: ")
jenis_pengguna = input("Apakah Anda pengguna personal atau bisnis?: ")


if penggunaan_data < 10:
    if waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
        paket = "Paket A"
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == "peak" and jenis_pengguna == "personal":
        paket = "Paket B"
elif penggunaan_data > 50:
    if waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
        paket = "Paket C"
    elif waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
        paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"

print(f"Paket layanan yang cocok untuk Anda: {paket}")
