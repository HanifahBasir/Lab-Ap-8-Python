
hargaSahamKemarin = float(input("masukkan harga saham kemarin : "))
hargaSahamSekarang = 105.0
perubahanPersentase = (hargaSahamSekarang - hargaSahamKemarin) / hargaSahamKemarin * 100

hasil = (perubahanPersentase > 5) * "beli" + (perubahanPersentase < -3) * "jual" + (-3 <= perubahanPersentase <= 5) * "tahan"

print(f"Perubahan persentase harga adalah {perubahanPersentase:.2f}%")
print(f"Rekomendasi investasi: {hasil}")
    