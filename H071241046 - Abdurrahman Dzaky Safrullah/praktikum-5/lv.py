import os
os.system("cls")

alfabet = "azabybcxcdwdevefufgtghahirijqjkpklolmnm"

string = input("masukkan kata : ")
geser = 1

kata = string.lower()
hasil = ""

for i in kata:

    if i in alfabet: 
        indeks = alfabet.index(i)
        new = (indeks + geser) % 39
        hasil += alfabet[new]
    else:
        hasil += i

print(f"Text: {string}")
# print(f"Shift: {geser}")
print(f"az: {hasil}")

