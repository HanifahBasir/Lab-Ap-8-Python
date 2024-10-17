# konversi jumlah detik ke jam
jumlah_detik = int(input("masukkan_jumlah_detik : "))
# 7550
# menghitung konversi jumlah detik ke jam : menit : detik
jam = int(jumlah_detik /  3600)
# menit = int(jumlah_detik % 3600) // 60
detik = int(jumlah_detik % 60)

print(f"{jam}:{detik}")