"""Permainan BlackJack Sederhana"""

print("Welcome to Blackjack!")

import random
pemain_bermain = True
dealer_bermain = True

dek_kartu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
kartu_pemain = []
kartu_dealer = []

# membagikan kartu
def BagikanKartu(turn): 
    kartu = random.choice(dek_kartu) #mengambil 1 kartu random dari list 
    turn.append(kartu) #memasukkan kartu yang terpilih
    dek_kartu.remove(kartu) #mengeluarkan kartu yang terpilih dari list
    
# menghitung total kartu pada pemain dan dealer
def total(turn): # list berisi kartu milik pemain atau dealer
    total = 0 # menghitung total dari 0
    face = ['J', 'Q', 'K'] 
    for kartu in turn:
        if kartu in range(1, 11):
            total += kartu
        elif kartu in face: # kartu 'J','Q','K' bernilai 10
            total += 10
        else: # kartu 'A'
            if total > 10: 
                total += 1
            else:
                total += 11
    return total # mengembalikan nilai total         

    
# loop permainan
BagikanKartu(kartu_dealer) #membagikan kartu
BagikanKartu(kartu_pemain) #membagikan kartu
    
while pemain_bermain or dealer_bermain: 
    print(f"Anda memiliki {kartu_pemain} dengan total {total(kartu_pemain)}")
    
    if pemain_bermain:
        yORn = input("Apakah anda masih ingin mengambil kartu? (y/n)\n")
    if total(kartu_dealer) > 16:
        dealer_bermain = False
    else:
        BagikanKartu(kartu_dealer)
    if yORn == 'n':
        pemain_bermain = False
    else: 
        BagikanKartu(kartu_pemain)
    if total(kartu_pemain) >= 21:
        break
    elif total(kartu_dealer) >= 21:
        break

print(f"Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")

if total(kartu_dealer) == total(kartu_pemain):
    print(f"\nKamu memiliki {kartu_pemain} dengan total {total(kartu_pemain)} dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Seri!")
elif total(kartu_pemain) == 21:
    print(f"\nKamu memiliki {kartu_pemain} dengan total 21 dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Blackjack! Kamu menang!")
elif total(kartu_dealer) == 21:
    print(f"\nKamu memiliki {kartu_pemain} dengan total {total(kartu_pemain)} dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Blackjack! Dealer menang!")
elif total(kartu_pemain) > 21:
    print(f"\nKamu memiliki {kartu_pemain} dengan total {total(kartu_pemain)} dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Kartumu lebih, Dealer menang!")
elif total(kartu_dealer) > 21:
    print(f"\nKamu memiliki {kartu_pemain} dengan total {total(kartu_pemain)} dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Kartu Dealer lebih, Kamu menang!")
elif 21 - total(kartu_dealer) < 21 - total(kartu_pemain):
    print(f"\nKamu memiliki {kartu_pemain} dengan total {total(kartu_pemain)} dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Dealer menang!")
elif 21 - total(kartu_dealer) > 21 - total(kartu_pemain):
    print(f"\nKamu memiliki {kartu_pemain} dengan total {total(kartu_pemain)} dan Dealer memiliki {kartu_dealer} dengan total {total(kartu_dealer)}")
    print("Kamu menang!")
