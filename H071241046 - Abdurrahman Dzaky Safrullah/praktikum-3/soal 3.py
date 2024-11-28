x = int(input("masukkan x : "))
y = int(input("masukkan y : "))

for i in range(x+1):
    if i % 2 == 0:
        for b in range(y+1):
            print(f"MOVE TO : ({i},{b})")
    else:
        for b in range(y, -1, -1):
            print(f"MOVE TO : ({i},{b})")
                