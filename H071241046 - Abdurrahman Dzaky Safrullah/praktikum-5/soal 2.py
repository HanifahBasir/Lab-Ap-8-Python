import os
os.system('cls')

def akronim(kata:str) -> str :
    ambil = "".join([i[0] for i in kata.split()])
    print(ambil.upper())
    
akronim('negara kesatuan republik indonesia')