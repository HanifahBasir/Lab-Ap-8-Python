try:
    n = int(input("Masukan angka: "))
    if n>0:
        langkah = 0
        while n!=1:
            if n%2==0:
                n/=2
                print(float(n))
                langkah+=1
            elif n%2!=0:
                n=n*3+1
                print(float(n))
                langkah+=1
        print(f"Jumlah langkah: {langkah}")
    else:
        print("Input harus memasukkan bilangan positif")
except ValueError:
    print("Input tidak Valid")
