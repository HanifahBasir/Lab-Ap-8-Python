import datetime
import os

DAFTAR_FILM_FILE = 'daftar_film.txt'
DAFTAR_TIKET_FOLDER = 'tiket_folder'

if not os.path.exists(DAFTAR_TIKET_FOLDER):
    os.makedirs(DAFTAR_TIKET_FOLDER)

def detail_tiket(ticket_id, film_name, date):
    return f"""
    +--------------------------------------+
    |          TIKET BIOSKOP               |
    +--------------------------------------+
    | ID Tiket : {ticket_id:<25}|
    | Film     : {film_name:<25}|
    | Tanggal  : {date:<25}|
    +--------------------------------------+
    |    Terima kasih telah membeli        |
    |           tiket Anda!                |
    +--------------------------------------+
    """

def mengisi_daftar_film():
    daftar_film = []
    if os.path.exists(DAFTAR_FILM_FILE):
        with open(DAFTAR_FILM_FILE, 'r') as file:
            for line in file:
                nama_film = line.strip()
                daftar_film.append(nama_film)
    return daftar_film

def simpan_daftar_film(daftar_film):
    with open(DAFTAR_FILM_FILE, 'w') as file:
        for nama in daftar_film:
            file.write(f"{nama}\n")

daftar_film = mengisi_daftar_film()
daftar_tiket = {}

def tambah_film():
     while True:
        print("\n--- Tambah Film ---")
        nama_film = input("Masukkan Nama Film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
        if not nama_film:
            print("\nKembali ke Menu Admin")
            break
        daftar_film.append(nama_film)
        simpan_daftar_film(daftar_film)
        print(f"Film '{nama_film}' berhasil ditambahkan.")

def hapus_film():
    while True:
        print("\nDaftar Film:")
        if daftar_film:
            for i, film in enumerate(daftar_film, start=1):
                print(f"{i}. {film}")
        else:
            print("Daftar film kosong.")
        
        print("0. Kembali")
        
        nama_film = input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")

        if nama_film == '0':
            print("\nKembali ke menu Admin")
            break

        try:
            index = int(nama_film) - 1
            if 0 <= index < len(daftar_film):
                film_yang_hapus = daftar_film.pop(index)
                simpan_daftar_film(daftar_film)

                # jadi kak, pada baris ini mencari daftar file tiket yang ada di folder tiket
                tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
               # pada baris ini memeriksa apakah file tersebut ada dalam tiket dalam folder
                for ticket_file in tiket_files:
                    # untuk variabel ini kak, ia menyimpan path lengkap dari setiap tiket yang ada dalam folder kita dan memungkinkan kode mengakses file ini secara langsung
                    ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, ticket_file)
                    # untuk kode ini ia membuka file tiket agar isinya dapat dibaca 'r'
                    with open(ticket_file_path, 'r') as file:
                        content = file.read()  # untuk kode ini kak, tugasnya menyimpan isi file ke dalam variabel "content" untuk dapat diperiksa

                    # kode ini kak, mengecek apakah nama film yang akan dihapus ada dalam isi file
                    if film_yang_hapus in content:
                        # kode ini bertugas menghapus file tiket, jika tiket tersebut terkait dengan film yang akan dihapus
                        os.remove(ticket_file_path)
                        print(f"Tiket terkait film '{film_yang_hapus}' berhasil dihapus: {ticket_file_path}")
                # kalau kode ini kak, memberikan informasi bahwa film dan tiket yang terkait telah berhasil di hapus
                print(f"\nFilm '{film_yang_hapus}' dan tiket terkait berhasil dihapus.")
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor film yang benar.")

def lihat_daftar_film():
    if not daftar_film:
        print("Daftar film kosong.")
        return
    print("\nDaftar Film:")
    for index, nama in enumerate(daftar_film, start=1):
        print(f"{index}. {nama}")
    print("0. Kembali")

def beli_tiket():
    while True:
        print("\n--- Beli Tiket ---")
        lihat_daftar_film()
        nomor_film = input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ")

        if nomor_film == '0':
            print("\nKembali ke menu Pengunjung")
            break 

        try:
            index = int(nomor_film) - 1 
            if 0 <= index < len(daftar_film):
                film_yang_dipilih = daftar_film[index]
                
                # Membeli tiket
                ticket_id = generate_ticket_id()
                date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
                daftar_tiket[ticket_id] = film_yang_dipilih
                simpan_informasi_tiket(ticket_id, film_yang_dipilih, date)
                
                
                print(f"Tiket berhasil dibeli! ID Tiket Anda: {ticket_id}")
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor film yang benar.")

def simpan_informasi_tiket(ticket_id, nama_film, date):
    ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
    with open(ticket_file_path, "w") as file:
        file.write(detail_tiket(ticket_id, nama_film, date))
        print(f"file tiket telah dibuat: {ticket_file_path}.")

def tampilkan_daftar_tiket():
    while True:
        print("\n----Daftar Tiket----")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
            for index, ticket_file in enumerate(tiket_files, start=1):
                ticket_id = ticket_file.split('.')[0]
                print(f"{index}. {ticket_id}")

        elif pilihan == '2':
            print("Detai Tiket: ")
            tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
            for index, ticket_file in enumerate(tiket_files, start=1):
                ticket_id = ticket_file.split('.')[0]
                print(f"{index}. {ticket_id}")
            print("0. Kembali ke daftar tiket")

            try:
                ticket_index = int(input("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ")) - 1
                if ticket_index == -1:
                    break

                if 0 <= ticket_index < len(tiket_files):
                    ticket_id = tiket_files[ticket_index].split('.')[0]
                    ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
                    with open(ticket_file_path, 'r') as file:
                        print("\nDetail Tiket:")
                        print(file.read())
                else:
                    print("Nomor tiket tidak valid.")
            except ValueError:
                print("Input tidak valid.")

        elif pilihan == '3':
            tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
            for index, ticket_file in enumerate(tiket_files, start=1):
                ticket_id = ticket_file.split('.')[0]
                print(f"{index}. {ticket_id}")
            print("0. Kembali")

            try:
                ticket_index = int(input("Masukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): ")) - 1
                if ticket_index == -1:
                    continue

                if 0 <= ticket_index < len(tiket_files):
                    ticket_id = tiket_files[ticket_index].split('.')[0]
                    ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
                    os.remove(ticket_file_path)
                    print(f"Tiket dengan ID {ticket_id} telah dihapus.")
                else:
                    print("Nomor tiket tidak valid.")
            except ValueError:
                print("Input tidak valid.")

        elif pilihan == '4':
            print("\nKembali ke menu Admin")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def generate_ticket_id():
    now = datetime.datetime.now()
    return f"TICKET{now.strftime('%d%m%Y%H%M%S')}"

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            tambah_film()
        elif pilihan == '2':
            hapus_film()
        elif pilihan == '3':
            tampilkan_daftar_tiket()
        elif pilihan == '4':
            print("\nKembali ke menu Utama")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_pengunjung():  
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. Lihat Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            lihat_daftar_film()
        elif pilihan == '2':
            beli_tiket()
        elif pilihan == '3':
            print("\nKembali ke menu Utama")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def run():
    while True:
        print("\n--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        elif pilihan == '3':
            print("Terima Kasih Telah Menggunakan Sistem ini")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    run()
