"""
For Loop
""" # Perulangan

# Ini dengan list
Angka1 = [1, 2, 3, 4, 5]
print(Angka1)

for i in range(5): # sama dengan penyebutan variabel
    print(f"i sekarang --> {i}")

print("Akhir Dari Program\n")

Angka2 = [0, 2, 4, 6, 8, 10]
print(Angka2)

for i in Angka2:
    print(f"i sekarang --> {i}")

print("Akhir Dari Program\n")

# ini dengan range
angka_range = range(5) # bisa juga menggunakan range(angka,angka)

for i in angka_range:
    print(f"i sekarang --> {i}")

print("akhir program\n")

# menggunakan string
data_str = "belajar coding python"

for huruf in data_str:
    print(huruf)

print("Program Selesai\n")

"""
While Loop
"""
# while kondisi:
#   aksi ini
#   aksi itu

# akhir dari program

angka = 0
print(f"angka sekarang --> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang --> {angka}")
    print("Mantap Jiwaa")

print("Program Selesai")
