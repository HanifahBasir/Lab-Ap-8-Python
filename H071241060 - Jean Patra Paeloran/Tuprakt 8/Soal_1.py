import re
String = str(input(""))
Kebenaran = True
if not re.fullmatch(r"[A-Za-z02468]{40}[13579\s]{5}",String):
        Kebenaran = False
print(Kebenaran)