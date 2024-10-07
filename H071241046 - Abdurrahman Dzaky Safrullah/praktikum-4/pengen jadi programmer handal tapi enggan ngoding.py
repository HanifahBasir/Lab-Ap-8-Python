import os
os.system("cls")

def operasi(angka1:int, angka2:int, operation:int) -> int:
    if operation == "+":
        return angka1 + angka2
    elif operation == "!":
        if angka1 < 0:
            return "apalah kau ini, kasih masuk angka positiflah"
        result = 1
        facto = angka1 
        while facto > 0:
            result *= facto  # i1 hasil = 1 * 5 , i2 hasil = 5 * 4 , i3 = 20 * 3 dst
            facto -= 1
        return result
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
    c = input("Masukkan operasi (+, -, *, /, !) : ")
    if c != "+" and c != "-" and c != "*" and c != "/" and c != "!":
        print("Masukkan operasi yang valid (+, -, *, /,)")
    else:
        print(f"hasil = {operasi(a,b,c)}")