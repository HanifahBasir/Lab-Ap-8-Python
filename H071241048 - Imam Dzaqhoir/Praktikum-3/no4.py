harga = int(input('masukkan total harga: '))
bayar = int(input('masukkan uang yang diberikan: '))

# tambah if bayar < harga dia ngutang
if bayar < harga:
    print('jangan ngutang')
else:
    kembalian = bayar - harga

    mata_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    print('kembalianmu berupa:')

    for i in mata_uang:
        print(i)
        jumlah = kembalian // i
        kembalian = kembalian % i
        if jumlah > 0:
            print(f'{jumlah} lembar Rp.{i:,}')