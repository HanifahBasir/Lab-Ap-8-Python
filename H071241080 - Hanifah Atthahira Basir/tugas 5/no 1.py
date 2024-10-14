"""Program untuk mengecek apakah sebuah string adalah Palindrome"""

def Palindrome(kata):
   
    kata = kata.lower() #mengubah input menjadi huruf kecil
    
    if kata == kata[::-1]: #cek palindrome
        print("Palindrome")
    else:
        print("Bukan Palindrome")

Palindrome("ajaja")  


