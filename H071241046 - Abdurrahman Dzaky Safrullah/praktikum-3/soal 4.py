import os
os.system("cls")

harga = int(input('Masukkan harga barang : '))
duit = int(input('Berapa duit anda : '))

kembalian = duit - harga

print(f"kembalian anda yaitu = Rp.{kembalian}")

# (pecahan uang yang tersedia adalah: 100.000, 50.000, 20.000, 10.000, 5.000, 2.000,
# 1.000).


pecahan_duit = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if kembalian < 0:
    print("ITU GAK RISPEK")
elif kembalian == 0:
    print("GADA KEMBALIAN")
else:
    print("RINCIAN KEMBALIAN")
    for i in pecahan_duit:
        jumlah_lembar = kembalian // i
        kembalian -= i * jumlah_lembar
        if jumlah_lembar > 0:
            print(f"Rp.{i:,} sebanyak : {jumlah_lembar} lembar")

