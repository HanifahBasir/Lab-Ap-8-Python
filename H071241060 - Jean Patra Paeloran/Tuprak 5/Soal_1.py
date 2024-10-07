def polindrome(palindrom):
    A = palindrom.lower()
    B = palindrom[::-1].lower()
    if A==B:
        print("Palindrome")
    else:
        print("Not Palindrom")
polindrome(input())      