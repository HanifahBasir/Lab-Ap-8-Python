def sandi_caesar(teks, pergeseran):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    teks_enkripsi = []

    for karakter in teks:
        if karakter.isalpha():
            is_lower = karakter.islower()
            index = alphabet.index(karakter.lower())
            karakter_enkripsi = alphabet[(index + pergeseran) % 26]

            teks_enkripsi.append(karakter_enkripsi if is_lower else karakter_enkripsi.upper())
        else:
            teks_enkripsi.append(karakter)

    return ''.join(teks_enkripsi)

teks = input("Masukkan String : ")
pergeseran = int(input("Masukkan jumlah pergeseran : "))

print(f"Teks : {teks}")
print(f"Pergeseran : {pergeseran}")
print(f"Sandi : {sandi_caesar(teks, pergeseran)}")