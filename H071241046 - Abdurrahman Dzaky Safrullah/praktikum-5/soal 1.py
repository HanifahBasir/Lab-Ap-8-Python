import os
os.system("cls")

def palindrome(kata:str) -> str:
    # kata = kata.lower()
    if ("".join(kata.split())).lower() == ("".join("".join(reversed(kata)).split())).lower():
        print(f"ADALAH PALINDROME")
    else:
        print(f"BUKAN PALINDROME")
        
palindrome("race car")


# kata = "Ibu  Ratna Antar Ubi"
# print(("".join(kata.split())).upper())

