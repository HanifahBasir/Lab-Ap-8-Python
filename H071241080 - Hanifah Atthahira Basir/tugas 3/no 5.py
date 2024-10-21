"""Program untuk memprediksi populasi serangga"""

serangga_A = int(input("Masukkan populasi awal serangga A: "))  
serangga_B = int(input("Masukkan populasi awal serangga B: "))  
jumlah_hari = int(input("Masukkan jumlah hari: "))  

for hari in range(1, jumlah_hari + 1):
       
    if hari % 2 != 0: #ganjil
        serangga_A = serangga_A * 1.3  # serangga A bertambah 30% 
        serangga_B = serangga_B * 1.5  # serangga B bertambah 50% 
       
    else: #genap
        serangga_A = serangga_A * 0.8  # serangga A berkurang 20% 
        serangga_B = serangga_B * 0.6  # serangga B berkurang 40% 
        
    if hari % 5 == 0: #predator datang
        print(f"hari {hari}: Predator memakan 10% populasi")
        serangga_A = serangga_A * 0.9  # serangga A berkurang 10% 
        serangga_B = serangga_B * 0.9  # serangga B berkurang 10% 
        
    print(f"hari {hari}: serangga A = {int(serangga_A)}, serangga B = {int(serangga_B)}")







