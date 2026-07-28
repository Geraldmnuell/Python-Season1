"""latihan logika atau boolean"""

# membuat gabungan area rentang dari angka
# misalnya kurang dari 3 dan lebih dari 10

# ++++++++++3----------10+++++++++
InputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10 :"))

# memeriksa angka kurang dari 3
isKurangDari = (InputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (InputUser > 10)
print("Lebih dari 10 =", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan adalah :", isCorrect)

#--------3+++++++++10---------
# Kasus irisan
print("\n", 10*"=", "\n")
InputUser2 = float(input("Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 :"))

# ------3+++++++++++++
# lebih dari 3
isLebihDari = InputUser2 > 3
print("Lebih dari 3 =", isLebihDari)

# ++++++++10---------
# kurang dari 10
isKurangDari = InputUser2 < 10
print("Kurang dari 10 =", isKurangDari)

#------3++++++10-------fffff
IsCorrect2 = isLebihDari and isKurangDari
print("Angka yang adalah masukkan adalah =", IsCorrect2)