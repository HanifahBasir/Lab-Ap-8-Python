import os
from datetime import datetime

# const
FILM_DIR = 'films'
MOVIE_FILE = os.path.join(FILM_DIR, 'movies.txt')
TICKET_DIR = 'tickets'
TICKET_HISTORY_FILE = 'ticket_history.txt'

os.system('cls')

def cetak_pembatas():
    print('=' * 60)

def simpan_film(films):
    with open(MOVIE_FILE, 'w') as file:
        for film in films:
            file.write(f'{film}\n')

def muat_film():
    if not os.path.exists(MOVIE_FILE):
        return []
    with open(MOVIE_FILE, 'r') as file:
        films = [line.strip() for line in file.readlines()]
    return films

def tambah_film():
    films = muat_film()
    cetak_pembatas()

    film_baru = input('Masukkan judul film baru \t: ')
    films.append(film_baru)
    simpan_film(films)
    cetak_pembatas()
    print(f'Film "{film_baru}" telah ditambahkan.')
    cetak_pembatas()

def tampilkan_film(films=None):
    '''Fungsi untuk menampilkan daftar film'''
    if films is None:
        films = muat_film()
    cetak_pembatas()
    print(f'{'Daftar Film Tersedia':^60}')
    cetak_pembatas()
    if not films:
        print('Tidak ada film yang tersedia.')
    else:
        for idx, film in enumerate(films, start=1):
            print(f'{idx}. {film}')
    cetak_pembatas()

def hapus_film():
    films = muat_film()
    cetak_pembatas()

    if not films:
        print('Tidak ada film yang tersedia untuk dihapus.')
        return
    tampilkan_film(films)
    try:
        indeks = int(input('Masukkan nomor film yang akan dihapus \t: ')) - 1
        if 0 <= indeks < len(films):
            film_dihapus = films.pop(indeks)
            simpan_film(films)
            cetak_pembatas()
            print(f'Film "{film_dihapus}" telah dihapus.')
            cetak_pembatas()
        else:
            print('Nomor film tidak valid.')
    except ValueError:
        print('Input harus berupa angka.')

def buat_id_tiket():
    waktu_sekarang = datetime.now()
    id_tiket = waktu_sekarang.strftime('TICK%d%m%Y%H%M%S')
    return id_tiket

def simpan_tiket(id_tiket, nama_film):
    if not os.path.exists(TICKET_DIR):
        os.makedirs(TICKET_DIR)
    waktu_transaksi = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    # tiket_info = f'ID Tiket\t: {id_tiket}\nFilm\t: {nama_film}\nWaktu Beli\t: {waktu_transaksi}\n'
    tiket_info = (
        '+-----------------------------------------+\n'
        '|              TIKET BIOSKOP              |\n'
        '+-----------------------------------------+\n'
        f'| ID Tiket : {id_tiket}\t\t\t  |\n'
        f'| Film     : {nama_film} |\n'
        f'| Tanggal  : {waktu_transaksi}          |\n'
        '+-----------------------------------------+\n'
        '|       Terima kasih telah membeli        |\n'
        '|              tiket Anda!                |\n'
        '+-----------------------------------------+\n'
    )
    with open(os.path.join(TICKET_DIR, f'{id_tiket}.txt'), 'w') as file:
        file.write(tiket_info)

    with open(TICKET_HISTORY_FILE, 'a') as history_file:
        history_file.write(f'{id_tiket},{nama_film},{waktu_transaksi}\n')

def beli_tiket():
    films = muat_film()
    if not films:
        cetak_pembatas()
        print('Maaf, tidak ada film yang tersedia untuk saat ini.')
        return
    tampilkan_film(films)
    try:
        indeks = int(input('Pilih nomor film yang ingin dibeli tiketnya \t: ')) - 1
        if 0 <= indeks < len(films):
            nama_film = films[indeks]
            id_tiket = buat_id_tiket()
            simpan_tiket(id_tiket, nama_film)
            cetak_pembatas()
            print(f'Tiket untuk film "{nama_film}" berhasil dibeli.')
            print(f'ID Tiket Anda: {id_tiket}')
            cetak_pembatas()
        else:
            print('Nomor film tidak valid.')
    except ValueError:
        print('Input harus berupa angka.')

def tampilkan_tiket():
    cetak_pembatas()
    print(f'{'Daftar Tiket Terjual':^60}')
    cetak_pembatas()

    if not os.path.exists(TICKET_HISTORY_FILE):
        print('Belum ada tiket yang terjual.')
        return
    with open(TICKET_HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        if not lines:
            print('Belum ada tiket yang terjual.')
            return
        for idx, line in enumerate(lines, start=1):
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) == 3:
                    id_tiket, nama_film, waktu = parts
                    print(f'{idx}. ID Tiket: {id_tiket}, Film: {nama_film}, Waktu: {waktu}')
                else:
                    print(f'Data tidak lengkap pada baris {idx}.')
    cetak_pembatas()

