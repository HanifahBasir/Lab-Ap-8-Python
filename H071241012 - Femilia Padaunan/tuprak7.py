import datetime
import os

DAFTAR_FILM_FILE = 'daftar_film.txt'
DAFTAR_TIKET_FOLDER = 'tiket_folder'

# Pastikan folder untuk tiket ada
if not os.path.exists(DAFTAR_TIKET_FOLDER):
    os.makedirs(DAFTAR_TIKET_FOLDER)

def detail_tiket(ticket_id, film_name, date):
    return f"""
    +--------------------------------------+
    |          TIKET BIOSKOP               |
    +--------------------------------------+
    | ID Tiket : {ticket_id}  |
    | Film     : {film_name}  |
    | Tanggal  : {date}       |
    +--------------------------------------+
    |    Terima kasih telah membeli        |
    |           tiket Anda!                |
    +--------------------------------------+
    """

def load_daftar_film():
    """Memuat daftar film dari file."""
    daftar_film = []
    if os.path.exists(DAFTAR_FILM_FILE):
        with open(DAFTAR_FILM_FILE, 'r') as file:
            for line in file:
                nama_film = line.strip()
                daftar_film.append(nama_film)
    return daftar_film

def save_daftar_film(daftar_film):
    """Menyimpan daftar film ke file."""
    with open(DAFTAR_FILM_FILE, 'w') as file:
        for nama in daftar_film:
            file.write(f"{nama}\n")

daftar_film = load_daftar_film()
daftar_tiket = {}

