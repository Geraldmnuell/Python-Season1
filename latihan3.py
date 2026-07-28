# NOMOR 2
# +++++++0-------5++++++++8----------11++++++++

InputUser1 = float(input("Masukkan angka yang kurang dari 0 : "))
InputUser11 = float(input("Masukkan angka yang lebih dari 11 : "))

isKurangDari = InputUser1 < 0
print("Angka kurang dari 0 =", isKurangDari)
isLebihDari = InputUser11 > 11
print("Angka lebih dari 11 =", isLebihDari)

Hasil = isKurangDari or isLebihDari
print("Hasilnya adalah =", Hasil)
# menggabungkan input angka yang kurang dari 0 dan lebih dari 11 untuk menentukan hasil booleannya

InputUser2 = float(input("Masukkan angka yang lebih dari 5 : "))
InputUser22 = float(input("Masukkan angka yang kurang dari 8 : "))

isLebihDari = InputUser2 > 5
print("Angka lebih dari 5 =", isLebihDari)
isKurangDari = InputUser22 < 8
print("Angka kurang dari 8 =", isKurangDari)

Hasil = isLebihDari and isKurangDari
print("Hasilnya adalah =", Hasil)