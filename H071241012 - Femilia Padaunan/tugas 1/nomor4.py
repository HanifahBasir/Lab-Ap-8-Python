def konversi_suhu(celsius):
    # Konversi ke Kelvin
    kelvin = celsius + 273.15
    # Konversi ke Reamur
    reamur = celsius * 4 / 5
    # Konversi ke Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    
    print(f"Hasil konversi dari suhu {celsius} derajat Celcius ke Kelvin adalah: {kelvin:.2f}K")
    print(f"Hasil konversi dari suhu {celsius} derajat Celcius ke Reamur adalah: {reamur:.2f}R")
    print(f"Hasil konversi dari suhu {celsius} derajat Celcius ke Fahrenheit adalah: {fahrenheit:.2f}F")

# Input suhu dalam Celcius
celsius = float(input("Masukkan suhu dalam Celcius: "))
konversi_suhu(celsius)