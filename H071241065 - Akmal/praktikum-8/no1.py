import re

pattern = "^([A-Za-z]|[02468]){40}[ 13579]{5}$"
input_string = input("masukkan string: ")
result = re.match(pattern, input_string)

if result:
    print(True)
else:
    print(False)



