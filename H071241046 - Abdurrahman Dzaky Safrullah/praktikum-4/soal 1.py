import os
import random
os.system("cls")

def judi():
    
    # header
    print("SELAMAT DATANG DI BLACKJACK")
    
    # masing-masing punya 1 kartu
    pemain = random.randint(1, 11)
    dealer = random.randint(1, 11)
    
    
    #pemain dulu
    while True:
        print(f"kartu anda sekarang = {pemain}")
        y = input("apakah anda masih ingin mengambil kartu (y/n) : ")
        if y == "n" or y == "N":
            break
        elif y == "y" or y == "Y":
            pemain += random.randint(1, 11)
            if pemain > 21:
                print(f"Kartu anda sekarang = {pemain}\nANDA KALAH, kartu lebih dari 21")
                return
        else:
            print(f"Silahkan input y/n")
            continue
            
            
    # giliran dealer ambil kartu        
    print(f"Kartu dealer sekarang = {dealer}")
    while dealer < 17:
        dealer += random.randint(1, 11)
        print(f"kartu dealer : {dealer}")
        
        # print(f"kartu dealer = {dealer}")
        
    print(f"kartu akhir anda {pemain}")
    print(f"kartu akhir dealer {dealer}")
    # print(f"kartu lawan {dealer}")

    if dealer > 21:
        print("ANDA MENANG")
    elif dealer < pemain:
        print("ANDA MENANG")
    elif dealer == pemain:
        print("SERI")
    else:
        print("ANDA KALAH")
        
            
judi()

