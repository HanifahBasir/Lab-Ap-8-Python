
n = int(input("masukkan jumlah baris yang ingin ditampilkan = "))
m = n +1
for i in range(1,(m + 1)//2):
    print('  ' * (n-i) + '* ' * (2*i-1))

for i in range((m//2),0,-1):
    print('  ' * (n-i) + '* ' * (2*i-1))
