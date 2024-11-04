harga_total = int(input("Masukkan total harga: "))
uang_awal = int(input("Masukkan uang yang diberikan: "))
uang_kasir = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
uang_kembalian = uang_awal - harga_total
for m in uang_kasir:
    if uang_kembalian >= m:
        lembar = uang_kembalian // m
        uang_kembalian %= m
        print(f"{lembar} lembar {m}")