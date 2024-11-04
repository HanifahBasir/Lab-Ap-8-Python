
penyimpanan = {}

#tambah barang
def tambah_barang():
    try:
        kode = int(input("masukkan kode:"))
        
        if kode in  penyimpanan:
            print("kode sudah ada, masukkan kode lain")
            return
        
        nama = input("masukkan nama: ")
        jumlah = input("masukkan jumlah: ")
        harga = float(input("masukkan jumlah harga: "))
            
        penyimpanan[kode] = {
            "nama": nama,
            "jumlah": jumlah,
            "harga": harga
        }
        print(f"barang berhasil ditambahkan")
    except:
        print(f"barang gagal ditambahkan")


#menghapus barang
def hapus_barang(): 
    try:
        hapus = int(input("masukkan kode barang yang ingin dihapus: "))
        if hapus in penyimpanan:
            del penyimpanan[hapus]
            print("barang berhasil dihapus")
        else:
            print("kode tidak ada")
    except:
        print("barang gagal dihapus/barang tidak ada")


#tampilkan barang
def tampilkan_barang():
    try:
        for kode, barang in penyimpanan.items():
            print(f"kode: {kode}")
            print(f"nama: {barang['nama']}")
            print(f"jumlah: {barang['jumlah']}")
            print(f"harga: {barang['harga']}")
            print("\n")
    except:
        print("error")


#cari barang
def cari_barang():
    try:
        cari = int(input("masukkan kode barang yang ingin dicari: "))
        if cari in penyimpanan:
            barang = penyimpanan[cari]
            print(f"kode: {cari}")
            print(f"nama: {barang['nama']}")
            print(f"jumlah: {barang['jumlah']}")
            print(f"harga: {barang['harga']}")
            print("\n")
        else:
            print("barang tidak diitemukan")
    except:
        print(f"barang tidak ditemukan")


#update barang
def update_barang():
    try:
        kode = int(input("masukkan kode barang yang ingin diupdate: "))
        if kode in penyimpanan:
            barang = penyimpanan[kode]
            
            jumlah_baru = int(input("masukkan jumlah unit baru: "))
            harga_baru = int(input("masukkan harga baru: "))
            
            barang["jumlah"] = jumlah_baru
            barang["harga"] = harga_baru
            print(f"barang berhasil diupdate")
        else:
            print("barang tidak di temukan")
    except:
        print("barang gagal diupdate")



while True:
    print("\n")
    print("""=== menu inventory barang ===
1. tambah barang
2. hapus barang
3. tampilkan barang
4. cari barang
5. update barang
6. keluar
pilih opsi 1-6:""")

    opsi = int(input("pilih opsi: "))
    if opsi == 1:
        tambah_barang()
    elif  opsi == 2:
        hapus_barang()
    elif opsi == 3:
        tampilkan_barang()
    elif  opsi == 4:
        cari_barang()
    elif  opsi == 5:
        update_barang()
    elif  opsi == 6:
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang tersedia.")

