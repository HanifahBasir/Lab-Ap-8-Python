import backend
import os


os.system("cls")

while True:
    
    os.system("cls")
    
    print("SELAMAT DATANG".center(105))
    print("GUDANG SERBA ADA".center(105))
    print("="*105)
    
    print("\nopsi yang tersedia".upper())
    print("1. menampilkan daftar barang".upper())
    print("2. menambahkan daftar barang".upper())
    print("3. mengupdate daftar barang".upper())
    print("4. menghapus daftar barang".upper())
    print("5. mencari barang".upper())
    
    opsi = input("\nsilahkan pilih opsi : ".upper())
    
    match opsi:
        case "1" : backend.tampil()
        case "2" : backend.tambah()
        case "3" : backend.update()
        case "4" : backend.delete()
        case "5" : backend.cari()
        case _ : print("MASUKKAN OPSI YANG TEPAT!! (1,2,3,4,5)")
        
    stop = input("\napakah anda ingin keluar? (y/n) : ")
    if stop == "y" or stop == "Y":
        break

print("\n\nBYEE")