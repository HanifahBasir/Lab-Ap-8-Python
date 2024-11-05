import re
def pengetesan_TI():
    pattern=r'^[a-zA-Z2468]{40}[13579\s]{5}$'
    while True:
        inputuser=input("= " )
        if re.match(pattern,inputuser) :
            if len(inputuser)==45:
                print("True")
                break
        else :
            print("False")

pengetesan_TI()