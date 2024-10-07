print("konversi detik ke jam")
jumlah_detik = int(input("Masukkan jumlah detik:"))
jam = str(jumlah_detik//3600).zfill(2) # ditambahi %24 setelah 3600 jika termasuk menghitung hari
menit = str((jumlah_detik%3600)//60).zfill(2)
detik = str(jumlah_detik%60).zfill(2)
# hari = jumlah_detik//3600//24
print(f"{jam}:{menit}:{detik}")
# print("jumlah hari:", hari)