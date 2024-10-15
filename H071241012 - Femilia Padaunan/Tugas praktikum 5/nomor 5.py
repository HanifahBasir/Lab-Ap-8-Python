def enkripsi_caesar(teks_input, pergeseran):
    teks_enkripsi = ""
    
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for karakter in teks_input:
        if karakter in huruf_kecil:
            indeks = huruf_kecil.index(karakter)
            indeks_baru = (indeks + pergeseran) % 26
            teks_enkripsi += huruf_kecil[indeks_baru]
        elif karakter in huruf_besar:
            indeks = huruf_besar.index(karakter)
            indeks_baru = (indeks + pergeseran) % 26
            teks_enkripsi += huruf_besar[indeks_baru]
        else:
            teks_enkripsi += karakter

    return teks_enkripsi

teks_input = input("Masukkan string: ")
pergeseran = int(input("Masukkan jumlah pergeseran: "))

hasil = enkripsi_caesar(teks_input, pergeseran)

print("Teks :", teks_input)
print("Pergeseran:", pergeseran)
print("Cipher:", hasil)


