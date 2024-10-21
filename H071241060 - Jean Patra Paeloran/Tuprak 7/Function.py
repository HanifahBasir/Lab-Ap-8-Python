import os
from datetime import datetime as dt
def Tambah():
    print("\n--- Tambah Film ---")
    nama = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
    if nama=="":
        print("\nKembali ke Menu Admin")
        return
    else:
        if not os.path.exists("Film"):
            os.makedirs("Film")
        File = os.path.join("Film", f"{nama}.txt")
        with open(File,"w") as file:
            file.write(nama+"\n")
        print(f"\nFilm '{nama}' berhasil ditambahkan.")
    Tambah()
def Hapus():
    if not os.path.exists("Film"):
        print("\nBelum ada film yang tersedia.")
        return
    DaftarFilm = os.listdir("Film")  # Ambil semua file dalam folder "Tiket"
    if not DaftarFilm:
        print("\nBelum ada film tersedia.")
        return
    print("\n--- Hapus Film ---\nDaftar Film:")
    for i,film in enumerate(DaftarFilm,start=1):
        print(f"{i}. {film.strip('.txt')}")
    print("0. Kembali")
    try:
        Nomor = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali):  "))
        if Nomor==0:
            print("\nKembali ke menu admin.")
            return
        elif 1<=Nomor<=len(DaftarFilm):
            FileFilm = DaftarFilm[Nomor-1]
        else:
            print("Opsi tidak valid")
            return
        FileFilm = os.path.join("Film", FileFilm)
        os.remove(FileFilm)
        Hapus()
    except ValueError:
        print("Opsi tidak valid")
        return
def ListTiket():
    if not os.path.exists("Tiket"):
        print("\nBelum ada tiket yang dijual.")
        return
    daftar_tiket = os.listdir("Tiket")
    if not daftar_tiket:
        print("\nBelum ada tiket yang dijual.")
        return
    print("\nDaftar Tiket:")
    for i,tiket in enumerate(daftar_tiket,start=1):
        print(f"{i}. {tiket.strip('.txt')}")
    return
def DetailTiket():
    if not os.path.exists("Tiket"):
        print("\nBelum ada tiket yang dijual.")
        return
    daftar_tiket = os.listdir("Tiket")  # Ambil semua file dalam folder "Tiket"
    if not daftar_tiket:
        print("\nBelum ada tiket yang dijual.")
        return
    print("\n--- Detail Tiket ---\nDaftar Tiket:")
    for i,tiket in enumerate(daftar_tiket,start=1):
        print(f"{i}. {tiket.strip('.txt')}")
    print("0. Kembali")
    try:
        Nomor = int(input("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): "))
        if Nomor==0:
            print("\nKembali ke Daftar Tiket")
            return
        elif 1<=Nomor<=len(daftar_tiket):
            FileTiket = daftar_tiket[Nomor-1]
        else:
            print("Opsi tidak valid")
            return
        fileTiket = os.path.join("Tiket", FileTiket)
        with open(fileTiket, "r") as file:
            detail = file.read()
            print(f"\nDetail Tiket '{FileTiket}':")
            print(detail)
    except ValueError:
        print("opsi tidak valid")
        return
    DetailTiket()
def HapusTiket():
    if not os.path.exists("Tiket"):
        print("\nBelum ada tiket yang dijual.")
        return
    daftar_tiket = os.listdir("Tiket")  # Ambil semua file dalam folder "Tiket"
    if not daftar_tiket:
        print("\nBelum ada tiket yang dijual.")
        return
    print("\n--- Hapus Tiket ---\nDaftar Tiket:")
    for i,tiket in enumerate(daftar_tiket,start=1):
        print(f"{i}. {tiket.strip('.txt')}")
    print("0. Kembali")
    try:
        Nomor = int(input("Pilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
        if Nomor==0:
            print("\nKembali ke menu daftar tiket")
            return
        elif 1<=Nomor<=len(daftar_tiket):
            FileTiket = daftar_tiket[Nomor-1]
        else:
            print("Opsi tidak valid")
            return
        fileTiket = os.path.join("Tiket", FileTiket)
        os.remove(fileTiket)
        HapusTiket()
    except ValueError:
        print("Opsi tidak valid")
        return
    except ValueError:
        print("Opsi tidak valid.")
        return
def ListFilm():
    if not os.path.exists("Film"):
        print("\nBelum ada film yang tersedia.")
        return
    DaftarFilm = os.listdir("Film")  # Ambil semua file dalam folder "Tiket"
    if not DaftarFilm:
        print("\nBelum ada film tersedia.")
        return
    print("\nDaftar Film:")
    for i,film in enumerate(DaftarFilm,start=1):
        print(f"{i}. {film.strip('.txt')}")
    return
def Beli(): 
    if not os.path.exists("Film"):
        print("\nBelum ada film yang tersedia.")
        return
    DaftarFilm = os.listdir("Film")  # Ambil semua file dalam folder "Tiket"
    if not DaftarFilm:
        print("\nBelum ada film tersedia.")
        return
    print("\nDaftar Film:")
    for i,film in enumerate(DaftarFilm,start=1):
        print(f"{i}. {film.strip('.txt')}")
    print("0. Kembali")
    try:
        Tiket = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
    except ValueError:
        print("Opsi tidak valid")
        return
    Waktu = dt.now().strftime("%d%m%Y%H%M%S")
    Tanggal = dt.now().strftime("%d-%m-%Y %H:%M:%S")
    if Tiket==0:
        print("\nKembali ke menu pengunjung")
        return
    elif 1<=Tiket<=len(DaftarFilm):
        try:
            Film = DaftarFilm[Tiket-1]
            TiketBioskop = f"""
+-------------------------------------+
|            TIKET BIOSKOP            |
+-------------------------------------+
| ID Tiket : TICK{Waktu}       |
| Film     : {Film.strip(".txt")}|
| Tanggal  : {Tanggal}      |
+-------------------------------------+
|     Terima kasih telah membeli      |
|             tiket Anda!             |
+-------------------------------------+
"""
            if not os.path.exists("Tiket"):
                os.makedirs("Tiket")
            File = os.path.join("Tiket", "TICK"+Waktu)
            with open(File, "w") as file:
                file.write(TiketBioskop)
            print(f"\nTiket berhasil dibeli. ID tiket Anda: TICK{Waktu}\nFile tiket telah dibuat: Tiket/TICK{Waktu}.txt")
            return
        except ValueError as e:
            print(e)
    else:
        print("Opsi tidak valid")
        Beli()
    
    