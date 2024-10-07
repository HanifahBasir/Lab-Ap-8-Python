
while True :
    num = input("cek bilangan prima: ")
    cek = False

    if num == "stop":
        break
    elif int(num) < 0:
        print("Harus bilangan Riil kocakk")
    elif int(num) == 0 or int(num) == 1:
        print(int(num), "Bukan bilangan Prima")
    elif int(num) > 1:
        for i in range(2, int(num)):
            if (int(num) % i) == 0:
                cek = True
                break

        if cek:
            print(int(num), "Bukan bilangan Prima")
        else:
            print(int(num), "Bilangan Prima")

