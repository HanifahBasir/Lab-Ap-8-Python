import os
os.system("cls")



def fungsi(inputan):
    if inputan <= 0:
        return "Input tidak valid!"
    else:
        langkah = 0
        while inputan != 1:
            langkah += 1
            if inputan % 2 == 0:
                inputan //= 2
            else:
                inputan = inputan * 3 + 1
            a = float(inputan)
            print(a)
        return f"Langkah = {langkah}"
try:
    a = float(input("Masukkan angka predict : "))
except ValueError:
    print("Masukan Integer!!!!!!!!!!!!!!!")
else:
    print(fungsi(a))