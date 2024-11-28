import os
os.system("cls")

from collections import Counter as ambatron

def min_anagram(str1="q", str2="s"):
    
    str1 = input("masukkan input 1 : ")
    str2 = input("masukkan input 2 : ")
    
    # Hitung frekuensi kcarakter dalam kedua string
    count1 = ambatron(str1) 
    count2 = ambatron(str2)

    # Hitung jumlah karakter yang perlu dihapus
    deletions = 0
    
    # Daftar semua karakter unik dari kedua string
    all_chars = set(list(count1.keys()) + list(count2.keys()))
    
    # Hitung selisih frekuensi untuk setiap karakter
    for char in all_chars:
        freq1 = count1[char] if char in count1 else 0
        freq2 = count2[char] if char in count2 else 0
        difference = abs(freq1 - freq2)
        deletions += difference



    print(deletions)

min_anagram()


