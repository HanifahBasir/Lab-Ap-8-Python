import re

def IP_address(ip):
    if "." in ip:
        bagian = ip.split(".")
        if len(bagian) == 4: 
            for b in bagian:
                if not b.isdigit() or not (0 <= int(b) <= 255):
                    return "Bukan IP Address"
            return "IPv4"

    elif ":" in ip:
        bagian = ip.split(":")
        if len(bagian) == 8: 
            for b in bagian:
                if not re.match(r"^[0-9a-fA-F]{1,4}$", b):
                    return "Bukan IP Address"
            return "IPv6"

    return "Bukan IP Address"

N = int(input("Masukkan jumlah baris: "))
for _ in range(N):
    ip_input = input("Masukkan alamat IP: ").strip()
    print(IP_address(ip_input))





