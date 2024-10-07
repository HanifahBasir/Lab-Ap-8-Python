######## SOAL 4
######## REKOMENDASI



data = int(input("Masukkan penggunaan data (GB) : "))

print('''
> Penggunaan di Luar Jam Sibuk (Off-Peak): Penggunaan data antara jam 11 malam hingga 7 pagi.
> Penggunaan di Jam Sibuk (Peak): Penggunaan data di luar jam 11 malam hingga 7 pagi.
''')

waktu = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? : ")

print('''
> Pengguna Personal: Menggunakan internet untuk keperluan sehari-hari seperti browsing, streaming, dan media sosial.
> Pengguna Bisnis: Menggunakan internet untuk keperluan bisnis seperti video conference, hosting website, dan cloud services.
''')

jenis = input("Apakah anda penggunaa personal atau bisnis? : ")

match data:
    case d if d < 10:
        data = "ringan"
    case d if 10<=d<=50:
        data = "sedang"
    case d if d > 50:
        data = "berat"

if data == "ringan" :
    rekomendasi = "tidak"
    if waktu == "off-peak":
        if jenis == "personal":
            rekomendasi = "Paket A"
elif data == "sedang":
    rekomendasi = "tidak"
    if waktu == "peak":
        if jenis == "personal":
            rekomendasi = "Paket B"
elif data == "berat" and waktu == "peak" and jenis == "personal" or jenis == "bisnis":
    rekomendasi = "tidak"
    if waktu == "peak":
        if jenis == "personal" or jenis == "bisnis":
            rekomendasi = "Paket C"
elif data == "berat" and waktu == "off-peak" and jenis == "bisnis":
    rekomendasi = "tidak"
    if waktu == "off-peak":
        if jenis == "bisnis":
            rekomendasi = "Paket D"
else:
    rekomendasi = "tidak"


if rekomendasi == "tidak":
    print("Tidak ada paket yang cocok")
else:
    print(f"rekomendasi untuk anda yaitu : {rekomendasi}")
    
    
#  