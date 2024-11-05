from datetime import datetime
import os

from .pengunjung import tampil

os.system("cls")

### INI TAMBAH
def tambah():
    while True:
        with open("film.txt", "a") as f:
            nama_film = input("\nmasukkan judul film  atau enter untuk berhenti: ")
            if nama_film == "":
                break
            else:
                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{nama_film} , {waktu}\n")
                print(f'film berjudul : "{nama_film}" berhasil ditambahkan')



# def hapus():
#     tampil()
    
#     while True:
#         with open("film.txt", "r") as file:
#             pilih = input("film nomor berapa yang ingin anda hapus? : ")
#             for index, line in enumerate(file.readlines()):
#                 with open("sementara.txt", "w") as f:
#                     file.readline()
#                     if pilih == index+1:
#                         pass
#                     else:
#                         f.write(line)
                
#             print("daftar film terbaru : ")
#             tampil()
#             close = input(f"keluar? (y/n) : ")
#             if close == "y" or close =="Y":
#                 break
                    
#     os.replace("sementara.txt", "film.txt")

#### INI HAPUS
def hapus():
    
    tampil()

    with open("film.txt", "r") as file:
        nomor = int(input("film nomor berapa yang ingin anda hapus? : "))
        count = 0
        while True:
            content = file.readline()
            if len(content) == 0:
                break
            elif count == nomor - 1:
                pass
            else:
                with open("a.txt", "a") as f:
                    f.write(content)
            count += 1
            
    print("BERHASIL TERHAPUS\n")
    os.replace("a.txt", "film.txt")
    
############# TIKET

def tiket():
    while True:
        os.system("cls")
        print(("menu tiket".upper()).center(20,"="))
        print("\n")
        print("1. tampilkan seluruh tiket\n".upper())
        print("2. tampilkan detail tiket\n".upper())
        print("3. hapus tiket".upper())
        print("\n")
        opsi_tiket = input("\nmasukkan opsi : ")
        
        match opsi_tiket:
            case "1" : tampil_tiket()
            case "2" : detail_tiket()
            case "3" : hapus_tiket()
            case _ : print("masukkan opsi yang tepat (1/2/3)!!! : ")

        print("\n") 
        
        quit = input("keluar dari menu tiket? (y/n) : ".upper())
        if quit == "y" or quit == "Y":
            break


def tampil_tiket():
    print(f"\ndaftar tiket : ".upper())
    folder_path = 'C:/Users/Dzaky/Documents/Lab Python/pert 10/tugas/tiket' 
    print("\n")
    index = 1
    for file_name in os.listdir(folder_path):
            print(f"{index}. {file_name[:-4]}")
            index += 1
    if index == 1:
        print("\nTIDAK ADA TIKET KAPTEN")


# def hapus_tiket():
#     tampil_tiket()

#     hapus = input("\nSALIN KEMUDIAN TEMPELKAN KODE YANG INGIN ANDA HAPUS\n-> ")
#     hapus_kode = (f"{hapus}.txt").strip()
    
#     folder_path = 'C:/Users/Dzaky/Documents/Lab Python/pert 10/tugas/tiket' 
#     ada = False
#     for file_name in os.listdir(folder_path):
#         if hapus_kode == file_name:
#             ada = True
#             break
#     if ada:
#         os.remove(hapus_kode)
#         print(f"\nTiket dengan kode '{hapus_kode}' TERHAPUS\n".upper())
#     else:
#         print("KODE TIKET TIDAK VALID!!")


def hapus_tiket():
    tampil_tiket()

    hapus = input("\nSALIN KEMUDIAN TEMPELKAN KODE TIKET YANG INGIN ANDA HAPUS\n-> ")
    hapus_kode = (f"{hapus}.txt").strip()

    folder_path = 'C:/Users/Dzaky/Documents/Lab Python/pert 10/tugas/tiket' 

    file_path = os.path.join(folder_path, hapus_kode)

    if os.path.exists(file_path):
        os.remove(file_path)  
        print(f"\nTiket dengan kode '{hapus_kode}' TERHAPUS\n".upper())
    else:
        print("KODE TIKET TIDAK VALID!!")


# def detail_tiket():
#     tampil_tiket()
#     tampil = input("\nSALIN KEMUDIAN TEMPELKAN KODE TIKET YANG INGIN ANDA LIHAT\n-> ")
    
#     kode_tiket = (f"{tampil}.txt").strip()

#     folder_path = 'C:/Users/Dzaky/Documents/Lab Python/pert 10/tugas/tiket' 
#     print("\n")
    
#     ada = False
#     for file in os.listdir(folder_path):
#         if file == kode_tiket:
#             ada = True
#             break

#     if not ada:
#         print("KODE TIKET TIDAK VALID!!")
#     else:
#         with open(kode_tiket, "r") as f:
#             print(f.read())

def detail_tiket():
    tampil_tiket()
    tampil = input("\nSALIN KEMUDIAN TEMPELKAN KODE TIKET YANG INGIN ANDA LIHAT\n-> ")
    
    kode_tiket = (f"{tampil}.txt").strip()

    folder_path = 'C:/Users/Dzaky/Documents/Lab Python/pert 10/tugas/tiket' 
    print("\n")
    
    ada = False
    for file in os.listdir(folder_path):
        if file == kode_tiket:
            ada = True
            break

    if not ada:
        print("KODE TIKET TIDAK VALID!!")
    else:
        # Gabungkan folder_path dengan kode_tiket
        file_path = os.path.join(folder_path, kode_tiket)
        
        # Buka file menggunakan path lengkap
        with open(file_path, "r") as f:
            print(f.read())

            
        



    
def admin():
    
    while True:
        
        os.system("cls")
        
        print("\n")
        print(" MODE ADMIN ".center(40,"="))
        print("\n")
        print("opsi yang tersedia".upper())
        print("\n")
        print("1. tambah film\n".upper())
        print("2. hapus film\n".upper())
        print("3. daftar tiket".upper())
        
        print("\n")

        opsi = input("masukkan opsi : ")
        
        match opsi:
            case "1" : tambah()
            case "2" : hapus()
            case "3" : tiket()
            case _ : print("masukkan input yang valid!! (1/2/3)")
        
        print("\n")

        quit = input("keluar dari mode atmin? (y/n) : ".upper())
        if quit == "y" or quit == "Y":
            break




