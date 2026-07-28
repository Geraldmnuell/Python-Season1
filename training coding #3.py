""" latihan satuan konversi satuan temperature"""

# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("\nsuhu adalah", celcius, "CELCIUS\n")

# reamur ( rumus : 4/5 * C )
reamur = (4/5) * celcius
print("\nsuhunya adalah", reamur, "reamur\n")

# fahrenheit ( rumus : 9/5 * celcius + 32 )
fahrenheit = ((9/5) * celcius) + 32
print("\nsuhunya adalah", fahrenheit, "fahrenheit\n")

# kelvin ( rumus : celcius + 273 )
kelvin = celcius + 273
print("\nsuhunya adalah", kelvin, "kelvin\n")