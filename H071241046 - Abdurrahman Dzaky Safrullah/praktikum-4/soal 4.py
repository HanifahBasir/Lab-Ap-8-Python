import os
os.system("cls")


def operasi(angka1, angka2, operation):
    if operation == "+":
        return angka1 + angka2
    elif operation == "-":
        return angka1 - angka2
    elif operation == "*":
        return angka1 * angka2
    elif operation == "/":
        try:    
            return angka1 / angka2
        except ZeroDivisionError:
            return "pembagian dengan angka 0 tidak diperbolehkan"
        
    
try:
    a = int(input("Masukkan angka pertama : "))
    b = int(input("Masukkan angka kedua : "))
except ValueError:
    print("Input tidak valid! Masukkan angka(int)")
else:
    c = input("Masukkan operasi (+, -, *, /,) : ")
    if c != "+" and c != "-" and c != "*" and c != "/":
        print("Masukkan operasi yang valid (+, -, *, /,)")
    else:
        print(f"hasil = {operasi(a,b,c)}")