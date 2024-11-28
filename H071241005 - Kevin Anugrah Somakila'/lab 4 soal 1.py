import random as rn
kartu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10, 10, 10]
def ambil_kartu():
    return rn.choice(kartu)
def blacjack():
    kartu_pemain = [ambil_kartu()]
    kartu_dealer = [ambil_kartu()]
    print (f"kartu anda sekarang adalah : {kartu_pemain[0]}")
    while True:
        input_pemain = input("ingin mengambil kartu lagi? (y/n)").lower()
        if input_pemain == "y":
            kartu_pemain.append(ambil_kartu())
            print(f"kartu anda sekarang adalah {sum(kartu_pemain)}")
            if sum(kartu_pemain) >21:
                print("anda kalah kartu lebih dari 21.")
                return
        elif input_pemain =="n":
            break
        else:
            print("Input tidak valid. Masukkan y atau n untuk tidak.")
            
    while sum(kartu_dealer)<17:
        kartu_dealer.append(ambil_kartu())
    total_pemain = sum(kartu_pemain)
    total_dealer = sum(kartu_dealer)
    if total_dealer>21 or total_dealer < total_pemain:
        print("Anda menang !")
    elif total_dealer > total_pemain:
        print("Dealer menang!")
    elif total_pemain < total_dealer:
        print("Anda menang !")
    elif total_dealer == total_pemain:
        print("Seri !")
print("Welcome To Blacjack")
blacjack()

