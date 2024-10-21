
def kalkulator(angka_pertama, angka_kedua, operasi):
    if operasi == '+':
        return angka_pertama + angka_kedua
    elif  operasi == '-':
        return angka_pertama - angka_kedua
    elif operasi == '*':
        return angka_pertama * angka_kedua
    elif operasi == '/':
        if angka_kedua == 0:
            return "pembagian dengan 0 tidak diperbolehkan"
        else:
            return  angka_pertama / angka_kedua
    elif operasi == "!":
        x = angka_pertama ** 0.3333333333333
        return f"akar {x} "
    
        
        
try:
    pertama = int(input("angka pertama: "))
    kedua =  int(input("angka kedua: "))
    operasi = input("operasi (+,-,*,/,!): ")
except ValueError:
    print("harus angka")
else:
    print(kalkulator(pertama, kedua, operasi))




