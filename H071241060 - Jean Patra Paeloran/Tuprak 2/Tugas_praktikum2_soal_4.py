data = int(input("Masukkan jumlah data yang digunakan (GB): "))
jam = str(input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? "))
pengguna = str(input("Apakah anda pengguna Personal atau Bisnis? "))
if pengguna=="Personal" and jam=="off-peak"and data<10:
    print("Paket yang sesuai: Paket A")
elif 10<=data<=50 and jam=="peak" and pengguna=="Personal":
    print("Paket yang sesuai: Paket B")
elif data>50 and jam=="peak" and (pengguna=="Personal" or pengguna=="Bisnis"):
    print("Paket yang sesuai: Paket C")
elif data>50 and jam=="off-peak" and pengguna=="Bisnis":
    print("Paket yang sesuai: Paket D")
else:
    print("Tidak ada paket yang cocok")