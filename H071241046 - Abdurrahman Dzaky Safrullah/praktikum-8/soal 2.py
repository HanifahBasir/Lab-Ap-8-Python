import re

def cek(n="a"):
    
    print("akan ada 3 inputan untuk mengecek apakah IPv4, IPv6, atau bukan keduanya")

    a = input("inputan 1\n->")
    b = input("inputan 2\n->")
    c = input("inputan 3\n->")
    
    print("\n\n")
    # a
    if len(a) <= 500:
        print("inputan 1:")
        v4 = a.split(".")
        if len(v4) == 4:
            is_v4 = True
            for digit in v4:
                try:
                    apalah = int(digit)
                    if apalah > 255:
                        is_v4 = False
                        break
                except ValueError:
                    is_v4 = False
                    break
            if is_v4 and re.fullmatch(r"([\d]+\.){3}[0-9]+" , a):
                print("IPv4")
            else:
                print("bukan IP address")
        # elif re.fullmatch(r"([\d]+\.){3}[0-9]+" , a):
        #     print('IPv4')
        elif re.fullmatch(r'([a-f\d]+:){7}[a-f\d]{4}', a ):
            print("IPv6")
        else:
            print("bukan IP address")
    else:
        raise ValueError("jumlah karakter dari inp 1 tidak boleh lebih dari 100")

    ## b
    if len(b) <= 500:
        print("inputan 2:")
        v4 = b.split(".")
        if len(v4) == 4:
            is_v4 = True
            for digit in v4:
                try:
                    apalah = int(digit)
                    if apalah > 255:
                        is_v4 = False
                        break
                except ValueError:
                    is_v4 = False
                    break
            if is_v4 and re.fullmatch(r"([\d]+\.){3}[0-9]+" , b):
                print("IPv4")
            else:
                print("bukan IP address")
        elif re.fullmatch(r'([a-f\d]+:){7}[a-f\d]{4}', b ):
            print("IPv6")
        else:
            print("bukan IP address")
    else:
        raise ValueError("jumlah karakter dari inp 1 tidak boleh lebih dari 100")

        
    ## c
    if len(c) <= 500:
        print("inputan 3:")
        v4 = c.split(".")
        if len(v4) == 4:
            is_v4 = True
            for digit in v4:
                try:
                    apalah = int(digit)
                    if apalah > 255:
                        is_v4 = False
                        break
                except ValueError:
                    is_v4 = False
                    break
            if is_v4 and re.fullmatch(r"([\d]+\.){3}[0-9]+" , a):
                print("IPv4")
            else:
                print("bukan IP address")
        elif re.fullmatch(r'([a-f\d]+:){7}[a-f\d]{4}', c ):
            print("IPv6")
        else:
            print("bukan IP address" or "")
    else:
        raise ValueError("jumlah karakter dari inp 1 tidak boleh lebih dari 100")
    
cek()
