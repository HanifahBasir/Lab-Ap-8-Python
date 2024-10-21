def bilangan(angka):
    if angka <= 0:
        print("input tidak valiid")
    else:
        x = 0
        while angka != 1:
            x += 1
            if angka % 2 == 0:
                angka = angka // 2
            else:
                angka = angka * 3 + 1
            print(f"{angka:.2f}")
        return f"langkah = {x}"
    
try:
    isi = float(input("masukkan angka: "))
except ValueError:
    print("masukkan angka bulat positif")
else:   
    print(bilangan(isi))


            



