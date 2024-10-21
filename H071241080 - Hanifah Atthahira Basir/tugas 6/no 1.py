"""Membuat Program Inventory Barang Sederhana"""

# Inventory program menggunakan dictionary
gudang = {}


# Fungsi untuk menambah barang
def tambah():
    print("\nTambah Barang")
    
    while True: #input id
        try:
            id = int(input("Masukkan id barang atau 0 untuk kembali: "))  # id sebagai kunci utama
            if id == 0:
                return
            if id in gudang:
                print(f"Barang dengan id {id} sudah ada, silahkan isi dengan id berbeda")
                continue
            break
        except ValueError:
            print("Input tidak valid, silahkan masukkan angka")

    #input nama
    while True:
        nama = input("Masukkan nama barang atau 0 untuk kembali: ")  
        if nama == 0:
                return
        else:
            break
        
    while True: #input jumlah
        try:
            jumlah = int(input("Masukkan jumlah barang atau 0 untuk kembali: "))
            if jumlah == 0:
                return
            if jumlah < 0:
                print("Jumlah tidak boleh nol atau negatif")
                continue
            elif jumlah == 0:
                break
            break
        except ValueError:
            print("Input tidak valid, silahkan masukkan angka")
    
    while True: #input harga
        try:        
            harga = float(input("Masukkan harga barang atau 0 untuk kembali: "))
            if harga == 0:
                return
            if harga < 0:
                print("Harga tidak boleh nol atau negatif")
                continue
            elif harga == 0:
                break
            break
        except ValueError:
            print("Input tidak valid, silahkan masukkan angka")
                
    gudang[id] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
    print(f"Barang dengan id {id} berhasil ditambahkan\n")
    

# Fungsi untuk menghapus barang
def hapus():
    print("\nHapus Barang")
    
    if not gudang:  
        print("Gudang kosong, tidak ada barang yang dapat dihapus.")
        return
    
    while True:
        try:
            id = int(input("Masukkan id barang yang ingin dihapus atau 0 untuk kembali: "))
            if id == 0:
                return
            if id in gudang:
                del gudang[id]
                print(f"Barang dengan id {id} berhasil dihapus.")
                break
            else:
                print(f"Barang dengan id {id} tidak ditemukan dalam gudang.")
        except ValueError:
            print("Input tidak valid, silahkan masukkan angka")


# Fungsi untuk menampilkan daftar barang
def tampilkan():
    print("\nTampilkan Barang")
    
    if gudang:
        print("\nDaftar Barang di Gudang:")
        
        for id, data in gudang.items():
            print(f"id: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Gudang kosong, tidak ada barang yang dapat ditampilkan.")


# Fungsi untuk mencari barang berdasarkan id
def cari():
    print("\nCari Barang")
    
    if not gudang:  
        print("Gudang kosong, tidak ada barang yang dapat dicari.")
        return
    
    while True:
        try:
            id = int(input('Masukkan id barang yang ingin dicari atau 0 untuk berhenti: '))
            if id == 0:
                return
            if id in gudang:
                data = gudang[id]
                print(f"id: {id}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}\n")
                break
            elif id == 0:
                break
            else:
                print(f"Barang dengan id {id} tidak ditemukan.\n")
        except ValueError:
            print("Input tidak valid, silahkan masukkan angka.")
        continue
        
        
# Fungsi untuk mengupdate data barang
def update():
    print("\nUpdate Barang")
    
    if not gudang:  
        print("Gudang kosong, tidak ada barang yang dapat diupdate.")
        return
    
    while True:
        try:
            id = int(input("Masukkan id barang yang ingin diupdate atau 0 untuk berhenti: "))
            if id == 0:
                return
            elif id in gudang:
                while True: #nama baru
                    nama = input("Masukkan nama baru barang atau 0 untuk kembali: ")
                    if nama == 0:
                        return
                    break
                    
                while True: #jumlah baru
                    try:
                        jumlah = int(input("Masukkan jumlah baru barang atau 0 untuk kembali: "))
                        if jumlah == 0:
                            return
                        if jumlah < 0:
                            print("Jumlah tidak boleh nol atau negatif")
                            continue
                        break
                    except ValueError:
                        print("Input tidak valid, silahkan masukkan angka")

                while True: #harga baru
                    try:
                        harga = float(input("Masukkan harga baru barang atau 0 untuk kembali: "))
                        if harga == 0:
                            return  
                        if harga < 0:
                            print("Harga tidak boleh nol atau negatif")
                            continue
                        break
                    except ValueError:
                        print("Input tidak valid, silahkan masukkan angka")

                gudang[id] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
                print(f"Barang dengan id {id} berhasil diupdate.")
                break  
            
            else:
                print(f"Barang dengan id {id} tidak ditemukan dalam gudang.")
                break  
            
        except ValueError:
            print("Input tidak valid, silahkan masukkan angka")


# Menu utama
def menu():
    
    while True:
        print("\nMenu Gudang:")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            hapus()
        elif pilihan == '3':
            tampilkan()
        elif pilihan == '4':
            cari()
        elif pilihan == '5':
            update()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program inventory")
            break
        else:
            print("Pilihan tidak valid, silakan pilih dari menu diatas (1-6).")

# mulai program
menu()
