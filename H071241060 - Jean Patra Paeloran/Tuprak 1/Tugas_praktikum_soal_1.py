harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105.0
persentase_perubahan = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100
rekomendasi = (
    "Beli" * (persentase_perubahan > 5)+
    "Tahan" * (5 >= persentase_perubahan >= -3)+
    "Jual" * (persentase_perubahan < -3)
)
print(f"Perubahan persentase harga saham:{persentase_perubahan:.2f}%")
print(f"Rekomendasi investasi:{rekomendasi}")

