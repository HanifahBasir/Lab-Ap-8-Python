def acronym(s1):
    s1 = [x for x in s1 if x.isupper()]
    s2 = "".join(s1)
    print(s2)
try:
    s1 = input("masukkan kata: ")
except KeyError:
    print("input tidak valid")
else:
    acronym(s1)