def menghapus_anagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    for karakter in s1:
        if karakter in list2:
            list1.remove(karakter)
            list2.remove(karakter)   
    penghapusan = len(list1) + len(list2)
    return penghapusan
string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")
jumlah_penghapusan = menghapus_anagram(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {jumlah_penghapusan}")