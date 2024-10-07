String1 = input("Masukkan string pertama: ")
String2 = input("Masukkan string kedua: ")
Hapus = 0
for char in String1:
    if char in String2:
        String2 = String2.replace(char,"",1)
    else:
        Hapus+=1
Hapus+=len(String2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {Hapus}")