def sandi_az(teks):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    teks_enkripsi = []

    for karakter in teks:
        if karakter.isalpha():
            is_lower = karakter.islower()
            index = alphabet.index(karakter.lower())
            karakter_enkripsi = alphabet[(25 - index)]

            teks_enkripsi.append(karakter_enkripsi if is_lower else karakter_enkripsi.upper())
        else:
            teks_enkripsi.append(karakter)

    return ''.join(teks_enkripsi)

teks = input("Masukkan String : ")

print(f"Teks : {teks}")
print(f"Sandi : {sandi_az(teks)}")