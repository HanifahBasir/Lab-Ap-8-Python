nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))


def status_kelulusan(nilai, kehadiran, tugas):
    if kehadiran < 75:
        return "Tidak Lulus"

    if 85 <= nilai <= 100:
        return "Lulus dengan Predikat A"
    elif 70 <= nilai <= 84:
        return "Lulus dengan Predikat B"
    elif 60 <= nilai <= 69:
        return "Lulus dengan Predikat C"
    elif nilai < 60:
        tugas = int(input("Berapa nilai tugas tambahan: "))
        if tugas > 70 and kehadiran >= 75:
            return "Lulus dengan Predikat C"
    else:
        return "Tidak Lulus"

print(status_kelulusan(nilai, kehadiran,))
