import menu

while True:
    print(
        """
=== Menu Inventori Barang ===
1. Tambah Barang
2. Hapus Barang
3. Tampilkan Barang
4. Cari barang
5. Update barang
6. Keluar"""
    )
    try:
        opsi = int(input("Pilih opsi (1-6):"))
        match opsi:
            case 1:
                menu.menambah()
            case 2:
                menu.menghapus()
            case 3:
                menu.tampilkan()
            case 4:
                menu.mencari()
            case 5:
                menu.update()
            case 6:
                break
            case _:
                print("Opsi tidak tersedia")
    except ValueError:
        print("Opsi tidak valid")