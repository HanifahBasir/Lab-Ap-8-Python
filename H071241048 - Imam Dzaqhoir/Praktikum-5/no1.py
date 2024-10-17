def cekpalindrom(input_string):
    input_string = input_string.replace(" ", "").lower()
    if input_string == input_string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


print(cekpalindrom("Kakak"))
print(cekpalindrom("ibu  ratna antar ubi"))
print(cekpalindrom("Hello"))