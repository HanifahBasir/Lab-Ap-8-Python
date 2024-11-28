n=int(input("masukkan jumlah baris: "))

if n % 2 == 1:                           
    for i in range(n):
        if i < n// 2:
            print('  ' * (n // 2 - i ) + '* ' * (2 * i + 1))
        # else:
        #     print('  ' * (i - n // 2 ) + '* ' * (2 * (n - i - 1) + 1))
        
else:                                              
    for i in range(n):
        if i < n // 2:
            print('  ' * (n // 2 - i) + '* ' * (2 * i + 1))
        else:
            print('  ' * ((i - n // 2) + 1  ) + '* ' * (2 * (n - i - 1) + 1))
       
       