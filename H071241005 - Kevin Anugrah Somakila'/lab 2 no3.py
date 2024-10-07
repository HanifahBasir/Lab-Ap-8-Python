nilai = int(input("masukkan nilai: "))
kehadiran = int(input("masukkan persentasi kehadiran: "))

#  rekomendasi predikat
if 80<= nilai<=100 and kehadiran >=75:
    predikat="A"
elif 70<= nilai <=84 and kehadiran >=75:
    predikat="B"
elif 60<= nilai <= 69 and kehadiran >=75:
    predikat="C"
# elif nilai <60 and kehadiran >=75:
#     predikat="C"
elif nilai<= 60 and kehadiran <= 75 :
    tugas_tambahan = int(input("tugas_tambahan: ")) 
    if tugas_tambahan >=70:
        predikat ="c"
    else: 
        predikat = "tidak lulus"
   

else:
    predikat = "Tidak Lulus"




print(f"Lulus dengan predikat {predikat} ")