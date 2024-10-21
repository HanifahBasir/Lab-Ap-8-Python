daftar = []


def tampil():
    if daftar == []:
        print("KOSONG BOSKU, ISI BARANG DULULAH")
    else:
        print("\n")
        print("="*67)
        # print("|","DAFTAR BARANG".center(36),"|")
        print(f"|{"KODE".center(6)}|{"DAFTAR BARANG".center(36)}|{"JUMLAH".center(8)}|{"HARGA".center(12)}|")
        print("="*67)
        for i in sorted(daftar):
            print(i)
        print("="*67)
        print("\n")



def tambah():
    print("\n")
    # untuk kode
    while True:
        ada = False
        while True:
            try:
                kode = input("masukkan kode (tiga digit) : ")
                if kode != ValueError and len(str(kode)) == 3:
                    break
            except:
                print("MASUKKAN KODE BILANGAN BULAT 3 BIJI!!!")
        kode = str(kode)
        for index, item in enumerate(daftar):
            item_split = item.split("|")
            if item_split[1].strip() == f"{kode.strip()}":
                print("kode sudah ada, coba yang lain")
                ada = True
        if not ada:
            break
    # untuk barang
    while True:
        ada = False
        barang = input("masukkan barang yang ingin anda tambahkan : ")
        for index, item in enumerate(daftar): 
            item_split = item.split("|")  
            if item_split[2].strip() == f"{barang.strip()}":
                print("barang sudah ada!!")
                ada = True
        if not ada:
            break
    # untuk jumlah
    while True:
        try:
            jumlah = int(input("masukkan jumlah : "))
            if jumlah != ValueError:
                jumlah = str(jumlah)
                break
        except:
            print("MASUKKAN INPUT INTEGER!!!")
    # untuk harga
    while True:
        try:
            harga = int(input("masukkan harga : "))
            if harga != ValueError:
                harga = str(harga)
                break
        except:
            print("MASUKKAN INPUT INTEGER!!!")
    daftar.append(f"|{kode[:3].center(6)}|{barang[:34].center(36)}|{jumlah[:6].center(8)}|{harga[:10].center(12)}|")
    print("\n")
    print("Gudang anda sekarang:")
    tampil()


def update():
    print("\n")
    tampil()
    kode = input("kode apa yang ingin anda ganti : ")
    update = False
    for index, item in enumerate(daftar):
        if item.startswith(f"|{kode[:3].center(6)}"):
            barang = input("masukkan barang : ")
            jumlah = input("masukkan jumlah : ")
            harga = input("masukkan harga : ")
            daftar[index] = f"|{kode[:3].center(6)}|{barang[:34].center(36)}|{jumlah[:6].center(8)}|{harga[:10].center(12)}|"
            print("barang setelah update: ")
            tampil()
            update = True
            break
    if not update:
        print(f"barang dengan kode : {kode} tidak ditemukan")

def delete():
    print("\n")
    tampil()
    kode = input("kode apa yang ingin anda hapus : ")
    delete = False
    for index, item in enumerate(daftar):
        if item.startswith(f"|{kode[:3].center(6)}"):
            del daftar[index]
            print("barang setelah delete: ")
            tampil()
            delete = True
            break
    if not delete:
        print(f"barang dengan kode : {kode} tidak ditemukan")
        

def cari():
    print("\n")
    print("""cari berdasarkan:
        1. kode
        2. nama
        """)
    
    while True:
        opsi = input("masukkan opsi : ")
        if opsi == "1" or opsi == "2":
            break
        else:
            print("masukkan opsi benar")
    
    ada = False
    # while not ada:
        
    #     if opsi == "1":
    #         for index, item in enumerate(daftar):
    #             kode = input("masukkan kode : ")
    #             item_break = item.split("|")
    #             if item_break[1] == f"{kode[:3].center(6)}":
    #                 print(f'''
    #                     barang ke-{index+1}
    #                     kode   = {item_break[1].strip()}
    #                     barang = {item_break[2].strip()}
    #                     jumlah = {item_break[3].strip()}
    #                     ''')
    #                 ada = True
    #             else:
    #                 print(f"kode tidak ditemukan!! coba lagi")
                    
    #     elif opsi == "2":
    #         for index, item in enumerate(daftar):
    #             barang = input("masukkan barang : ")
    #             item_break = item.split("|")
    #             if item_break[2] == f"{barang[:34].center(36)}":
    #                 print(f'''
    #                     barang ke-{index+1}
    #                     kode   = {item_break[1].strip()}
    #                     barang = {item_break[2].strip()}
    #                     jumlah = {item_break[3].strip()}
    #                     ''')
    #                 ada = True
    #             else:
    #                 print(f"barang tidak ditemukan!! coba lagi")
    
    if opsi == "1":
        kode = input("masukkan kode : ")
        for index, item in enumerate(daftar):
            item_break = item.split("|")
            if item_break[1].strip() == kode.strip():
                print(f'''
                    barang ke-{index+1}
                    kode   = {item_break[1].strip()}
                    barang = {item_break[2].strip()}
                    jumlah = {item_break[3].strip()}
                    ''')
                ada = True
                break
        if not ada:
            print("kode tidak ditemukan!! coba lagi")
                    
    elif opsi == "2":
        barang = input("masukkan barang : ")
        for index, item in enumerate(daftar):
            item_break = item.split("|")
            if item_break[2].strip() == barang.strip():
                print(f'''
                    barang ke-{index+1}
                    kode   = {item_break[1].strip()}
                    barang = {item_break[2].strip()}
                    jumlah = {item_break[3].strip()}
                    ''')
                ada = True
                break
        if not ada:
            print("barang tidak ditemukan!! coba lagi")
