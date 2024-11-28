def karakter_spesial(teks):
    return ''.join(filter(str.isalnum, teks))

string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

string1 = karakter_spesial(string1)
string2 = karakter_spesial(string2)

penghapusan = 0

string = set(string1) | set(string2)
for char in string:
    penghapusan += abs(string1.count(char) - string2.count(char))
    

print(f"Jumlah minimum penghapusan untuk membuat anagram: {penghapusan}")
