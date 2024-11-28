String = input("Input your string : ")
print("="*20)
panjang = len(String)
for i in range(1,panjang+1):
    for j in range(panjang-i+1):
        print(String[j:j+i])