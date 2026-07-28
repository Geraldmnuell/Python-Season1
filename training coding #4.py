"""operasi komparansi"""
# setiap hasil dari operasi komparansi adalah boolean
# simbol : >,<,>=,<=,==,!=,is, is not

# lebih besar dari >
a = 4
b = 2
print("\nlebih dari :")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = a > 5
print(a, '>', 5, '=', hasil)
hasil = b > 5
print(b, '>', 5, '=', hasil)

# kurang dari
a = 4
b = 2
print("\nkurang dari :")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < a
print(b, '<', a, '=', hasil)
hasil = a < b
print(a, '<', b, '=', hasil)
# HAL INI BERLAKU SAMA DENGAN SIMBL >=, <=, == DSB

# tidak sama dengan !=
a = 1
b = 2
print("\ntidak sama dengan :")
hasil = a != b
print(a, '!=', b, '=', hasil)
hasil = a != a
print(a, '!=', a, '=', hasil)

# is (membandingkan memori atau objek) >> sebagai komparansi object indentity
x = 4 # ini adalah assignment membuat objek
y = 4
print("\nobjek identity(is)")
print("nilai x = ", x, "id = ", hex(id(x)))
print("nilai y = ", y, 'id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 6
y = 7
print("nilai x =", x, 'id =', hex(id(x)))
print("nilai y =", y, 'id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil) # ini juga berlaku pada is not karena hanya dibedakan sama pembanding