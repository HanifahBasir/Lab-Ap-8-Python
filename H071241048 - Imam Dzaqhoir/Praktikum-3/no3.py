
n = int(input("N = "))
m = int(input("M = "))

for i in range(n+1):
    if i%2 == 0:
        for j in range(m+1):
            print(f"MOVE to ({i}),({j})")
    else:
        for j in range (m,-1,-1):
            print(f"MOVE to ({i}),({j})")


