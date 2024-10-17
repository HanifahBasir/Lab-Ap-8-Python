data = int(input("masukkan jumlah data yang digunakan(GB): "))
waktu=(input("apakah mayoritas penggunaan di luar jam sibuk(off-peak) atau  di jam sibuk(peak)?: "))
jenis_pengguna=(input("apakah anda pengguna bisnis atau personal?: "))

if jenis_pengguna == "personal":
    if data < 10 and waktu =="off-peak":
        print("paket yang sesuai: paket A")
    elif 10 <= data <=50 and waktu =="peak":
        print("paket yang sesuai : paket B")
    elif data>50 and waktu =="peak":
        print("paket yang sesuai : paket C")
    else:
        print("tidak ada paket yang sesuai")
elif jenis_pengguna == "bisnis":
    if data >50 and waktu=="peak":
        print("paket yang sesuai D")
    elif data>50 and waktu == "off-peak":
        print("paket yang sesuai : paket C")
    else:
        print("tidak  ada paket yang sesuai")

else:
    print("tidak ada paket yang sesuai")