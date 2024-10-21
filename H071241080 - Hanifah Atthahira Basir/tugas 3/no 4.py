"""Program untuk menghitung kembalian"""

total_harga = int(input("Masukkan total harga: Rp "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: Rp "))

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

kembalian = uang_diberikan - total_harga
    
if kembalian < 0:
    print("Uang yang diberikan tidak cukup")
elif kembalian == 0:
    print("Tidak ada kembalian")
else:
    print(f"Kembalian: Rp {kembalian} rupiah")
    print("Rincian kembalian:")
        
    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah_lembar = kembalian // pecahan
            #kembalian %= pecahan
            print(f"{jumlah_lembar} lembar uang Rp {pecahan}")


