"""Menentukan jumlah penghapusan karakter untuk menciptakan anagram"""

def jumlah_penghapusan_anagram(s1, s2): 
    total_hapus = 0 #perhitungan dimulai dari 0
    
    # frekuensi huruf dalam string pertama
    for huruf in set(s1):
        count_s1 = s1.count(huruf) #menghitung frekuensi huruf di string pertama
        count_s2 = s2.count(huruf) #menghitung frekuensi huruf yg sama di string kedua
        total_hapus += abs(count_s1 - count_s2) 
    
    # frekuensi huruf yang tidak ada di string pertama
    for huruf in set(s2):
        if huruf not in s1:
            total_hapus += s2.count(huruf)

    return total_hapus

# Input 
s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")

# hasil 
hapus_karakter = jumlah_penghapusan_anagram(s1, s2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hapus_karakter}")
