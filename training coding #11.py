"""operator dalam bentuk methods"""

## merubah case dari string
# merubah semua ke upper case

salam = "heloo broooo!"
print("Normal = " + salam)
rubah = salam.upper()
print("Upper = " + rubah)

# merubah semua ke lower case
alay = "aKu KeceE ABieeZZZZZz"
subs_ke_lower = alay.lower()
print("Lower = " + subs_ke_lower)

## pengecekan dengan menggunakan isX method
salam = "halo"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() = untuk mengecek semuanya adalah huruf
# isalnum() = huruf dan angka
# isdecimal() = angka saja
#isspace() = spasi, tab, newline \n
# istitle() = semua kata dimulai dengan huruf besar

#isalpha()
kata = "saya gerald"
alpha = kata.isalpha()
print(kata + " is alpha = " + str(alpha))

# istitle()
kata = "saya Adalah manusia"
title = kata.istitle() # hasil akan boolean
print(kata + " is title = " + str(title))

## ngecek komponen startwith() endwith() <----- keren
cek_start = "Whatsapp".startswith("Whatsapp")
print('Start = ' + str(cek_start))

cek_end = "Whattsapppoi brooo".endswith("broo")
print("End = " + str(cek_end))

print(50*"=")
## penggabungan komponen join(), split()
pisah = ['halo', 'apa', 'kabar']
print(pisah)
gabung = ','.join(pisah)
print(gabung)
gabungan = ' '.join(pisah)
print(gabungan)
gabungan = '.'.join(pisah)
print(gabungan)

gabungan = "halo.apa.kabar"
print(gabungan.split('.')) # membuat string balik berbentuk list/kebalikan dari join

## alokasi karakter rjust(), ljust(), cewnter()
print(50*"=")

kanan = "kanan".rjust(10)
print("'" + kanan + "'")
kiri = "kiri".ljust(10)
print("'" + kiri + "'")
tengah = "tengah".center(20, "=")
print("'" + tengah + "'")

# kebalikannya ----> strip()
tengah = tengah.strip("=") # menghilangkan tanda =
print("'" + tengah + "'")
kanan = kanan.strip()
print("'" + kanan + "'") 