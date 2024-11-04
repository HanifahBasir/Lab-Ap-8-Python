import os
import time

#buat folder films
praktikum_7 = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7"
nama_films = "films"
path_folder_films = os.path.join(praktikum_7, nama_films)

#buat folder tickets
nama_tickets = "tickets"
path_folder_tickets = os.path.join(praktikum_7, nama_tickets)

try:
    os.makedirs(path_folder_films)
    os.makedirs(path_folder_tickets)
except FileExistsError:
    print(f"Folder {nama_films} sudah ada")
    print(f"Folder {nama_tickets} sudah ada")
    
#menu utama
def  menu_utama():


    
    #admin
    def admin():
        #tambah film
        def tambah_film():
            films = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\films"
 
            while True:
                judul = input("\n--- Tambah film ---\nMasukkan judul film yang ingin ditambah (atau enter untuk kembali): ")
                tambah = os.path.join(films,  judul)
                print(f"film {judul} berhasil ditambahkan")
                try:
                    if os.path.exists(tambah):
                        print(f"film {judul} sudah ada")
                        return
                    with open(tambah, "w") as w:
                        w.write(f"ini adalah film {judul}")
                except:
                    print("Gagal membuat folder film")
        #hapus film
        def hapus_film():
            films = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\films"

            films_list = os.listdir(films)
            print("\n--- Hapus film ---")
            for index, film in enumerate(films_list, start=1):
                print(f"{index}. {film}")
            judul = int(input("\nmasukkan nomor film yang ingin dihapus (atau enter untuk kembali): "))
            if 1 <= judul <= len(films_list):
                try:
                    os.remove(os.path.join(films, films_list[judul - 1]))  # Menggunakan judul yang benar
                    print(f"film {films_list[judul - 1]} berhasil dihapus")
                except:
                    print("Gagal menghapus folder film")
            else:
                print("gagal menghapus film")
        #daftar tiket
        def daftar_tiket():
            #lihat daftar tiket
            def lihat_daftar_tiket():
 
                tickets = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\tickets"
                tickets_list = os.listdir(tickets)
                try:
                    if not tickets_list:
                        print("belum ada tiket")
                    else:
                        for index, tiket in enumerate(tickets_list, start=1):
                            print(f"\n{index}. {tiket}")
                except:
                    print("Gagal menampilkan daftar tiket")
            #lihat detail tiket
            def lihat_detail_tiket():

                tickets = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\tickets"
                tickets_list = os.listdir(tickets)
                try:
                    if not tickets_list:
                        print("Belum ada tiket")
                    else:
                        for index, tiket in enumerate(tickets_list, start=1):
                            print(f"\n{index}. {tiket}")
                        pilih_tiket = int(input("\npilih nomor tiket untuk menampilkan detailnya: "))
                        if 1 <= pilih_tiket  <= len(tickets_list):
                            try:
                                with open((os.path.join(tickets, tickets_list[pilih_tiket - 1])), "r") as r:
                                    print(r.read())
                            except Exception as e:
                                print(f"gagal membuka file tiket: {e}")
                        else:
                            print("pilihan tidak ada")
                except:
                    print("Gagal menampilkan detail tiket")
                        
            #hapus tiket
            def hapus_tiket():

                tickets = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\tickets"
                while True:
                    tickets_list = os.listdir(tickets)
                    try:
                        if not tickets_list:
                            print("tidak ada tiket yang bisa dihapus")
                            break
                        else:
                            print("\n--- tiket ---")
                            for index, tiket in enumerate(tickets_list, start=1):
                                print(f"{index}. {tiket}")
                            pilih_hapus = int(input("\npilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
                            if 1 <= pilih_hapus <= len(tickets_list):
                                os.remove(os.path.join(tickets, tickets_list[pilih_hapus - 1]))
                                print("tiket berhasil dihapus")
                            elif pilih_hapus == 0:
                                break
                            else:
                                print("nomor tiket tidak ditemukan")
                    except:
                        print("Gagal menghapus tiket")
                
            while True:
                print("\n--- daftar tiket ---")
                print("1. lihat daftar tiket")
                print("2. lihat detail tiket")
                print("3. hapus tiket")
                print("4. kembali")
                pilih_opsi_daftar_tiket = int(input("pilih opsi 1/2/3/4: "))
                if  pilih_opsi_daftar_tiket == 1:
                    lihat_daftar_tiket()
                elif  pilih_opsi_daftar_tiket == 2:
                    lihat_detail_tiket()
                elif   pilih_opsi_daftar_tiket == 3:
                    hapus_tiket()
                elif   pilih_opsi_daftar_tiket == 4:
                    admin()
                else:
                    print("pilih opsi yang sesuai")
            
        while True:
            print("\n-- Menu Admin --")
            print("1. Tambah Film")
            print("2. Hapus film")
            print("3. daftar tiket")
            print("4. kembali")
            pilih_opsi = int(input("pilih opsi 1/2/3/4: "))
            if pilih_opsi == 1:
                tambah_film()
            elif pilih_opsi == 2:
                hapus_film()
            elif pilih_opsi == 3:
                daftar_tiket()
            elif pilih_opsi == 4:
                menu_utama()
            else:
                print("pilih sesuai opsi")

    #pengunjung
    def pengunjung():
        #lihat daftar film
        def lihat_daftar_film():
            films = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\films"


            films_list = os.listdir(films)
            try:
                if not films_list:
                    print("belum ada film")
                else:
                    print("\n--- daftar film ---")
                    for index, film in enumerate(films_list, start=1):
                        print(f"{index}. {film} ")
            except:
                print("gagal menampilkan film")
        #beli tiket
        def beli_tiket():
            films = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\films"
            tickets = r"D:\TUGAS LAB\tugas algoritma lab\Lab-Ap-8-Python\H071241065 - Akmal\praktikum-7\tickets"
            films_list = os.listdir(films)
            id_tiket = "TICK"
            time_sekarang = time.localtime()
            format_waktu = time.strftime("%d%m%Y%H%M%S", time_sekarang)
            nama_tiket = id_tiket + format_waktu
            films_list = os.listdir(films)
            try:
                if not films_list:
                    print("belum ada film")
                else:
                    print("\n--- daftar film ---")
                    for index, film in enumerate(films_list, start=1):
                        print(f"{index}. {film} ")
                    nomor_tiket = int(input("pilih nomor film untuk beli tiketnya (atau enter untuk kembali): "))
                    if 1 <= nomor_tiket <= len(films_list):  # Memeriksa apakah nomor_tiket valid
                        hias = "-" * 36 # Mendapatkan judul film yang dipilih
                        join = os.path.join(tickets, nama_tiket)
                        with open(join, "w") as f:
                            f.write(hias)
                            f.write("\n|          TIKET BIOSKOP           |")
                            f.write(f"\n{hias}")
                            f.write(f"\nID Tiket  : {nama_tiket}")
                            f.write(f"\nFilm      : {film}")
                            f.write(f"\nTanggal   : {time.strftime("%d-%m-%Y", time_sekarang)}")
                            f.write(f"\n{hias}")  # Menambahkan garis pemisah di bawah tiket
                        print(f"tiket berhasil dibeli. ID ttiket anda {nama_tiket}\nFile tiket telah dibuat: tickets/{nama_tiket}")
                    else:
                        print("nomor tiket yang anda masukkan salah")
            except:  # Menangkap semua exception dan mencetak pesan kesalahan
                print("kembali ke menu pengunjung")

        while True:
            print("\n--- Menu pengujung ---")
            print("1. lihat daftar film")
            print("2. beli tiket")
            print("3. kembali")
            pilih_opsi = int(input("pilih opsi 1/2/3: "))
            if  pilih_opsi == 1:
                lihat_daftar_film()
            elif  pilih_opsi == 2:
                beli_tiket()
            elif   pilih_opsi == 3:
                menu_utama()
            else:
                print("pilih sesuai opsi")


    while True:
        print("\n--- Menu Utama ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilih_opsi = int(input("pilih opsi 1/2/3: "))
        if  pilih_opsi == 1:
            admin()
        elif pilih_opsi == 2:
            pengunjung()
        elif  pilih_opsi == 3:
            print("Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            print("pilih sesuai opsi")
menu_utama()



