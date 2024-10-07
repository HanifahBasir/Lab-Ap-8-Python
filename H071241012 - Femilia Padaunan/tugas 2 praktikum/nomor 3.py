# nomor 3
# kehadiran siswa
nilai=int(input("masukkan nilai akhir: "))
kehadiran=int(input("masukkan persentasi kehadiran: "))

if kehadiran >= 75:
    if 85<= nilai <= 100:
     print("lulus dengan predikat A")
    elif 70<= nilai <=84:
      print("lulus dengan predikat B")
    elif 60<= nilai <=69:
      print("lulus dengan predikat C")
    elif nilai <60:
      tugas_tambahan= int(input("masukkan nilai tugas tambahan: "))
      if tugas_tambahan >=70:
        print("lulus dengan predikat C")
      else:
        print("tidak lulus")
     
else:
    print("tidak lulus")