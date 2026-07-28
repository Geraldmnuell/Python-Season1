"""operasi adan manipulasi string"""

# 1. menyambung string (concatenate)
nama_pertama = 'Gerald'
nama_tengah = 'Imanuel'
nama_akhir = 'Manongga'

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang_nama = len(nama_lengkap)
print("Jumlah string dari " + nama_lengkap + " adalah " + str(panjang_nama))

# operator untuk string
# mengecek apakah ada komponen char atau string di string
cek_komponen = 'G'
status = cek_komponen in nama_lengkap
print(cek_komponen + " ada di " + nama_lengkap + ' = ' + str(status))

# mengulang string
print(10*"wk")
ketawa = "wk"
print(10*ketawa)

# indexing
print("index ke-0 dari " + nama_lengkap + " adalah " + nama_lengkap[0])
print("index ke-10 dari " + nama_lengkap + " adalah " + nama_lengkap[10])
print("index ke-17 dari " + nama_lengkap + " adalah " + nama_lengkap[17])
print("index ke-(-3) dari " + nama_lengkap + " adalah " + nama_lengkap[-3]) # mengambil dari belakang mulai dari index -1
# mwngambil beberapa string (range)
print("index ke-[0:3] dari " + nama_lengkap + " adalah " + nama_lengkap[0:3]) # pakai :
# tapi aneh jadinya tidak sesuai aturan index, jadinya kita tambah satu saja (semisalnya mau cari ambil yang sesuai)
print("index ke-[0:3] dari " + nama_lengkap + " adalah " + nama_lengkap[0:4])
print("index ke-[10:13] dari " + nama_lengkap + " adalah " + nama_lengkap[10:14])
# kalau mau ambil secara tidak berurutan
print("index ke-[0,2,4,6,8,10] dari " + nama_lengkap + " adalah " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 32
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
nama = "moroko pororo sutono"
jumlah = nama.count("o")
print("Jumlah huruf o di " + nama + " adalah " + str(jumlah))

print("\nTerima Kasih")