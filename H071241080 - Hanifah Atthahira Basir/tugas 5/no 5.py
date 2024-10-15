"""Kriptografi"""

def caesar_cipher(text, shift):
    hasil = ''
    
    for char in text:
        if char.isalpha():  # apakah karakter adalah huruf
            # Tentukan kode numerik berdasarkan huruf kecil atau besar
            offset = ord('a') if char.islower() else ord('A')
            # Geser huruf
            hasil += chr((ord(char) - offset + shift) % 26 + offset)
        else: # selain huruf dibiarkan tetap
            hasil += char  

    return hasil

# input 
text = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))

# hasil 
print("text:", text)
print("shift:", shift)
print("Cipher:", caesar_cipher(text, shift))

