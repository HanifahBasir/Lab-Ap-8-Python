######### SOAL 3
######### Nilai



nilai = int(input("masukkan nilai : "))
hadir = int(input("masukkah persentasi kehadiran : "))

if 85<=nilai<=100:
    nilai_huruf = "Predikat A" 
elif 70<=nilai<=84:
    nilai_huruf = "Predikat B" 
elif 0<=nilai<=69:
    nilai_huruf = "Predikat C" 
else:
    nilai_huruf = "Masukkan nilai yang valid"

hadirr = "Lulus" if hadir >= 75 else "Tidak Lulus"

if nilai_huruf == "Masukkan nilai yang valid":
    print(f"{nilai_huruf}")
elif hadirr == "Tidak Lulus":
    print(f"Anda {hadirr}")
else:
    print(f"Anda {hadirr} dengan {nilai_huruf}")