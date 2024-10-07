

karakter = input("Masukkan karakter yang dicari : ")
kalimat = input("Masukkan kalimat yang dicari : ")

hasil = karakter in kalimat

print((f"{karakter} bukan bagian dari '{kalimat}'", f"{karakter} merupakan bagian dari '{kalimat}'")[hasil])