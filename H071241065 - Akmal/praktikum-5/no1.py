def palindrome(s1):
    if s1 == s1[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
try:
    s1 = input("masukkan sebuah kata/kalimat: ")
except KeyError:
    print("input tidak valid")
else:
    print(palindrome(s1)) 