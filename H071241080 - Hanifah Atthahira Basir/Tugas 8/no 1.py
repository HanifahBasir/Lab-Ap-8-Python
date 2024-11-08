"""Validasi String"""
import re

def is_valid_str(string):
    # 1-40: huruf atau angka genap, 41-45: angka ganjil atau whitespace
    pattern = r"^[A-Za-z02468]{40}[13579\s]{5}$" 
    return re.fullmatch(pattern, string)

string = input("Masukkan string sesuai dengan ketentuan: ")
if is_valid_str(string):
    print("True")
else:
    print("False")




