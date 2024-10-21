""" Program untuk menentukan kelulusan mahasiswa """


nilai_akhir = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))


if kehadiran < 75:
    hasil = "Tidak Lulus (Kehadiran kurang dari 75%)"
elif nilai_akhir >= 85:
    hasil = "Lulus dengan Predikat A"
elif 70 <= nilai_akhir < 85:
    hasil = "Lulus dengan Predikat B"
elif 60 <= nilai_akhir < 70:
    hasil = "Lulus dengan Predikat C"
elif nilai_akhir < 60:
    tugas_tambahan = int(input("Masukkan nilai tugas tambahan (0-100): "))    
    if tugas_tambahan >= 70 and kehadiran >= 75:
        hasil = "Lulus dengan Predikat C (berdasarkan tugas tambahan)"
    else:
        hasil = "Tidak Lulus"

print(hasil)
