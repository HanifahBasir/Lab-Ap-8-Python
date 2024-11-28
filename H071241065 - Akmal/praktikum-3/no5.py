populasi_awalA = int(input("masukkan pupulasi awal serangga A : "))
populasi_awalB = int(input("masukkan pupulasi awal serangga B : "))
jumlah_hari = int(input("masukkan jumlah hari : "))

if jumlah_hari <= 0 :
    print("masukkan hari yang benar")
else:
    for i in range(1, jumlah_hari + 1):
        if i % 2 == 0:
            populasi_awalA = int(populasi_awalA * 0.8)
            populasi_awalB = int(populasi_awalB * 0.6)
            print(f"hari {i}: serangga A = {populasi_awalA}, serangga B = {populasi_awalB}")
            
        else :
            populasi_awalA = int(populasi_awalA * 1.3)
            populasi_awalB = int(populasi_awalB * 1.5)
            print(f"hari {i}: serangga A = {populasi_awalA}, serangga B = {populasi_awalB}")

        if i % 5 == 0:
            populasi_awalA = int(populasi_awalA * 0.9)
            populasi_awalB = int(populasi_awalB * 0.9)
            print(f"hari {i}: predator memakan 10% populasi")
            print(f"hari {i}: serangga A = {populasi_awalA}, serangga B = {populasi_awalB}")


            