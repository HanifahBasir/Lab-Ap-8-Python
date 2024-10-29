"""Sistem Informasi Bioskop"""

import os
from datetime import datetime

# Inisialisasi daftar film dan tiket
daftar_film = []
daftar_tiket = []

# Fungsi untuk admin: Tambah film
def tambah_film():
    print("\n=== Tambah Film ===")
    nama_film = input("Masukkan nama film yang ingin ditambahkan (enter untuk kembali): ")
    if nama_film == "":
        print("Kembali")
        return
    else:
        if not os.path.exists("Film"):
            os.makedirs("Film")
        File = os.path.join("Film", f"{nama_film}.txt")
        with open(File, "w") as file:
            file.write(nama_film+"\n")
        print(f"Film dengan judul {nama_film} berhasil ditambahkan")
   

    
def hapus_film():
    if not os.path.exists("Film"):
        print("\nTidak ada film yang tersedia.")
        return

    print("\n=== Hapus Film ===")
    tampilkan_daftar_film()
    
    try:
        nomor_film = int(input("Masukkan nomor film yang ingin dihapus (0 untuk kembali): "))
        if nomor_film == 0:
            print("Kembali")
            return
        elif 1 <= nomor_film <= len(daftar_film):
            film_dihapus = daftar_film.pop(nomor_film - 1)  # Hapus dari daftar
            os.remove(os.path.join("Film", f"{film_dihapus}.txt"))  # Hapus file
            print(f"Film '{film_dihapus}' berhasil dihapus\n")
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")
    
    # Muat ulang daftar film setelah penghapusan
    muat_daftar_film()

        
# Fungsi untuk menampilkan daftar film
def tampilkan_daftar_film():
    if not os.path.exists("Film"):
        print("\nBelum ada film yang tersedia.")
        return
    daftar_film = os.listdir("Film")  
    if not daftar_film:
        print("\nBelum ada film yang tersedia.")
        return
    
    print("\n=== Daftar Film ===")
    for i, film in enumerate(daftar_film):
        print(f"{i + 1}. {film}")
    print()
    
# Fungsi untuk memuat ulang daftar film dari folder "Film"
def muat_daftar_film():
    global daftar_film
    daftar_film = []
    if os.path.exists("Film"):
        for file in os.listdir("Film"):
            if file.endswith(".txt"):
                # Ambil nama film dari nama file (tanpa ".txt")
                nama_film = file[:-4]
                daftar_film.append(nama_film)
    else:
        os.makedirs("Film")  # Buat folder "Film" jika belum ada

# Fungsi pembelian tiket
def beli_tiket():
    muat_daftar_film()  # Pastikan daftar film selalu diperbarui
    
    if not daftar_film:
        print("\nBelum ada film yang tersedia.")
        return
    
    tampilkan_daftar_film()  # Tampilkan daftar film ke pengguna
    
    try:
        nomor_film = int(input("Masukkan nomor film yang ingin dibeli tiketnya (0 untuk kembali): "))
        if nomor_film == 0:  
            print("Kembali")
            return
        if 1 <= nomor_film <= len(daftar_film):
            film_dipilih = daftar_film[nomor_film - 1]
            Waktu = datetime.now().strftime("%d%m%Y%H%M%S")
            Tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            id_tiket = f"TICK{Waktu}"

            # Format tampilan tiket
            tiket = f"""
+-------------------------------------+
|            TIKET BIOSKOP            |
+-------------------------------------+
| ID Tiket : {id_tiket}       |
| Film     : {film_dipilih}             |
| Tanggal  : {Tanggal}      |
+-------------------------------------+
|            Terima kasih!            |
+-------------------------------------+
"""
            # Pastikan direktori untuk menyimpan tiket sudah ada
            if not os.path.exists("Tiket"):
                os.makedirs("Tiket")
            
            # Simpan tiket ke dalam file dengan detail lengkap
            file_tiket = os.path.join("Tiket", f"{id_tiket}.txt")
            with open(file_tiket, "w") as file:
                file.write(tiket)
                
            # Tampilkan konfirmasi pembelian ke layar
            print(f"Tiket berhasil dibeli untuk film '{film_dipilih}'")
            print(f"ID tiket: {id_tiket}")

            
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")


