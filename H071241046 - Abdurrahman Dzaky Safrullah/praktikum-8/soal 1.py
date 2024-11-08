import re

def soal_1(a:str="a") -> bool:
    
    a = input("masukkan string (len = 45) : ")
    
    if len(a) != 45:
        return "panjang tidak sesuai"
    
    if not re.search(r"[13579\s]{5}$", a):
        return "tidak valid"
    
    else:
        return True
    
print(soal_1())