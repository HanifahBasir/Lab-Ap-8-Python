n = int(input("baris : "))
m = n
for i in range(n):
    if i%2==1:
        bintang = "*"
        spasi = " "*i
        baris = bintang+spasi+bintang
        tambahan = " "
        print(baris.center(n*3-1," "))
    else:
        bintang = "*"
        spasi = " "*i
        baris = bintang+spasi+bintang
        tambahan = " "
        print(baris.center(n*3," "))
    

