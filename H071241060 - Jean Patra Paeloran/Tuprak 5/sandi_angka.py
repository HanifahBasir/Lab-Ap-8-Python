
sandi = input("Masukkan sandi: ")
Hasil = ""
for char in sandi:
    if char.isalpha():
        if char.isupper():
            A = ord(char)-64
            Hasil += str(A)
        elif char.islower():
            A = ord(char)-96
            Hasil += str(A)
    elif char.isnumeric():
        A = chr(int(char)+64)
        Hasil += A
print(Hasil)