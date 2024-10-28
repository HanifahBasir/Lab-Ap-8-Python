import re
User = input("= ")
pola = r'[a-zA-Z02468]{40}[13579\s]{5}'
valid = re.match(pola, User) != None

print('True' if len(User) == 45 and valid else 'False')
