def menu():
    print("\n=== Menu Inventory Barang ===")
    print("1. Tambah barang")
    print("2. Hapus barang")
    print("3. Tampilkan barang")
    print("4. Cari barang")
    print("5. Update barang")
    print("6. Keluar")


def tambah_barang(inventory):
    while True:
        kode_barang =input("Masukkan Kode Barang (enter untuk kembali): ")
        if kode_barang in inventory:
            print(f"barang dengan kode barang {kode_barang} sudah ada, isi dengan  kode barang lain.")
            continue
        elif kode_barang=="":
            return
        elif not kode_barang.isnumeric():
            print("Kode barang harus berupa angka saja.")
            continue
        nama_barang = input("Masukkan nama barang: ")
        if nama_barang==0:
            return
        if not nama_barang.isalpha(): 
            print("Nama barang harus berupa huruf saja.")
            continue 

        try:
            jumlah = int(input("Masukkan jumlah barang: "))
            if jumlah==0:
              return
            harga_per_unit = float(input("Masukkan harga per unit: ")) 
            if harga_per_unit==0:
               return 
            break 
        except ValueError:
            print("Input tidak valid. Pastikan jumlah adalah angka bulat dan harga adalah angka desimal.")
    
    inventory[kode_barang] = {
        "nama": nama_barang,
        "jumlah": jumlah,
        "harga": harga_per_unit
    }
    print("Barang berhasil ditambahkan.")


def hapus_barang(inventory):
    if not inventory:
        print("Inventory kosong.")
        return
    while True:
        kode_barang = int(input("Masukkan kode barang yang ingin dihapus: "))
        if kode_barang ==0:
            return
        if kode_barang in inventory:
            del inventory[kode_barang]
            print(f"{kode_barang} telah dihapus dari inventory.")
            break
        elif kode_barang not in inventory:
            print(f"{kode_barang} tidak ditemukan dalam inventory. Coba lagi.")
            break


def tampilkan_barang(inventory):
    if not inventory:
        print("Inventory kosong.")
    else:
        for kode, detail in inventory.items():
            print(f"Kode: {kode}, Nama: {detail['nama']}, Jumlah: {detail['jumlah']}, Harga per unit: {detail['harga']}")
            

def cari_barang(inventory):
    if not inventory:
        print("Inventory kosong.")
        return
    while True:
        kode_barang = input("Masukkan kode barang yang ingin dicari: ")
        if kode_barang==0:
            return
        if kode_barang in inventory:
            detail = inventory[kode_barang]
            print(f"{kode_barang} ditemukan dengan nama: {detail['nama']}, jumlah: {detail['jumlah']}, dan harga per unit: {detail['harga']}")
            break
        else:
            print(f"{kode_barang} tidak ditemukan dalam inventory. Coba lagi.")
            break


def update_barang(inventory):
    if not inventory:
        print("Inventory kosong.")
        return
    while True:
        kode_barang = input("Masukkan kode barang yang ingin diupdate (atau enter untuk kembali): ")
        if kode_barang==0:
            return
        if kode_barang in inventory:
            try:
                jumlah_baru = int(input("Masukkan jumlah baru: "))
                if jumlah_baru==0:
                   return
                harga_baru = float(input("Masukkan harga per unit baru: "))
                if harga_baru==0:
                   return
                inventory[kode_barang]['jumlah'] = jumlah_baru
                inventory[kode_barang]['harga'] = harga_baru  
                print("Data barang berhasil diperbarui")
                break 
            except ValueError:
                print("Input tidak valid. Pastikan jumlah adalah angka bulat dan harga adalah angka desimal.")
        else:
            print(f"Kode {kode_barang} tidak ditemukan dalam inventory.")
            break

def main():
    inventory = {}

    while True:
        menu()
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_barang(inventory)
        elif pilihan == '2':
            hapus_barang(inventory)
        elif pilihan == '3':
            tampilkan_barang(inventory)
        elif pilihan == '4':
            cari_barang(inventory)
        elif pilihan == '5':
            update_barang(inventory)
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()