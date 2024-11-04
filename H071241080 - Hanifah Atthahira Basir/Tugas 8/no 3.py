"""Validasi Registrasi Akun"""
import re

def is_valid_username(username):
    # 5-20 karakter, hanya huruf dan angka.
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)

def is_valid_email(email):
    # diawali huruf kecil, diikuti karakter bebas, dan domain yang valid.
    pattern = r"^[a-z0-9]+@[a-z]+\.(com|co\.id)$"
    return re.search(pattern, email)

def is_valid_password(password):
    # minimal 8 karakter, harus mengandung setidaknya satu huruf kapital,
    # satu huruf kecil, dan satu angka, tanpa simbol khusus.
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.search(pattern, password)

username = input("Masukkan username: ")
if is_valid_username(username):
    email = input("Masukkan email: ")
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! Halo {username}.")  
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal.")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal.")
