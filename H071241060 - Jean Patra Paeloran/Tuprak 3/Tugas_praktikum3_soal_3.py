N = int(input("N = "))
M = int(input("M = "))
for i in range(0,N+1):
    if i%2==1:
        for j in range(M,-1,-1):
            print(f"MOVE to ({i},{j})")
    else:
        for j in range(0,M+1):
            print(f"MOVE to ({i},{j})")