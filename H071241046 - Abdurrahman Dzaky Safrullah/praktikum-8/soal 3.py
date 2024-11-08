import re

def regis(fadil_bayangan="oomagad"):
    
    user = input("masukkan username:")
    email = input("masukkan email : ")
    password = input("masukkan password : ")
    
    is_true = False
    
    #user
    if 5<=len(user)<=20:
        if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).+", user):
        # if re.fullmatch(r"^[0-9a-zA-Z]{$", user):
            is_true = True
        else:
            return "username tidak valid!!!"
    else:
        return "panjang username minimal 5 karakter dan maksimal 20 karakter!!!"
    
    if len(email) > 0:
        if re.fullmatch(r"[a-z]+\d+@[a-z]+((\.com)|(\.co\.id))", email): # (\.[a-z]{2,})+
            is_true = True
        else:
            return "email tidak valid!!!"
    else:
        return "email tidak boleh kosong!!!"
    
    if len(password) > 7:
        if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).+", password):
            is_true = True
        else:
            return "password tidak valid!!!"
    else:
        return "panjang password minmal 8!!!"   
    
    if is_true:
        return f"Rgistrasi berhasil, selamat datang '{user}'!"

print(regis())