gol = input("golongan = ")
daya = float(input("daya = "))
pemakaian = float(input("pemakaian = "))

def tarif(gol, daya, pemakaian):
    if gol == "R1":
        if daya <= 900:
            return 1352
        elif 900 <= daya <= 1300:
            return 1444.70
        elif 1300 <= daya <= 2200:
            return 1444.70
        
    elif gol == "R2":
        if 3500<=daya <= 5500:
            return 1699.53

        
    elif gol == "R3":
        if daya >= 6600:
            return 1699.53

    else:
        return 0

total_biaya = pemakaian * tarif(gol, daya, pemakaian)
print(f'jumlah tagihan anda: {total_biaya:,.1f}')