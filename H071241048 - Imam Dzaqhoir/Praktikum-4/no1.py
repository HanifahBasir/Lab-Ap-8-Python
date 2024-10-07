import random

def kartu():
    return random.randint(1, 10)

def ambil_kartu():
    total_kartu, hitung_as = 0, 0

    # Pemain menarik kartu pertama
    kartu_tertarik = kartu()
    if kartu_tertarik == 1:
        kartu_tertarik = 11
        hitung_as += 1
        print("=== Anda menarik kartu As (nilai 11). ===\n")
    else:
        print(f"Anda menarik kartu: {kartu_tertarik}")

    total_kartu += kartu_tertarik
    print(f"Kartu anda sekarang adalah: {total_kartu}\n")

    # Proses pengambilan kartu tambahan
    while True:
        if input("Apakah masih akan mengambil kartu? (y/n): ").lower() != 'y':
            break

        # Tarik kartu tambahan
        kartu_tertarik = kartu()
        if kartu_tertarik == 1:
            kartu_tertarik = 11
            hitung_as += 1
            print("=== Anda menarik kartu As (nilai 11). ===\n")

        total_kartu += kartu_tertarik
        print(f"Kartu anda sekarang adalah: {total_kartu}\n")

        # Cek apakah total_kartu melebihi 21 dan ada kartu As
        while total_kartu > 21 and hitung_as > 0:
            total_kartu -= 10
            hitung_as -= 1
            print("--- Mengubah nilai kartu As menjadi 1. ---\n")
            print(f"Kartu anda sekarang adalah: {total_kartu}")

        if total_kartu > 21:
            print("Anda kalah!")
            return total_kartu

    return total_kartu

def dealer():
    total_kartu, hitung_as = 0, 0

    # Dealer menarik kartu pertama
    kartu_tertarik = kartu()
    if kartu_tertarik == 1:
        kartu_tertarik = 11
        hitung_as += 1
        print("=== Dealer menarik kartu As (nilai 11). ===\n")
    else:
        print(f"Dealer menarik kartu: {kartu_tertarik}")

    total_kartu += kartu_tertarik
    print(f"Kartu dealer sekarang adalah: {total_kartu}")

    # Dealer menarik kartu tambahan sampai total >= 17
    while total_kartu < 17:
        kartu_tertarik = kartu()
        if kartu_tertarik == 1:
            kartu_tertarik = 11
            hitung_as += 1
            print("=== Dealer menarik kartu As (nilai 11). ===\n")
        total_kartu += kartu_tertarik
        print(f"Kartu dealer sekarang adalah: {total_kartu}")

        # Cek apakah total_kartu melebihi 21 dan ada kartu As
        while total_kartu > 21 and hitung_as > 0:
            total_kartu -= 10
            hitung_as -= 1
            print("--- Mengubah nilai kartu As menjadi 1. ---\n")
            print(f"Kartu dealer sekarang adalah: {total_kartu}")

    return total_kartu

def tentukan_pemenang(total_pemain, total_dealer):
    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_pemain == total_dealer:
        print("Seri!")
    elif total_pemain > total_dealer:
        print("**Anda menang!**")
    else:
        print("Dealer menang!")

print("Welcome to Blackjack!")
total_pemain = ambil_kartu()
if total_pemain <= 21:
    total_dealer = dealer()
    tentukan_pemenang(total_pemain, total_dealer)
else:
    print("Anda kalah, kartu anda melebihi 21.")