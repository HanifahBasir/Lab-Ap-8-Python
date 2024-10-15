"""Program untuk menyingkat suatu string menjadi akronim"""

def akronim(kalimat):
    kata_kata = kalimat.split() #memecah kalimat menjadi beberapa kata
    
    #mengambil setiap huruf di indeks 0  dan menjadikannya huruf kapital
    akronim = ''.join([kata[0].upper() for kata in kata_kata]) 
    
    # Mencetak akronim yang sudah terbentuk
    print(akronim)

akronim("Dewan Perwakilan Rakyat")  
