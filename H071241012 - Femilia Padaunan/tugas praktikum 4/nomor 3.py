def hitung_langkah(n):
    langkah_langkah = [ ]
    if n <= 0:
        return "Input tidak Valid"
    
    while n != 1:
        if n % 2 == 0:  
            n = n // 2
        else:  
            n = n * 3 + 1
        langkah_langkah.append(n)
    
    return langkah_langkah

def main():
    try:
        n = int(input("Masukkan angka: "))
        if n <= 0:
            print("Input tidak Valid")
        else:
            langkah = hitung_langkah(n)
            print("Langkah-langkah:")
            for step in langkah:
                print(step)
            print(f"Jumlah langkah: {len(langkah)}")
    except ValueError:
        print("Input tidak Valid")


main()

