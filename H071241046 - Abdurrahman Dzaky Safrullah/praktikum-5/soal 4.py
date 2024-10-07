import os
os.system("cls")

# kata = "mipa"

# print(kata[0:1])
# print(kata[1:2])
# print(kata[2:3])
# print(kata[3:4])
# print(kata[0:2])
# print(kata[1:3])
# print(kata[2:4])
# print(kata[0:3])
# print(kata[1:4])
# print(kata[0:4])

kata = input("silahkan masukkan string : ")
n = len(kata)

for panjang in range(1, n+1):         
    for i in range(n - panjang + 1):  
        print(kata[i:i+panjang])      
