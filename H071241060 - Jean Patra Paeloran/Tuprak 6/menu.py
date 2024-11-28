inventori = {}
def menambah():
    Kode = input("Masukkan kode barang: ")
    if Kode in inventori:
        print("Kode sudah ada, silahkan masukkan kode lain")
        menambah()
        return
    if Kode.isnumeric():
        nama = input("Masukkan nama barang: ").capitalize()
        jumlah = input("Masukkan jumlah barang: ")
        harga = input("Masukkan harga per unit: ")
        inventori[Kode] = {
            "Nama"  : nama,
            "Jumlah": jumlah,
            "Harga" : harga
        }
        print("Barang berhasil ditambahkan.")
    else:
        print("Barang harus integer")
        menambah()
def menghapus():
    try:
        Kode = input("Masukkan kode barang yang akan dihapus: ")
        del inventori[Kode]
        print("Barang berhasil dihapus.")
    except:
        print(f"Barang dengan kode {Kode} tidak ditemukan")
        menghapus()
def tampilkan():
    kosong = "ada"
    for i in inventori:
        kosong = "tidak"
        barang = inventori[i]
        print(f"Kode: {i}, Nama: {barang['Nama']}, Jumlah: {barang['Jumlah']}, Harga per unit: {barang['Harga']}")
    if kosong == "ada":
        print("Inventori masih kosong")
def mencari():
    opsi = int(input("Cari berdasarkan (1) Kode atau (2) Nama: "))
    if opsi == 1:
        Kode = input("masukkan kode barang: ")
        if Kode in inventori:
            barang = inventori[Kode]
            print(f"Kode: {Kode}, Nama: {barang['Nama']}, Jumlah: {barang['Jumlah']}, Harga per unit: {barang['Harga']}")
        else:
            print(f"Barang dengan kode {Kode} tidak ditemukan")
    elif opsi == 2:
        Ada = False
        Nama = input("Masukkan nama barang: ").capitalize()
        for Kode in inventori:
            if Nama == inventori[Kode]['Nama']:
                print(f"Kode: {Kode}, Nama: {inventori[Kode]['Nama']}, Jumlah: {inventori[Kode]['Jumlah']}, Harga per unit: {inventori[Kode]['Harga']}")
                Ada = True
                break
        if Ada == False: 
            print(f"Barang dengan nama {Nama} tidak ditemukan")    
def update():
    Kode = input("Masukkan kode barang yang ingin diupdate: ")
    if Kode in inventori:    
        jumlah = input("Masukkan jumlah baru: ")
        harga = input("Masukkan harga baru: ")
        inventori[Kode] = {
            "Nama"  : inventori[Kode]['Nama'],
            "Jumlah": jumlah,
            "Harga" : harga
        }
        print("Barang berhasil diupdate.")
    else:
        print(f"Barang dengan kode {Kode} tidak ada")