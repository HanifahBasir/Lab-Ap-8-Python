enkripsi = input("Masukkan string :")
Shift = int(input("Masukkan jumlah penggeseran :"))
hasil = ""
for karakter in enkripsi:
    if karakter.isupper():
        hasil+=chr((ord(karakter)+Shift-65)%26+65)
    elif karakter.islower():
        hasil+=chr((ord(karakter)+Shift-97)%26+97)
    else:
        hasil+=karakter
print(f"Text  : {enkripsi}\nShift : {Shift}\nCipher: {hasil}")