inventory = {}
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Data Barang")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_daftar_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program inventori.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def tambah_barang():
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    try:
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        harga_barang = float(input("Masukkan harga barang: "))
        inventory[kode_barang] = {"nama":nama_barang,"kode": kode_barang,"jumlah": jumlah_barang, "harga": harga_barang}
        print(f"Barang berhasil ditambahkan.")
    except ValueError:
        print("input yang anda masukkkan tidak valid.Tolong masukkan angka")

def hapus_barang():
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    if kode_barang in inventory:
        del inventory[kode_barang]
        print(f"Barang berhasil dihapus.")
    else:
        print(f"Barang tidak ditemukan.")

def tampilkan_daftar_barang():
    if not inventory:
        print("Inventori kosong.")
    else:
        for kode_barang,info_barang in inventory.items():
            print(f"Kode: {info_barang['kode']}, Nama: {info_barang['nama']}, Jumlah: {info_barang['jumlah']}, Harga per unit: {info_barang['harga']:.1f}")

def cari_barang():
    print("Cari berdasarkan (1) Kode atau (2) Nama:")
    pilihan_cari = input("Masukkan pilihan (1/2): ")

    if pilihan_cari == "1":
        kode_input = input("Masukkan kode barang yang ingin dicari: ")
        found = False
        for kode_barang, info_barang in inventory.items():
            if info_barang['kode'] == kode_input:
                found = True
                print(f"Kode: {info_barang['kode']}, Nama: {info_barang['nama']}, Jumlah: {info_barang['jumlah']}, Harga per unit: {info_barang['harga']:.1f}")
                break
        if not found:
            print(f"Barang dengan kode {kode_input} tidak ditemukan.")
    
    elif pilihan_cari == "2":
        nama_barang = input("Masukkan nama barang yang ingin dicari: ")
        found = False
        for info_barang in inventory.values():
            if info_barang['nama'] == nama_barang:
                found = True
                print(f"Kode: {info_barang['kode']}, Nama: {info_barang['nama']}, Jumlah: {info_barang['jumlah']}, Harga per unit: {info_barang['harga']:.1f}")
                break
        if not found:
            print(f"Barang dengan nama {nama_barang} tidak ditemukan.")
def update_barang():
    kode_barang = input("Masukkan kode barang: ")
    if kode_barang in inventory:
            try:  
                jumlah_barang = int(input("Masukkan jumlah baru: "))
                while True:
                    harga_barang = input("Masukkan harga per unit: ")
                    if harga_barang.lower() == "kembali":
                        jumlah_barang = int(input("Masukkan jumlah baru: "))
                        continue
                    try:
                        harga_barang = float(harga_barang)
                        inventory[kode_barang]["jumlah"] = jumlah_barang
                        inventory[kode_barang]["harga"] = harga_barang
                        print(f"Data barang berhasil diperbarui.")
                        break
                    except ValueError:
                        print("Input tidak valid.Tolong masukkakn anggka")

            except ValueError:
                print("Input tidak valid.Tolong masukkakn anggka")
            return
    else:
        print(f"Barang tidak ditemukan.")
   
if __name__ == "__main__":
    main()