# Fungsi untuk admin: Tampilkan daftar tiket
def tampilkan_daftar_tiket():
    if not os.path.exists("Tiket"):
        print("\nBelum ada tiket yang terjual.")
        return
    daftar_tiket = os.listdir("Tiket")  # Ambil semua file dalam folder "Tiket"
    if not daftar_tiket:
        print("\nBelum ada tiket yang terjual.")
        return
    print("\n=== Daftar Tiket ===")
    for i, id_tiket in enumerate(daftar_tiket):
        print(f"{i + 1}.{id_tiket}")
print()


# Fungsi untuk admin: Tampilkan detail tiket
def tampilkan_detail_tiket():
    if not os.path.exists("Tiket"):
        print("\nBelum ada tiket yang terjual.")
        return

    daftar_tiket = os.listdir("Tiket")  # Ambil semua file dalam folder "Tiket"
    if not daftar_tiket:
        print("\nBelum ada tiket yang terjual.")
        return

    print("\n=== Detail Tiket ===")
    tampilkan_daftar_tiket()  # Tampilkan daftar tiket untuk memilih

    try:
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dilihat detailnya (0 untuk kembali): "))
        if nomor_tiket == 0:
            print("Kembali")
            return
        if 1 <= nomor_tiket <= len(daftar_tiket):
            # Ambil nama file tiket berdasarkan pilihan pengguna
            tiket_file = daftar_tiket[nomor_tiket - 1]
            tiket_path = os.path.join("Tiket", tiket_file)

            # Buka dan baca isi file tiket untuk menampilkan detail
            with open(tiket_path, "r") as file:
                isi_tiket = file.read()
            
            print("\n=== Detail Tiket ===")
            print(isi_tiket)  # Tampilkan isi lengkap tiket
        else:
            print("Nomor tiket tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

# Fungsi untuk admin: Hapus tiket
def hapus_tiket():
    if not os.path.exists("Tiket"):
        print("\nBelum ada tiket yang terjual.")
        return
    
    daftar_tiket = os.listdir("Tiket")  # Ambil semua file dalam folder "Tiket"
    if not daftar_tiket:
        print("\nBelum ada tiket yang terjual.")
        return
    
    print("\n=== Hapus Tiket ===")
    tampilkan_daftar_tiket()
    
    try:
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dihapus (0 untuk kembali): "))
        if nomor_tiket == 0:
            print("Kembali")
            return
        elif 1 <= nomor_tiket <= len(daftar_tiket):
            tiket_dihapus = daftar_tiket[nomor_tiket - 1]
            file_tiket = os.path.join("Tiket", tiket_dihapus)
            os.remove(file_tiket)  # Hapus file tiket dari sistem
            print(f"Tiket dengan ID '{tiket_dihapus}' berhasil dihapus\n")
        else:
            print("Nomor tiket tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

    
# Menu untuk admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Tampilkan Daftar Film")
        print("4. Tampilkan Daftar Tiket")
        print("5. Tampilkan Detail Tiket")
        print("6. Hapus Tiket")
        print("7. Keluar dari menu admin")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tambah_film()
        elif pilihan == "2":
            hapus_film()
        elif pilihan == "3":
            tampilkan_daftar_film()
        elif pilihan == "4":
            tampilkan_daftar_tiket()
        elif pilihan == "5":
            tampilkan_detail_tiket()
        elif pilihan == "6":
            hapus_tiket()
        elif pilihan == "7":
            break
        else:
            print("Opsi tidak valid")

# Menu untuk pengunjung
def menu_pengunjung():
    while True:
        print("\n=== Menu Pengunjung ===")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("3. Keluar dari menu pengunjung")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tampilkan_daftar_film()
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            break
        else:
            ("Opsi tidak valid")

# Menu utama
def main_menu():
    while True:
        print("\n=== Sistem Manajemen Bioskop ===")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar dari Program")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            menu_pengunjung()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem manajemen bioskop.")
            break
        else:
            print("Opsi tidak valid")

# Fungsi untuk memuat daftar film dari file
def muat_daftar_film():
    if not os.path.exists("Film"):
        os.makedirs("Film")
    global daftar_film
    daftar_film = []
    for file in os.listdir("Film"):
        if file.endswith(".txt"):
            with open(os.path.join("Film", file), "r") as f:
                daftar_film.append(f.readline().strip())

# Jalankan program
if __name__ == "__main__":
    main_menu()
