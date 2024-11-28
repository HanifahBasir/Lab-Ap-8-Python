from collections import Counter

def anagram(s1, s2):   
    x1 = Counter(s1)
    x2 = Counter(s2)
    
    hapus = 0
    for i in x1:
        if i in x2:
            hapus += abs(x1[i] - x2[i])
        else:
            hapus += x1[i]
            
    for i in  x2:
        if i not in x1:
            hapus +=  x2[i]
            
    return hapus

str1 = input("masukkan string pertama: ")
str2 = input("masukkan string kedua: ")

hasil = anagram(str1, str2)
print(f"jumlah minimum penghapusan untuk membuat anagram: {hasil}")


