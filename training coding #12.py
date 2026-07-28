"""format string"""

# contoh generic
# string
nama = "gerald"
format_str = f"hello {nama}" # pake tanda kurung {}
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 200.7
format_str = f"angka = {angka}"
print(format_str)

# bilangan_bulat 
angka = 15
format_str = f"angka = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"hasil = {angka:,}" # tambahkan :, (berlaku juga dengan jumlah yang jutaan,miliar)
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # menambahkan :.-angka-f , misal berapa angka di belakang koma yang diinginkan
print(format_str)                      # maka tinggal di ganti saja angka di antara titik dan f

# menampilkan leading zero
angka = 2005.54321
format_str = f"angka   = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_negatif = -10
angka_positif = 10
format_negatif = f"negatif = {angka_negatif}"
format_positif = f"positif = {angka_positif:+d}"
print(format_negatif)
print(format_positif)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.0%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5

format_str = f"harga total = Rp {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal) 
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = oct = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)