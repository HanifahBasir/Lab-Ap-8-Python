###### SOAL 1
###### SEGITIGA


a = int(input("masukkan sisi a : "))
b = int(input("masukkan sisi b : "))
c = int(input("masukkan sisi c : "))

print(f'''
sisi a = {a}
sisi b = {b}
sisi c = {c} 
''')

if a + b <= c or a + c <= b or b + c <= a:
    print("Tidak dapat membentuk sigitiga yang valid")
elif a <= 0 or b <= 0 or c <= 0:
    print("Tidak dapat membentuk sigitiga yang valid")
elif a == b == c :
    print("Membentuk segitika sama sisi")
elif a == b or a == c or b == c:
    print("Membentuk segitiga sama kaki")
else:
    print("Membentuk segitiga sembarang")