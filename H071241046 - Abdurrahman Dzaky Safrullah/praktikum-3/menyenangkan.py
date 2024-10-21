import os
from pydoc import cli
os.system("cls")


###### DETEKSI BILANGAN PRIMA

'''
Bilangan prima adalah bilangan yang lebih besar dari 1 dan hanya bisa dibagi dengan bilangan 1 dan bilangan itu sendiri,

4, 1 

4, , k 3 2 , kalau misal 4 habis dibagi bilangan sebelum 4 maka dia bukan bilangan prima


'''

is_prima = True

while True:
    n = input("masukkan bilangan : ")
    if n == "stop":
        break
    
    if int(n) < 2 :
        print("bukan bilangan prima")
        continue
    # elif n == 'stop':
    #     break
    else:
        for i in range(2, int(n)):
            if int(n) % i == 0:
                is_prima = False
                break
                # print("bukan bilangan prima")
                # break
            else :
                is_prima = True
        if is_prima:
            print("Bilangan prima")
        else:
            print("Bukan bilangan prima")
            
                
            
 
       