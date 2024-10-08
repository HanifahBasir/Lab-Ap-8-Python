def tekateki():
    try:
        m = int(input("Masukkan angka = "))
    except ValueError:
        print("Masukkan angka yang benar. ")
        return
    langkah = 0
    while m != 1:
        if m % 2 == 0:
            m = m //2
        else:
            m = m * 3 + 1
        langkah += 1
        print(m)
    print(f"Jumlah langkah yang diperlukan = {langkah}")
tekateki()