def inputan():
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))

            if langkah >= 0:
                return langkah
            elif langkah < 0:
                print("Input tidak valid. Masukkan angka positif atau 0 untuk berhenti.")
                continue
            # else:
            #     return langkah
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

def main():
    total_jarak = 0
    bahaya = False

    while True:
        langkah = inputan()

        if langkah == 0:
            break
        if langkah > 20:
            bahaya = True

        total_jarak += langkah

    print(f"Total jarak: {total_jarak} meter")
    print(f"Ada bahaya: {'Ya' if bahaya else 'Tidak'}")

    if bahaya:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

main()