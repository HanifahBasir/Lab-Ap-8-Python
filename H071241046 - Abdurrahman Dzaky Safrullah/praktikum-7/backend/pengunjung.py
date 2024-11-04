import os
from datetime import datetime


def tampil():
    with open("film.txt", "r") as f:
        print("\n")
        print(f"="*44)
        print("|",("daftar film".upper()).center(40),"|")
        print(f"="*44)
        for index,line in enumerate(f.readlines()):
            line_break = line.strip("\n")
            line_break = line_break.split(",")
            print(f"|{(str(index+1)).center(4)}|{(line_break[0][:30]).center(37)}|")
        print(f"="*44)
        print("\n")


def beli():
    while True:
        os.system("cls")
        with open("film.txt", "r") as f:
            tampil()
            opsi_tiket = input("\npilih nomor film yang ingin anda tonton (enter untuk kembali) : ")
            if opsi_tiket == "":
                break
            
            for index,line in enumerate(f.readlines()):
                line_break = line.strip("\n")
                line_break = line_break.split(",")
                if opsi_tiket == str(index+1):
                    nama_file = f"TICK{datetime.now().strftime("%d%m%Y%H%M%S")}!"
                    os.makedirs("tiket", exist_ok=True)
                    with open(os.path.join("tiket", f"{nama_file}.txt"), "a") as f:
                        f.write(
                            f'''
        {"-"*60}
        |{"TIKET BIOSKOP".center(58)}|
        {"-"*60}
        | id tiket : {(nama_file).ljust(45)} |
        | film     : {((line_break[0]).strip()).ljust(45)} |
        | tanggal  : {(datetime.now().strftime("%d-%m-%Y %H:%M:%S")).ljust(45)} |
        {"-"*60}
                            '''
                        )
                        print(f'tiket film berjudul : "{(line_break[0]).strip()}" berhasil dibeli')
                        break
            else:
                print("MASUKKAN NOMOR FILM YANG TEPAT!!! : ")
        
        quit = input("\nLANJUT? (Y/N) : ")
        if quit == "n" or quit == "N":
            break


# def beli():
#     while True:
#         tampil()  # Panggil fungsi tampil untuk menampilkan daftar film
#         opsi_tiket = input("Pilih nomor film yang ingin Anda tonton (enter untuk kembali): ")
        
#         if opsi_tiket == "":
#             break
#         else:
#             try:
#                 opsi_tiket = int(opsi_tiket)  # Ubah input menjadi integer
#             except ValueError:
#                 print("Harap masukkan nomor yang valid.")
#                 continue
            
#             with open("film.txt", "r") as f:
#                 lines = f.readlines()
                
#                 # Pastikan opsi_tiket dalam rentang yang benar
#                 if 1 <= opsi_tiket <= len(lines):
#                     line_break = lines[opsi_tiket - 1].strip("\n").split(",")
#                     nama_file = f"TICK{datetime.now().strftime('%d%m%Y%H%M%S')}"

#                     with open(f"{nama_file}.txt", "a") as tiket_file:
#                         tiket_file.write(
#                             f'''
#                             {"-"*60}
#                             |{"TIKET BIOSKOP".center(58)}|
#                             {"-"*60}
#                             | id tiket : {nama_file.ljust(45)} |
#                             | film     : {line_break[0].strip().ljust(45)} |
#                             | tanggal  : {datetime.now().strftime("%d-%m-%Y %H:%M:%S").ljust(45)} |
#                             {"-"*60}
#                             '''
#                         )
#                         print(f'Tiket film berjudul: "{line_break[0].strip()}" berhasil dibeli.')
#                 else:
#                     print("Nomor film tidak valid. Silakan pilih lagi.")
                    

def pengunjung():
    
    while True:
        
        os.system("cls")
        print("\n")
        print(" MODE PENGUNJUNG ".center(40,"="))
        print("\n")
        print("opsi yang tersedia".upper())
        print("\n")
        print("1. tampilkan daftar film\n".upper())
        print("2. beli tiket".upper())
        
        print("\n")

        opsi = input("masukkan opsi : ".upper())
        
        match opsi:
            case "1" : tampil()
            case "2" : beli()
            case _ : print("masukkan input yang valid!! (1/2/3)")
            
        quit = input("keluar dari mode pengunjung? (y/n) : ".upper())
        if quit == "y" or quit == "Y":
            break
            