def tampilkan_detail_tiket():
    cetak_pembatas()
    id_tiket = input('Masukkan ID tiket yang ingin dilihat \t: ')
    file_tiket = os.path.join(TICKET_DIR, f'{id_tiket}.txt')
    if os.path.exists(file_tiket):
        with open(file_tiket, 'r') as file:
            detail = file.read()
            cetak_pembatas()
            print(f'Detail Tiket:\n{detail}')
            cetak_pembatas()
    else:
        print('Tiket tidak ditemukan.')

def hapus_tiket():
    cetak_pembatas()
    id_tiket = input('Masukkan ID tiket yang ingin dihapus \t: ')
    file_tiket = os.path.join(TICKET_DIR, f'{id_tiket}.txt')
    if os.path.exists(file_tiket):
        os.remove(file_tiket)
        if os.path.exists(TICKET_HISTORY_FILE):
            with open(TICKET_HISTORY_FILE, 'r') as file:
                lines = file.readlines()
            with open(TICKET_HISTORY_FILE, 'w') as file:
                for line in lines:
                    if not line.startswith(id_tiket):
                        file.write(line)
        cetak_pembatas()
        print(f'Tiket dengan ID "{id_tiket}" telah dihapus.')
        cetak_pembatas()
    else:
        print('Tiket tidak ditemukan.')

def admin_menu():
    while True:
        cetak_pembatas()
        print(f'{'ADMIN':^60}')
        cetak_pembatas()
        print('Menu Admin:\n1. Manajemen Film\n2. Manajemen Tiket\n3. Kembali ke menu utama')
        cetak_pembatas()
        pilihan = input('Pilih opsi \t: ').strip()
        if pilihan == '1':
            while True:
                cetak_pembatas()
                print('Manajemen Film:\n1. Tambah Film\n2. Hapus Film\n3. Tampilkan Daftar Film\n4. Kembali')
                cetak_pembatas()
                opsi = input('Pilih opsi \t: ').strip()
                if opsi == '1':
                    tambah_film()
                elif opsi == '2':
                    hapus_film()
                elif opsi == '3':
                    tampilkan_film()
                elif opsi == '4':
                    break
                else:
                    print('Opsi tidak valid.')
        elif pilihan == '2':
            while True:
                cetak_pembatas()
                print('Manajemen Tiket:\n1. Tampilkan Daftar Tiket\n2. Tampilkan Detail Tiket\n3. Hapus Tiket\n4. Kembali')
                cetak_pembatas()
                opsi = input('Pilih opsi \t: ').strip()
                if opsi == '1':
                    tampilkan_tiket()
                elif opsi == '2':
                    tampilkan_detail_tiket()
                elif opsi == '3':
                    hapus_tiket()
                elif opsi == '4':
                    break
                else:
                    print('Opsi tidak valid.')
        elif pilihan == '3':
            break
        else:
            print('Opsi tidak valid.')

def pengunjung_menu():
    while True:
        cetak_pembatas()
        print(f'{'PENGUNJUNG':^60}')
        cetak_pembatas()
        print('Menu Pengunjung:\n1. Tampilkan Daftar Film\n2. Beli Tiket\n3. Kembali ke menu utama')
        cetak_pembatas()
        pilihan = input('Pilih opsi \t: ').strip()
        cetak_pembatas()
        if pilihan == '1':
            tampilkan_film()
        elif pilihan == '2':
            beli_tiket()
        elif pilihan == '3':
            break
        else:
            print('Opsi tidak valid.')

def main():
    cetak_pembatas()
    print(f'{'SELAMAT DATANG DI APLIKASI TIKET BIOSKOP':^60}')
    cetak_pembatas()
    while True:
        print('Pilih peran:\n1. Admin\n2. Pengunjung\n3. Keluar')
        cetak_pembatas()
        peran = input('Masukkan peran Anda \t: ').strip()
        if peran == '1':
            admin_menu()
        elif peran == '2':
            pengunjung_menu()
        elif peran == '3':
            cetak_pembatas()
            print(f'\n{'TERIMA KASIH! Sampai Jumpa.':^60}\n')
            cetak_pembatas()
            break
        else:
            print('\nOpsi tidak valid. Silakan coba lagi.')

if not os.path.exists(FILM_DIR):
    os.makedirs(FILM_DIR)
if not os.path.exists(MOVIE_FILE):
    open(MOVIE_FILE, 'w').close()
if not os.path.exists(TICKET_DIR):
    os.makedirs(TICKET_DIR)
if not os.path.exists(TICKET_HISTORY_FILE):
    open(TICKET_HISTORY_FILE, 'w').close()

main()
