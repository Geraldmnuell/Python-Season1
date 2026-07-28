"""operasi aritmatika"""
# operasi perhitungan jika tidak menggunakan input user (berlaku semua operasi)
# tambahan : floor division sebutan untuk simbol //

a = 10 # pertambahan
b = 20
hasil = a + b
print(a,'+', b, '=', hasil)

a = 20 # pembagian 
b = 10
hasil = a / b
print(a,'/', b, '=', hasil)

a = 2 # eksponen (pangkat)
b = 2
hasil = a ** b
print(a,'**', b, '=', hasil)

a = 20 # modulus (sisa pembagian)
b = 7
hasil = a % b
print(a,'%', b, '=', hasil)

"""prioritas operasi"""
"""
    1. ()
    2. eksponen **
    3. perkalian dkk * / % //
    4 pertambahan dan pengurangan + -
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(hasil)

# conoth sederhana
hasil = x + y * z
print(hasil)

hasil = (x + y) * z
print(hasil)