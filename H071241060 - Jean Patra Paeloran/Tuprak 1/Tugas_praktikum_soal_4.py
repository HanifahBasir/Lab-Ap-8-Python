celcius = float(input("masukan suhu dalam celcius: "))
kelvin = str(celcius+273)
Reamur = 4/5*celcius
Fahrenheit = 9/5*celcius+32
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {kelvin}K")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Reamur adalah : {round(Reamur,2)}R")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Fahrenheit adalah : {round(Fahrenheit,2)}F")