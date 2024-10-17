def kalkulator():
    print("Selamat datang di kalkulator sederhana!")

    try:
        angka_pertama = float(input("Masukkan angka pertama: "))
        angka_kedua = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
        return
    
    operasi = input("Operasi (+, -, *, /): ")

    if operasi == "+":
        hasil = angka_pertama + angka_kedua
        print(f"Hasil tambah: {hasil}")
    elif operasi == "-":
        hasil = angka_pertama - angka_kedua
        print(f"Hasil kurang: {hasil}")
    elif operasi == "*":
        hasil = angka_pertama * angka_kedua
        print(f"Hasil kali: {hasil}")
    elif operasi == "/":
        if angka_kedua != 0:
            hasil = angka_pertama / angka_kedua
            print(f"Hasil bagi: {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Pilihan operasi tidak valid.")

kalkulator()


    
    
   

    

   
   