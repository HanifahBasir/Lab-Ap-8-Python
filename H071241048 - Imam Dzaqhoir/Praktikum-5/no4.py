def semua_substring(input_string):
    lis = []
    length = len(input_string)

    for i in range(1,length+1):
        for j in range(length-i + 1):
            lis.append(input_string[j:j+i])

    return lis

input_string = input("Input your string: ")
print("=" * 25)

substrings = semua_substring(input_string)
for i in substrings:
    print(i)