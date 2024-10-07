# menghitung perubahan persentase
harga_saham_kemarin = float (input("masukan harga saham kemarin: "))

harga_saham_hari_ini = 105.0

perubahan_persentase = (harga_saham_hari_ini - harga_saham_kemarin)/ harga_saham_kemarin * 100

# menentukan rekomendasi investasi
beli = (perubahan_persentase > 5) #0
tahan = (-3 <= perubahan_persentase <= 5) #0
jual = (perubahan_persentase < -3) #1

# mendapatkan rekomendasi
hasil_rekomendasi =beli*"beli"+tahan*"tahan"+jual*"jual"
# output
print(f"perubahan persentase : {perubahan_persentase:.2f}%")
print(f"rekomendasi investasi: " + hasil_rekomendasi )

