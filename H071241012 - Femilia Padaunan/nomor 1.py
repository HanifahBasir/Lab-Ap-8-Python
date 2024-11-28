import re

def validasi_string(sebuah_String):

    if len(sebuah_String) != 45:
        return False

    pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'
    return re.match(pattern, sebuah_String)
    

sebuah_string = input("Masukkan string: ")
if validasi_string(sebuah_string):
    print("True")
else:
    print("False")







