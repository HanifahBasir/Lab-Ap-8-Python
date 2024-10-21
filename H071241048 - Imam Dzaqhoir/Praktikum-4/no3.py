def main():
    try:
        n = float(input("Masukkan angka: "))
        if n <= 0:
            print("Input tidak Valid")
            return
    except ValueError:
        print(f"Input tidak Valid. Harus bilangan bulat positif cuyy!")
        return

    langkah = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        langkah += 1
        print(f"n = {n}")

    print(f"Jumlah langkah: {langkah}")

main()