def tambah_film():
    while True:
        print("\n--- Tambah Film ---")
        nama_film = input("Masukkan Nama Film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
        if not nama_film:
            print("\nKembali ke Menu Admin")
            break
        daftar_film.append(nama_film)
        save_daftar_film(daftar_film)
        print(f"Film '{nama_film}' berhasil ditambahkan.")

def hapus_film():
    while True:
        print("--- Hapus Film ---")
        lihat_daftar_film() 
        
        if not daftar_film:
            print("Tidak ada film yang tersedia untuk dihapus.")
            break

        nama_film = input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")

        if nama_film == '0':
            print("\n---- Kembali ke Menu Admin ----")
            break
        
        try:
            index = int(nama_film) - 1  
            if 0 <= index < len(daftar_film):
                film_yang_hapus = daftar_film[index]
                tiket_yang_dihapus = [ticket_id for ticket_id, film_name in daftar_tiket.items() if film_name == film_yang_hapus]
                for ticket_id in tiket_yang_dihapus:
                    ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
                    if os.path.exists(ticket_file_path):
                        os.remove(ticket_file_path)
                        print(f"Tiket dengan ID {ticket_id} telah dihapus.")
                
                daftar_film.remove(film_yang_hapus)
                save_daftar_film(daftar_film)
                
                print(f"Film '{film_yang_hapus}' berhasil dihapus.")
                
                if not daftar_film:
                    print("\nDaftar film kosong.")
                    break
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor film yang benar.")


def lihat_daftar_film():
    if not daftar_film:
        print("0.kembali")
        print("Daftar film kosong.")
        return
    print("\nDaftar Film:")
    for index, nama in enumerate(daftar_film, start=1):
        print(f"{index}. {nama}")
    print("0. Kembali")

        
import datetime

def beli_tiket():
    while True:
        print("\n--- Beli Tiket ---")
        lihat_daftar_film()
        nomor_film = input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ")

        if nomor_film == '0':
            break 

        try:
            index = int(nomor_film) - 1  # Mengonversi input ke indeks
            if 0 <= index < len(daftar_film):
                film_yang_dipilih = daftar_film[index]
                
                # Membeli tiket
                ticket_id = generate_ticket_id()
                date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
                daftar_tiket[ticket_id] = film_yang_dipilih
                simpan_informasi_tiket(ticket_id, film_yang_dipilih, date)
                
                # Menampilkan informasi tiket
                print(f"Tiket berhasil dibeli! ID Tiket Anda: {ticket_id}")
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor film yang benar.")

        

def simpan_informasi_tiket(ticket_id, nama_film, date):
    """Menyimpan informasi tiket ke file dalam folder tiket."""
    ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
    with open(ticket_file_path, "w") as file:
        file.write(detail_tiket(ticket_id, nama_film, date))
        print(f"file tiket telah dibuat: {ticket_file_path}.")

def hapus_tiket():
    tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
    for index, ticket_file in enumerate(tiket_files, start=1):
            ticket_id = ticket_file.split('.')[0]
            print(f"{index}. {ticket_id}")
            print("0. Kembali")

            ticket_index = int(input("Masukkan nomor tiket yang ingin dihapus(atau 0 untuk kembali): ")) - 1
            if 0 <= ticket_index < len(tiket_files):
                ticket_id = tiket_files[ticket_index].split('.')[0]
                ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
                os.remove(ticket_file_path)
                print(f"Tiket dengan ID {ticket_id} telah dihapus.")
        
            else:
                print("Nomor tiket tidak valid.")



def tampilkan_daftar_tiket():
    while True:
        print("\n----Daftar Tiket----")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            lihat_daftar_film()
            print("\nDaftar Tiket:")
            tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
            for index, ticket_file in enumerate(tiket_files, start=1):
                ticket_id = ticket_file.split('.')[0]
                print(f"{index}. {ticket_id}")
            print("0. kembali")
                

        elif pilihan == '2':
            print("\n----Detail Tiket----:")
            print("\Daftar Tiket:")
            tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
            for index, ticket_file in enumerate(tiket_files, start=1):
                ticket_id = ticket_file.split('.')[0]
                print(f"{index}. {ticket_id}")
            print("0. Kembali ke daftar tiket")
            ticket_index = int(input("pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ")) - 1
            if 0 <= ticket_index < len(tiket_files):
                ticket_id = tiket_files[ticket_index].split('.')[0]
                ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
                with open(ticket_file_path, 'r') as file:
                    print("\nDetail Tiket: ")
                    print(file.read())
            else:
                print("Nomor tiket tidak valid.")

        elif pilihan == '3':
            print("\nDaftar Tiket:")
            tiket_files = os.listdir(DAFTAR_TIKET_FOLDER)
            for index, ticket_file in enumerate(tiket_files, start=1):
                ticket_id = ticket_file.split('.')[0]
                print(f"{index}. {ticket_id}")
            print("0. Kembali")

            ticket_index = int(input("Masukkan nomor tiket yang ingin dihapus(atau 0 untuk kembali): ")) - 1
            if 0 <= ticket_index < len(tiket_files):
                ticket_id = tiket_files[ticket_index].split('.')[0]
                ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
                os.remove(ticket_file_path)
                print(f"Tiket dengan ID {ticket_id} telah dihapus.")
        
            else:
                print("Nomor tiket tidak valid.")

        elif pilihan == '4':
            break 

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def lihat_detail_tiket():
    while True:
        ticket_id = input("Masukkan nomor Tiket yang ingin dilihat (atau 0 untuk kembali): ")
        ticket_file_path = os.path.join(DAFTAR_TIKET_FOLDER, f"{ticket_id}.txt")
        if os.path.exists(ticket_file_path):
            with open(ticket_file_path, 'r') as file:
                print(file.read())
        else:
            print("ID Tiket tidak ditemukan.")

        

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

        try:
            if pilihan == '1':
                tambah_film()
            elif pilihan == '2':
                hapus_film()
            elif pilihan == '3':
                tampilkan_daftar_tiket()
            elif pilihan == '4':
                print("Kembali ke menu utama.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def menu_pengunjung():
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. lihat Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")
        pilihan = input("Pilih opsi (1/2/3): ")

        try:
            if pilihan == '1':
                lihat_daftar_film()
            elif pilihan == '2':
                beli_tiket()
            elif pilihan == '3':
                print("Kembali ke Menu Utama.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

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

