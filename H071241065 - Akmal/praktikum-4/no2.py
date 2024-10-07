def harta():
    total_langkah = 0
    bahaya = "tidak"
    while True: 
        langkah = input("masukkan langkah (meter) atau 0 untuk selesai: ")
        try :     
            langkah = int(langkah)
            if langkah == 0:
                break
            elif langkah < 0:
                print("masukkan angka yang lebih dari 0")
                continue
            total_langkah = total_langkah + langkah
            if langkah > 20:
                bahaya = "ya"
        except ValueError:
            print("input tidak valid. masukkan bilangan bulat")

            
    total_jarak = total_langkah 
    print(f"total jarak: {total_jarak}") 
    print(f"ada bahaya: {bahaya}")     
            
    if bahaya == "ya":
        print("keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50 and bahaya == "tidak":
        print("keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif bahaya  == "tidak" and  (total_jarak > 50 or total_jarak < 50):
        print("keputusan: tidak menemukan harta karun. coba lagi")


harta()




