def jarak(kartu):
    return sum(kartu)
def game():
    kartu = []
    bahaya = "Tidak"
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if langkah==0:
                break
            elif langkah>20:
                kartu.append(langkah)
                bahaya = "Ya"
            elif langkah>0:
                kartu.append(langkah)
        except ValueError:
            print("Input tidak valid. Masukan bilangan bulat.")
    print(f"Total jarak: {jarak(kartu)}")
    print(f"ada bahaya: {bahaya}")
    if bahaya=="Ya":
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif jarak(kartu)==50:
        print("Keputusan: Aman!Kamu tepat menemukan harta karun dan menang!")
    elif jarak(kartu)!=50:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
            
game()