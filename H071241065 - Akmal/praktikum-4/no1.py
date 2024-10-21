import random

def kartu_random():
    return random.randint(1, 10)

def kartu():
    print("welcome to blackjack")
    
# kartu pemainn
    x = kartu_random()
    print(f"kartu anda sekarang adalah: {x}")

    while True:
        ambil_kartu = input("apakah masih akan mengambil kartu? (y/n): \n").lower()
        if ambil_kartu == "y":
            x += kartu_random()
            print(f"kartu anda sekarang adalah: {x}")
            if x > 21:
                print("anda kalah kartu anda melebihi 21")
                return
        elif ambil_kartu == "n":
            break
        else:
            print("input yang anda masukkan tidak valid")
            continue
            
            
# kartu dealerr 
    y = kartu_random()

    print(f"kartu dealer adalah: {y}")
    
    while y < 17:
        y += kartu_random()
        print(f"kartu dealer sekarang adalah: {y}")
        
# total kartu
    total_kartu_pemain = x
    total_kartu_dealer = y
    
    if total_kartu_dealer > 21:
        print("anda menang, kartu dealer melebihi 21")
    elif total_kartu_pemain < total_kartu_dealer:
        print("anda kalah")
    elif total_kartu_pemain > total_kartu_dealer:
        print("anda menang")
    elif total_kartu_pemain == total_kartu_dealer:
        print("seri")

kartu()