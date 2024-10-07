import os
os.system("cls")




total_harga = int(input("masukkan total harga : "))
uang_diberikan = int(input("nasukkan uang yang diberikan : "))

kembalian =  uang_diberikan - total_harga

lembar_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if kembalian < 0:
    print("Uang yang diberikan tidak cukup")
else:
    print(f"Kembalian: Rp {kembalian:,}")
    for i in lembar_uang:
        jumlah_uang = kembalian // i
        if jumlah_uang > 0:
            print(f"{jumlah_uang} lembar Rp{i:,}")
        kembalian %= i
            