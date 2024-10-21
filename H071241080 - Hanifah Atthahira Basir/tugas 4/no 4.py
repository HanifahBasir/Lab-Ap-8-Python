"""Kalkulator Sederhana"""

def kalkulator():
    print("Selamat Datang di Kalkulator Sederhana!")

    # input angka 
    try:
        angka_pertama = float(input('Masukkan Angka Pertama: '))
        angka_kedua = float(input('Masukkan Angka kedua: '))
    except ValueError:
        print(f"Input tidak valid: Masukkan angka")

    # pilih operasi
    operasi = input('Pilih Operasi (+, -, *, /): ')
    if operasi not in ['+', '-', '*', '/']: # list berisi operasi
        print("Operasi tidak valid, gunakan +, -, *, /")
        return
 
    # operasi kalkulator
    if operasi == '+' :
        hasil = angka_pertama + angka_kedua
    elif operasi == '-' :
        hasil = angka_pertama - angka_kedua
    elif operasi == '*' :
        hasil = angka_pertama * angka_kedua
    elif operasi == '/' :
        if angka_kedua == 0:
            print("Pembagian dengan nol tidak diperbolehkan")
            return # menghentikan fungsi jika kondisi diatas terpenuhi
        else: 
            hasil = angka_pertama / angka_kedua
    
    print(f"Hasil: {hasil}")
    
kalkulator()