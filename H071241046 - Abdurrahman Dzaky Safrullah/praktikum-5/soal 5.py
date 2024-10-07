import os
os.system("cls")

alfabet = "abcdefghijklmnopqrstuvwxyz"
# print(len(alfabet))
string = input("masukkan kata : ")
geser = int(input("masukkan shift : "))

kata = string.lower()
hasil = ""

for i in kata:

    if i in alfabet: 
        indeks = alfabet.index(i)
        new = (indeks + geser) % 26
        hasil += alfabet[new]
    else:
        hasil += i

print(f"Text: {string}")
print(f"Shift: {geser}")
print(f"hasil: {hasil}")