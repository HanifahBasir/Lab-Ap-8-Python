import os
os.system("cls")

a = int(input("populasi awal serangga a : "))
b = int(input("populasi awal serangga b : "))

hari = int(input("masukkan jumlah hari : "))



if hari <= 0:
    print("MASUKKAN HARI YANG BENAR")
else:
    for i in range(1,hari+1):
        if i % 2 != 0:
            a = int(a*1.3)
            b = int(b*1.5)
        else:
            a = int(a*0.8)
            b = int(b*0.6)
        if i % 5 == 0:
            a = int(a*0.9)
            b = int(b*0.9)
            
        if i % 5 == 0:
            print(f'''hari ke {i} 
                predator sok asik makan 10% bjir
                serangga A = {a}
                serangga B = {b}''')
        else:
            print(f'''hari ke {i}
                serangga A = {a}
                serangga B = {b}''')
                
                
                















                
# Pada hari ganjil, populasi Serangga A bertambah 30%, sedangkan populasi Serangga
# B bertambah 50%. Sedangkan di hari genap, populasi Serangga A berkurang 20%,
# dan populasi Serangga B berkurang 40%. Namun, setiap kelip


# if hari <= 0:
#     print("KHODAMMU LABA LABA JAWA")
# else:
#     for i in range(1,hari+1):
#         if i % 2 != 0:
#             a *= 1.3
#             b *= 1.5
#             print(f'''hari ke {i}















#                 serangga A = {int(a)}
#                 serangga B = {int(b)}''')
#         else:
#             a *= 0.8
#             b *= 0.6
#             print(f'''hari ke {i}
#                 serangga A = {int(a)}
#                 serangga B = {int(b)}''')
#         if i % 5 == 0:
#             a *= 0.9
#             b *= 0.9
#             print(f'''hari ke {i}
#                 si serangga sok asik makan 10%
#                 serangga A = {int(a)}
#                 serangga B = {int(b)}''')
               #  serangga B = {b}''')