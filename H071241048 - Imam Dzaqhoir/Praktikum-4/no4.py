def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")

    try:
        no1 = float(input("Angka pertama: "))
        no2 = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return

    operasi = input("Operasi (+, -, *, /): ")

    if operasi == "+":
        hasil = no1 + no2
        print(f"Hasil: {hasil:.0f}")
    elif operasi == "-":
        hasil = no1 - no2
        print(f"Hasil: {hasil:.0f}")
    elif operasi == "*":
        hasil = no1 * no2
        print(f"Hasil: {hasil:.0f}")
    elif operasi == "/":
        if no2 == 0:
            print('Pembagian dengan nol tidak diperbolehkan.')
        else:
            hasil = no1 / no2
            print(f"Hasil: {hasil:.0f}")
    else:
        print("Operasi tidak valid. (Gunakan +, -, *, atau /)")

kalkulator()