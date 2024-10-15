def menampilkan_substring(string):
    panjang = len(string)
    for i in range(1, panjang + 1):  
        for j in range(panjang):  
            if j + i <= panjang:  
                print(string[j:j + i])  

masukkan_string = input("Input Your String: ")
print("========================")
menampilkan_substring(masukkan_string)


