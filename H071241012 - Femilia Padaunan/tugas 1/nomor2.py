# Input dari pengguna
karakter = input("Masukan karakter: ")
kalimat = input("Masukan kalimat: ")

# Menggunakan operator logika dan aritmatika untuk memilih pesan yang tepat
pesan = (f'{karakter} ditemukan di dalam "{kalimat}"', 
         f'{karakter} tidak ditemukan di dalam "{kalimat}"')[karakter not in kalimat]

# Tampilkan pesan
print(pesan)