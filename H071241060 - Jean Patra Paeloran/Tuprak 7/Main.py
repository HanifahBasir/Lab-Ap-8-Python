import Function as f
while True:
    print("\n--- Sistem Pemesanan Tiket Bioskop ---\n1. Admin\n2. Pengunjung\n3. Keluar")
    try:
        Opsi = int(input("Pilih peran (1/2/3): "))
        match Opsi:
            case 1:
                while True:
                    print("\n--- Menu Admin ---\n1. Tambah film\n2. Hapus film\n3. Daftar tiket\n4. Kembali")
                    try:
                        OpsiAdmin = int(input("Pilih opsi (1/2/3/4): "))
                        match OpsiAdmin:
                            case 1:
                                f.Tambah()
                            case 2:
                                f.Hapus()
                            case 3:
                                while True:
                                    print("\n---Daftar tiket---\n1. Lihat Daftar Tiket\n2. Lihat Detail Tiket\n3. Hapus Tiket\n4. Kembali")
                                    try:
                                        OpsiTiket = int(input("Pilih Opsi (1/2/3/4): "))
                                        match OpsiTiket:
                                            case 1:
                                                f.ListTiket()
                                            case 2:
                                                f.DetailTiket()
                                            case 3:
                                                f.HapusTiket()
                                            case 4:
                                                break
                                    except ValueError:
                                        print("Opsi tidak valid")
                                        break
                            case 4:
                                break
                            case _:
                                print("Opsi tidak valid")
                    except ValueError:
                        print("Opsi tidak valid")  
            case 2:
                while True:
                    print("\n--- Menu Pengunjung ---\n1. Lihat daftar film\n2. Beli tiket\n3. Kembali")
                    try:
                        OpsiPengunjung = int(input("Pilih opsi (1/2/3): "))
                        match OpsiPengunjung:
                            case 1:
                                f.ListFilm()
                            case 2:
                                f.Beli()
                            case 3:
                                break
                            case _:
                                print("Opsi tidak valid")
                    except ValueError:
                        print("Opsi tidak valid") # eror beli
            case 3:
                break
            case _:
                print("Opsi tidak valid")
    except ValueError:
        print("Opsi tidak valid")
