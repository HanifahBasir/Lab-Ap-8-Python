def cek_akronim(input_string):
    kata = input_string.split(' ')
    akronim = ''.join(i[0].upper() for i in kata)
    return akronim

# print(cek_akronim())
print(cek_akronim(input(": ")))

# akronim = ''.join(i[0] for i in kata if i[0] == i[0].upper()) #untuk validasi klo user menambahkan kata hubung
# print(cekakronim("Negara Kesatuan dan Republik Indonesia")) # contoh pake kata hubung

