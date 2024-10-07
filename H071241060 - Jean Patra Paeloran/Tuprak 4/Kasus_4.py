print("Selamat datang di Kalkulator Sederhana!")
try:
    A = float(input("Angka pertama: "))
    try:
        B = float(input("Angka kedua: "))
        try:
            Operator = input("Operasi (+, -, *, /): ")
            if Operator=="+":
                print("Hasil: ",A+B)
            elif Operator=="-":
                print("Hasil: ",A-B)
            elif Operator=="*":
                print("Hasil: ",A*B)
            elif Operator=="/":
                try:
                    print("Hasil: ",A/B)
                except ZeroDivisionError:
                    print("Pembagian dengan nol tidak diperbolehkan")
        except:
            print("operasi tidak valid. Gunakan +, -, *, atau /.")
    except ValueError as b:
        print(f"Input tidak valid: {b}")
except ValueError as a:
    print(f"Input tidak valid: {a}")
