"""Permainan mencari Harta Karun"""

print("Selamat datang di permainan memburu harta karun!")

def langkah_aman(langkah): # mengecek langkah aman
    return langkah <= 20 # langkah aman adalah 20 kebawah

def main():
    total_jarak = 0 # memulai perhitungan total jarak dari 0
    bahaya_terdeteksi = False

    while True:
        try:
            langkah = input("Masukkan langkah (meter) atau 0 untuk selesai: ")
            langkah = int(langkah)
            
            if langkah == 0:
                break  # berhenti jika input 0
            elif langkah < 0:
                print("Input tidak valid. Masukkan bilangan bulat positif.")
                continue # melewati kondisi dibawah dan mengulang loop jika kondisi terpenuhi
            
            if langkah_aman(langkah):
                total_jarak += langkah
            else:
                bahaya_terdeteksi = True
                print(f"Langkah {langkah} meter terlalu jauh! Ada bahaya.")
        
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat positif.")
            continue # melewati kondisi dibawah dan mengulang loop jika kondisi terpenuhi
    
    # keputusan akhir
    print(f"Total jarak: {total_jarak} meter")
    print(f"Ada bahaya: {'Ya' if bahaya_terdeteksi else 'Tidak'}")
    
    
    if total_jarak == 50 and not bahaya_terdeteksi:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif bahaya_terdeteksi:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")
        
      
main()


