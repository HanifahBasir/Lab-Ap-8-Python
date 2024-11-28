print("""Penggunaan Data: 
• Penggunaan Ringan: Di bawah 10 GB per bulan. 
• Penggunaan Sedang: 10 GB hingga 50 GB per bulan. 
• Penggunaan Berat: Lebih dari 50 GB per bulan. 
Waktu Penggunaan: 
• Penggunaan di Luar Jam Sibuk (Off-Peak): Penggunaan data antara jam 11 malam hingga 7 pagi. 
• Penggunaan di Jam Sibuk (Peak): Penggunaan data di luar jam 11 malam hingga 7 pagi. 
Jenis Pengguna: 
• Pengguna Personal: Menggunakan internet untuk keperluan sehari-hari seperti browsing, streaming, dan media sosial. 
• Pengguna Bisnis: Menggunakan internet untuk keperluan bisnis seperti video conference, hosting website, dan cloud services. 
Paket Layanan yang Ditawarkan: 
• Paket A: Untuk Penggunaan Ringan dengan mayoritas penggunaan di Luar Jam Sibuk oleh Pengguna Personal. 
• Paket B: Untuk Penggunaan Sedang dengan mayoritas penggunaan di Jam Sibuk oleh Pengguna Personal. 
• Paket C: Untuk Penggunaan Berat oleh Pengguna Personal atau Bisnis yang mayoritas penggunaannya di Jam Sibuk. 
• Paket D: Untuk Penggunaan Berat dengan mayoritas penggunaan di Luar Jam Sibuk oleh Pengguna Bisnis.""")



penggunaan_data = int(input("masukkan jumlah data yang digunakan per bulan (GB) : "))
waktu_pengguna = input("apakah mayoritas penggunaa di luar jam spenggibuk (off-peak) atau di jam sibuk (peak)?" ).lower()
jenis_pengguna = input("apakah anda pengguna personal atau bisnis?").lower()



if penggunaan_data < 10 and waktu_pengguna  == "off-peak" and jenis_pengguna == "personal":
    print("paket yang sesuai: paket A")
elif 10 <= penggunaan_data <= 50 and  waktu_pengguna == "peak" and jenis_pengguna == "personal":
    print("paket yang sesuai: paket B")
elif penggunaan_data > 50 and waktu_pengguna == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis") :
    print("paket yang sesuai: paket C")
elif penggunaan_data > 50 and waktu_pengguna == "off-peak" and jenis_pengguna == "bisnis":
    print("paket yang sesuai: paket D")
else:
    print("tidak ada paket yang cocok")