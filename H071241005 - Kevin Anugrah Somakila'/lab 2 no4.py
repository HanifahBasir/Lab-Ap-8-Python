data = int(input("Masukkan jumlah data yang digunakan (GB): "))
jam_pengunaan = input("Apakan mayoritass pengguanaan diluar jam sibuk (off-peak) atau di jam sibuk (peak)?: ")
pengunaan_data = input("Anda penguna personal atau bisnis?: ") 

#jenis paket
if pengunaan_data == "personal":
    if data<10 and jam_pengunaan == "off-peak":
        paket = "Paket A"
    elif 10<= data <=50 and jam_pengunaan == "peak":
        paket = "Paket B"
    elif data>50 and jam_pengunaan == "peak":
        paket = "Paket C"
    else:
        paket = "Tidak ada paket yang cocok"

elif pengunaan_data == "bisnis":
    if data>50 and jam_pengunaan == "peak":
        paket = "Paket C"
    elif data>50 and jam_pengunaan == "off-peak":
        paket = "Paket D"
    else:
        paket = "Tidak ada paket yang cocok"
else:
     paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket}")

