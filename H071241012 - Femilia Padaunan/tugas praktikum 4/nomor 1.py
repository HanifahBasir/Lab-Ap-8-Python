import random
def ambil_kartu():
    nomor_kartu = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]   #10 ada 4 adalah kartu 10, J, Q, K
    return random.choice(nomor_kartu)
 
def main():
    print("Welcome to Blackjack!")
    
    nilai_kartu_pemain = ambil_kartu()
    print(f"Kartu anda sekarang adalah: {nilai_kartu_pemain}")
    
    while True:
        pilihan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if pilihan == 'y':
            nilai_kartu_pemain = nilai_kartu_pemain + ambil_kartu()
            print(f"Kartu anda sekarang adalah: {nilai_kartu_pemain}")
            if nilai_kartu_pemain > 21:
                print(f"Anda kalah, kartu anda melebihi 21. ")
                return
        elif pilihan == 'n':
            break
        else:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    
    nilai_kartu_dealer = ambil_kartu()
    print(f"Kartu dealer adalah: {nilai_kartu_dealer}")
    
    while nilai_kartu_dealer < 17:
        nilai_kartu_dealer +=  ambil_kartu()
        print(f"Kartu dealer sekarang adalah: {nilai_kartu_dealer}")
    
    if nilai_kartu_dealer > 21 or nilai_kartu_dealer < nilai_kartu_pemain:
        print("Anda menang!")
    elif nilai_kartu_dealer > nilai_kartu_pemain:
        print("Dealer menang!")
    elif nilai_kartu_dealer==nilai_kartu_pemain:
        print("Seri!")

main()