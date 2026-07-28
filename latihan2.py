# latihan coding 

# 1. -------0+++++++++5---------8+++++++11-------

"""nomor 1"""
print("Langkah Pertama :")
InputUser1 = float(input("Masukkan angka lebih dari 0 dan kurang dari 5 : "))

# 0+++++++
print("\nLangkah Kedua :")
isLebihDari = InputUser1 > 0
print("Lebih dari 0 =", isLebihDari)

# ++++++++5
isKurangDari = InputUser1 < 5
print("Kurang dari 5 =", isKurangDari)

# 0+++++++++5
IsCorrect1 = isLebihDari and isKurangDari
print("Hasil =", IsCorrect1)

# 8++++++++++11
print("\nLangkah Ketiga :")
InputUser2 = float(input("Masukkan angka lebih dari 8 dan kurang dari 11 : "))

# 8++++++++
print("\nLangkah Keempat :")
isLebihDari2 = InputUser2 > 8
print("Lebih dari 8 =", isLebihDari)

# ++++++++11
isKurangDari2 = InputUser2 < 11
print("Kurang dari 11 =", isKurangDari)

# 8++++++++11
IsCorrect2 = isLebihDari2 and isKurangDari2
print("Hasil =", IsCorrect2)

print("\nLangkah Kelima :")
HasilAkhir = IsCorrect1 and IsCorrect2
print("Hasil akhir adalah =", HasilAkhir)