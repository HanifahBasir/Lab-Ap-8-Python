"""Identifikasi IP Adress"""
import re

def check_ip_address(line):
    # Memeriksa apakah string IPv4
    ipv4_pattern = r'^((\d{1,3}\.){3}\d{1,3})$'
    if re.fullmatch(ipv4_pattern, line):
        bagian = line.split('.')
        for i in bagian:
            if not (0 <= int(i) <= 255):
                return "Bukan IP Address"
        return "IPv4"
    # Memeriksa apakah string IPv6
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    if re.fullmatch(ipv6_pattern, line):
        return "IPv6"
    else:
        return "Bukan IP Address"

IP = input("Masukkan alamat IP: ").strip()  # Menghilangkan whitespace 
print(check_ip_address(IP))

    