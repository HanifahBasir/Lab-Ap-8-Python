print("Selamat datang di kalkulatur sederhana")
def kalkulator():
    try:
        angka_pertama = int(input("Masukkan angaka pertama = "))
    except ValueError:
        print("Input tidak valid, Masukkan Angka")
    try:
        angka_kedua = int(input("Masukkan angka kedua = "))
    except ValueError:
        print("Input tidak valid, Masukkan Angka")
    sistem = input("Operasi (+, -, *,/) = ")
    if sistem not in ["+", "-", "*","/"]:
        print("Operasi tidak valid. Gunakan +, -, *, atau / ")

    try:
        if sistem =="*":
            print(f"Hasil dari {angka_pertama} {sistem} {angka_kedua} adalah {angka_pertama * angka_kedua}")
        elif sistem == "/":
            if angka_kedua == 0:
                print("Pembagian degan nol tidak diperbolehkan")
            else:
                print(f"Hasil dari {angka_pertama} {sistem} {angka_kedua} adalah {angka_pertama / angka_kedua} ")
        elif sistem == "+":
            print(f"Hasil dari {angka_pertama} {sistem} {angka_kedua} adalah {angka_pertama + angka_kedua}")
        elif sistem == "-":
            print(f"Hasil dari {angka_pertama} {sistem} {angka_kedua} adalah {angka_pertama - angka_kedua}")
    except:
        print("Operasi tidak terdefinisi")
kalkulator()
