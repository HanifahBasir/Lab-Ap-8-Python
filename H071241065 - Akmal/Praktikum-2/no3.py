nilai_akhir = int(input("masukkan nilai akhir : "))
persentase_kehadiran = int(input("masukkan persentase kehadiran : "))

match nilai_akhir:
    case n if 85 <= n <=  100:
        predikat_kelulusan = "lulus dengan predikat A"
    case u if  70 <= u <=84:
        predikat_kelulusan = "lulus dengan predikat B"
    case i if 60 <= i <= 69:
        predikat_kelulusan = "lulus dengan predikat C"
    case p if p  < 60:
        predikat_kelulusan = "tidak lulus"
    case _:
        predikat_kelulusan = "nilai yang anda masukkan salah"
        
if  persentase_kehadiran >= 75 and  predikat_kelulusan == "tidak lulus":
    print("lulus dengan predikat C")
elif persentase_kehadiran < 75:
    print("tidak lulus")
else:
    print(predikat_kelulusan)