## nomor 1
# rekomendasi saham
def dapatkan_rekomendasi (ubah_persentase):
    rekomendasi = {"Beli": lambda x: x > 5,"Tahan": lambda x: -3 <= x <= 5,"Jual": lambda x: x < -3}
    return next(key for key, condition in rekomendasi.items() if condition(ubah_persentase))
# nilai
harga_saham_kemarin =float(input("Masukkan harga saham kemarin: "))
harga_saham_saat_ini =105
# persentase
perubahan_persen = ((harga_saham_saat_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100
rekomendasi = dapatkan_rekomendasi(perubahan_persen)

# output
print(f"Perubahan persentase saham kemarin:{perubahan_persen:.2f}%")
print(f"rekomendasi: {rekomendasi}")


# ## nomor 2
# # karakter dan kalimat
# masukkan_karakter = input("Masukkan karakter: ")
# masukkan_Kalimat = input("Masukkan kalimat: ")

# # output
# print(f"{masukkan_karakter} tidak ditemukan dalam \"{masukkan_Kalimat}\" ")


# ## nomor 3
# def mengubah_detik(detik):
#   jam = detik//3600
#   menit = (detik % 3600)//60
#   detik = detik % 60
#   return f"{jam:02}:{menit:02}:{detik:02}"


# konfersi_detik_ke_jam ="konfersi detik ke jam"
# total_detik = int(input("Masukkan jumlah detik: "))

# format_waktu = mengubah_detik(total_detik)

# print(f"{konfersi_detik_ke_jam}")
# print(f"{format_waktu}")


# ## nomor 4
# def mengubah_suhu(celcius):
#   kelvin = int(suhu_celcius +273)
#   reamur = int(4/5 * suhu_celcius)
#   farenheit = int((suhu_celcius * 9/5) + 32)
#   return kelvin, reamur, farenheit

# konfersi_suhu = "konfersi suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit"
# suhu_celcius = int(input("Masukkan suhu dalam Celcius: "))

# kelvin, reamur, farenheit = mengubah_suhu(suhu_celcius)
# print(f"{konfersi_suhu}")
# print(f"Hasil konversi dari suhu {suhu_celcius} derajat ke Kelvin adalah : {kelvin}K ")
# print(f"Hasil konversi dari suhu {suhu_celcius} derajat ke Reamur adalah : {reamur}R ")
# print(f"Hasil konversi dari suhu {suhu_celcius} derajat ke Farenheit adalah : {farenheit}F ")