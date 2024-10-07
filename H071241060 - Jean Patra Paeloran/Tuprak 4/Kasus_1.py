import random
def kartu():
    return random.randint(1,10)
def jumlah_kartu(nilai):
    return sum(nilai)
def mulai():
    print("Welcome to Blackjack!")
    anda = [kartu()]
    lawan = [kartu()]
    print(f"Kartu anda sekarang adalah: {anda[0]}")
    while True:
        keputusan = input("Apakah masih akan mengambil kartu? (y/n) \n").lower()
        total1 = jumlah_kartu(anda)
        if keputusan == "y":
            anda.append(kartu())
            total1 = jumlah_kartu(anda)
            if total1>21:
                print("Anda kalah, kartu anda melebihi 21")
                break
            print(f"Kartu anda sekarang adalah: {total1}")
        elif keputusan == "n":
            break
        else:
            print("inputan tidak valid")
            continue
    total2 = 0
    if total1<=21:
        print(f"Kartu dealer adalah: {lawan[0]}")
        while True:
            if total2<=17:
                lawan.append(kartu())
                total2 = jumlah_kartu(lawan)
                print("kartu dealer dibawah 17, dealer akan mengambil 1 kartu")
                print(f"Kartu dealer sekarang adalah: {total2}")
            elif total2>17:
                break
        if 21>=total1>total2 or total2>21:
            print("Anda menang!")
        elif 21>=total1<total2:
            print("Dealer menang!")
        elif 21>=total1==total2:
            print("Seri!")

mulai()