jumlah_baris = int(input("masukkan jumlah baris : "))

bintang = "*"

if jumlah_baris <= 0:
    print("masukkan angka yang benar")

elif jumlah_baris % 2 == 0:
    for i in range(jumlah_baris // 2):
        print(" " * (jumlah_baris - i - 1) + bintang * (2 * i + 1) )
        
    for i in  range((jumlah_baris // 2) - 1, -1, -1): 
        print(" " * (jumlah_baris - i - 1) + bintang * (2 * i + 1) )
        
elif jumlah_baris %  2 != 0:
    for i in range((jumlah_baris // 2) + 1 ):
        print(" " * (jumlah_baris - i - 1) + bintang * (2 * i + 1) )
        
    for i in  range((jumlah_baris // 2) - 1, -1, -1):
        print(" " * (jumlah_baris - i - 1) + bintang * (2 * i + 1) )
        
