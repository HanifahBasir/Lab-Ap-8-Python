import os

GUDANG = {}

def menu():
    print('=== Menu Inventory Barang ===')
    print('1. Tambah Barang')
    print('2. Hapus Barang')
    print('3. Tampilkan Daftar Barang')
    print('4. Cari Barang')
    print('5. Update Data Barang')
    print('6. Keluar')


def tambah():
    print('=== Tambah Barang ===')

    while True:
        id = input('Masukkan ID Barang(0 untuk stop): ')
        if id == '0':
            return

        if id in GUDANG:
            print('ID Barang sudah ada. Silakan gunakan ID yang berbeda.\n')
            continue

        nama = input('Masukkan Nama Barang(0 untuk stop): ')
        if nama == '0':
            return

        for i, data in GUDANG.items():
            if data['nama'] == nama:
                data['jumlah'] = int(input('Nama sudah ada, Anda akan mengupdate data Anda. Masukkan jumlah baru: '))
                data['harga'] = float(input('Masukkan harga baru: '))
                print('Barang berhasil diupdate!\n')
                return

        while True:
            try:
                jumlah = int(input('Masukkan Jumlah Barang(0 untuk stop): '))
                if jumlah == 0:
                    return
                if jumlah < 0:
                    print('Jumlah tidak boleh 0 atau negatif. Silakan coba lagi.\n')
                    continue
                break
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk jumlah barang.\n")

        while True:
            try:
                harga = float(input('Masukkan Harga Barang(0 untuk stop): '))
                if harga == 0:
                    return
                if harga < 0:
                    print('Harga tidak boleh 0 atau negatif. Silakan coba lagi.\n')
                    continue
                break
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk harga barang.\n")

        GUDANG[id] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print('Barang berhasil ditambahkan!\n')
        break


def hapus():
    print('=== Hapus Barang ===')

    while True:
        id = input('Masukkan ID Barang yang ingin dihapus (0 untuk stop): ')
        if id == '0':
            break

        if id in GUDANG:
            del GUDANG[id]
            print('Barang berhasil dihapus!\n')
            break
        else:
            print('ID Barang tidak ditemukan!\n')


def tampilkan_barang():
    print('=== Daftar Barang ===')

    if not GUDANG:
        print('Tidak ada barang dalam inventory.\n')
    else:
        for i in GUDANG:
            print(f'ID: {i}, Nama: {GUDANG[i]["nama"]}, Jumlah: {GUDANG[i]["jumlah"]}, Harga: {GUDANG[i]["harga"]}\n')

def cari():
    print('=== Cari Barang ===')

    while True:
        try:
            pilihan = int(input("Cari berdasarkan (1) ID (2) nama (0 untuk stop): "))
        except ValueError:
            print("Inputan harus berupa angka.")
            continue

        if pilihan == 0:
            break

        if pilihan == 1:
            id = input('Masukkan ID Barang yang ingin dicari(0 untuk stop): ')

            if id == 0:
                break
            else:
                if id in GUDANG:
                    data = GUDANG[id]
                    print(f'ID: {id}, Nama: {data["nama"]}, Jumlah: {data["jumlah"]}, Harga: {data["harga"]}\n')
                else:
                    print('ID Barang tidak ditemukan!\n')


        elif pilihan == 2:
            nama = input('Masukkan nama Barang yang ingin dicari(0 untuk stop): ')
            found = False

            if nama == 0:
                break

            for id, data in GUDANG.items():
                if data["nama"] == nama:
                    print(f'ID: {id}, Nama: {data["nama"]}, Jumlah: {data["jumlah"]}, Harga: {data["harga"]}\n')
                    found = True
                    break

            if not found:
                print('Nama Barang tidak ditemukan!\n')
        else:
            print('Inputan salah\n')


def update():
    print('=== Update Data Barang ===')
    id = input('Masukkan ID Barang yang ingin diupdate(0 untuk stop): ')
    if id == 0:
        return

    if id in GUDANG:
        while True:
            try:
                jumlah_baru = int(input('Masukkan Jumlah Barang baru (kosongkan jika tidak ingin mengubah. 0 untuk stop): '))
                if jumlah_baru == 0:
                    return
                break
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk jumlah barang.\n")

        while True:
            try:
                harga_baru = float(input('Masukkan Harga Barang baru (kosongkan jika tidak ingin mengubah. 0 untuk stop): '))
                if harga_baru == 0:
                    return
                break
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk harga barang.\n")

        if jumlah_baru != '':
            GUDANG[id]['jumlah'] = jumlah_baru
        if harga_baru != '':
            GUDANG[id]['harga'] = harga_baru

        print('Data barang berhasil diupdate!\n')
    else:
        print('ID Barang tidak ditemukan!\n')

def main():
    os.system('cls')

    while True:
        menu()
        try:
            opsi = int(input('Pilih opsi (1-6): '))
        except ValueError:
            print('Opsi tidak valid! Silakan pilih lagi.\n')
            continue

        if opsi == 1:
            tambah()
        elif opsi == 2:
            hapus()
        elif opsi == 3:
            tampilkan_barang()
        elif opsi == 4:
            cari()
        elif opsi == 5:
            update()
        elif opsi == 6:
            print('Terima kasih! Program selesai.')
            break
        else:
            print('Opsi tidak valid! Silakan pilih lagi.\n')

main()
