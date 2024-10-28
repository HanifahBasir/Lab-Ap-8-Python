import re
Hasil =[]
ipv4 = r'([0-9]{1,3}\.){3}[0-9]{1,3}'
ipv6 = r'([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})'
Baris = int(input("N: "))
for i in range (Baris):
    Ip = str(input("Ip: "))
    if not len(Ip)<=500:
        print("Karakter lebih dari 500")
    else:
        if re.match(ipv4, Ip):
            Sampel = Ip.split('.')
            kebenaran = False
            for i in Sampel:
                if len(Sampel)!=4:
                    Hasil.append("Bukan IP Address")
                    break
                elif not (0 <= int(i) <= 255):
                    Hasil.append("Bukan IP Address")
                    break
                else:
                    kebenaran = True
            if kebenaran:
                Hasil.append("IPv4")
        elif re.fullmatch(ipv6, Ip):
            Hasil.append("IPv6")
        else:
            Hasil.append("Bukan IP Address")
for i in Hasil:
    print(i)