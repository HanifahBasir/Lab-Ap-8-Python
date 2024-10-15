def buat_acronym(kalimat):
    kata_kata = kalimat.split()
    akronim = ''.join(kata[0] for kata in kata_kata)
    return akronim

inputan = input("Masukkan sebuah kalimat: ")
output = buat_acronym(inputan)
print("Output:", output)
