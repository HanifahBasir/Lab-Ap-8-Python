######## Soal 2
######## TIKET

umur = int(input("Masukkan umur : "))
anggota = input('Ketik "ya" jika anda anggota : ')

if 0 < umur < 5:
    harga = 0
elif 5<=umur<=12 :
    harga = 50000
elif 13<=umur<=59:
    harga = 100000
elif umur >= 60 :
    harga = 70000
else:
    harga = -1


total = harga * 0.8 if anggota == "ya" else harga

if harga == 0:
    print("Harga tiket gratis")
elif harga == -1:
    print("Anda belum lahir")
else:
    print(f"harga tiket = Rp {total:,.0f}")