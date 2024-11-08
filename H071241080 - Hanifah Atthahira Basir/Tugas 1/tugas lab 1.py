# No. 1
"""Mengambil keputusan investasi berdasarkan perubahan persentase harga:"""

print("\n1. PROGRAM UNTUK MENENTUKAN KEPUTUSAN INVESTASI\n")

harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = float(input("Masukkan harga saham hari ini: "))

perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = ["Jual", "Tahan", "Beli"][
    (perubahan_persen > 5) * 2 + (-3 <= perubahan_persen <= 5)
]

print(f"Perubahan persentase harga: {perubahan_persen:.2f}%")
print(f"Rekomendasi: {rekomendasi}")



# No. 2
"""Periksalah apakah sebuah karakter terdapat dalam sebuah kalimat"""

print("\n2. PROGRAM UNTUK MEMERIKSA APAKAH SEBUAH KARAKTER TERDAPAT DALAM KALIMAT\n")

karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

jawaban = "Karakter merupakan bagian dari Kalimat" * (karakter in kalimat) or "Karakter tidak ditemukan dalam Kalimat"

print(jawaban)



# No. 3
"""Buatlah sebuah program yang mengubah jumlah detik yang diberikan menjadi 
format waktu jam:menit:detik"""

print("\n3. PROGRAM KONVERSI DETIK KEDALAM FORMAT JAM:MENIT:DETIK\n")

def konversi_detik(detik):
    
    jam = detik // 3600
    menit = (detik % 3600) // 60
    detik = detik % 60
    
    return f"{jam:02}:{menit:02}:{detik:02}"
   
total_detik = int(input("Masukkan jumlah detik: "))
waktu = konversi_detik(total_detik)

print("Waktu dalam format jam:menit:detik adalah:", waktu)



# No. 4
"""Buatlah program yang bisa secara otomatis mengonversi suhu dari skala
Celcius ke beberapa skala lain seperti Kelvin, Reamur, dan Fahrenheit."""

print("\n4. PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah ",celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

# Fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")