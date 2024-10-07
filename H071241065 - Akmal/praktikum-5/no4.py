def fungsi(s):
    n = len(s)
    for j in range(1, n + 1):  
        for i in range(n - j + 1):  
            print(s[i:i + j])
            

string = input("Input your string: ")
fungsi(string)
