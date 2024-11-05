import os
import backend
os.system("cls")

# import tiket
# import films

while True:
    
    os.system("cls")
    
    print(" SELAMAT DATANG DI PROGRAM BIOSKOP ".center(60, "="))
    print("\n")
    print("silahkan pilih mode".upper())
    print("\n")
    
    print("1. mode atmin\n".upper())
    print("2. mode kroco".upper())
    
    print("\n")
    
    mode = input("mode apa? : ".upper())

    match mode: 
        case "1" : backend.admin()
        case "2" : backend.pengunjung()
        case _ : print("masukkan opsi yang tepat!! (1/2/3)")
        
    print("\n")

    quit = input("ingin keluar dari bioskop? (y/n) : ".upper())
    if quit == "y" or quit =="Y":
        break
        
print("\nterima kasih".upper())
    
