N = int(input("nilai N: "))
M = int(input("nilai M: "))
for m in range (0, N):
    if m % 2  == 0:
        for i in range (0, M):
            print(f"Move to {m},{i}")
    else:
        for i in range(M-1, -1,-1):
            print(f"Move to {m},{i}") 