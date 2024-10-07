Harga = int(input("Masukkan total harga: "))
Uang = int(input("Masukkan uang yang diberikan: "))
nominal =[100000,50000,20000,10000,5000,2000,1000]
kembalian = Uang-Harga
if kembalian>0:
    for i in nominal:
        lembar = kembalian//i
        kembalian%=i
        if lembar==0:
            continue
        print(f"{lembar} lembar Rp {i:,}")
elif Harga==Uang:
    print("Uang pas")
else:
    print("uang tidak cukup")
