nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))
if kehadiran>=75:
    if 85<=nilai<=100:
        print("Lulus dengan Predikat A")
    elif 70<=nilai<85:
        print("Lulus dengan Predikat B")
    elif 60<=nilai<70:
        print("Lulus dengan Predikat c")
    else:
        tambahan = int(input("nilai tugas tambahan: "))
        if tambahan>70:
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")
else:
    print("Tidak Lulus")