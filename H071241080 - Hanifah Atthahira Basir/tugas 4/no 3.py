"""Teka-Teki Matematika"""

def hitung_langkah(n):
    langkah = 0 # memulai perhitungan langkah dari 0
   
    while n != 1: # loop akan berjalan selama n belum mencapai 1
       print(float(n)) # mencetak nilai n
       if n % 2 == 0: # jika n genap
           n /= 2 # nilai n dibagi 2
       else: # jika n ganjil
           n = 3 * n + 1 # nilai n dikali 3 dan ditambah 1
       langkah += 1 # tambah langkah setiap operasi dilakukan
   
    print(float(n)) # mencetak angka 1 dibagian akhir
    return langkah
  
def main():
    try:
        n = int(input("Masukkan angka: "))
        if n <= 0: # memastikan input lebih besar dari 0
            print("Input tidak valid")
        else:
            jumlah_langkah = hitung_langkah(n)
            print(f"Jumlah langkah: {jumlah_langkah}")
    except ValueError:
        print("Input tidak valid")        
        
main()        
