import re
Username = str(input("Masukkan username: "))
if re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{5,20}",Username):
    Email = str(input("Masukkan email: "))
    if re.match(r"^[a-z]+@[a-z]+(|\d{2,})+\.(com|co.id)$",Email):
        Password = str(input("Masukkan Password: "))
        if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{8,}",Password):
            print(f"Registrasi berhasil! Selamat datang, {Username}")
        else:
            print("Password yang kamu masukkan sangat lemah. Registrasi gagal!")
    else:
        print("Email yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("Username yang kamu input tidak memenuhi syarat. Registrasi gagal!")