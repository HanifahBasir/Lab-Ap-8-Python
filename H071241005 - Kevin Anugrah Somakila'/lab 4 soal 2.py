def mencari_hartaKarun():
    total_jarak = 0
    bahaya = False

    while True:
        jarak_langkah = input("Masukkan langkah (meter) atau 0 untuk berhenti: ")
        try:
            jarak_langkah = int(jarak_langkah)
            if jarak_langkah < 0:
                print("Input tidak valid.")
                continue
            if jarak_langkah == 0:
                break
            total_jarak += jarak_langkah
            if jarak_langkah > 20:
                bahaya = True
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    print(f"Total jarak: {total_jarak} meter")
    
    if total_jarak == 50 and not bahaya:
        print("Ada bahaya: Tidak")
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    elif bahaya:
        print("Ada bahaya: Ya")
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

mencari_hartaKarun()
