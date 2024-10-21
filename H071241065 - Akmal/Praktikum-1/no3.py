

waktu = int(input("masukkan detik :"))

jam = waktu // 3600
menit = waktu % 3600 // 60
detik = waktu % 60

print(f"{jam:02}:{menit:02}:{detik:02}")
