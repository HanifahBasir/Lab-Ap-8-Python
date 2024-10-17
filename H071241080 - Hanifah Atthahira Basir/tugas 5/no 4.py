"""Program untuk menampilkan semua substring dari sebuah string"""

def substring(kata):
    panjang = len(kata)
    
    for i in range(panjang): #menentukan panjang substring
        for j in range(i + 1, panjang + 1): #menghasilkan substring dari panjang yang telah ditentukan
            print(kata[i:j])

kata = input("Masukkan string: ")

substring(kata)

