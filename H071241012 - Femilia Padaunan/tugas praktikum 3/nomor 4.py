total_harga=int(input("masukkan harga total: "))
bayar= int(input("masukkan uang yang diberikan: "))

kembalian = bayar-total_harga
uang = [100000,50000,20000,10000,5000,2000,1000]

if kembalian==0:
    print("tidak ada kembalian")
for pecahan in uang:
    if kembalian>=pecahan:
        jumlah_lembar=kembalian//pecahan
        kembalian%=pecahan
        print(f"{jumlah_lembar} lembar Rp{pecahan}")