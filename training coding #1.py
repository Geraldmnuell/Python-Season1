nama = "gerald" # tipe data string
umur = 18 # tipe data integer (tidak perlu menggunakan tanda kutip)
tinggi_badan = 165.5 # tipe data float (penggunaan angka desimal)
hobi_belajar_coding = True # tipe data boolean (menyatakan kondisi benar atau salah). untuk True/False harus menggunakan kapital pada huruf awalnya. 

"""memasukkan tipe data apa saja untuk mengkonversi"""
# contoh :
# str("variabel bebas") >>> konversi dari integer ke string
# int("variabel bebas") >>> konversi dari string ke integer

print("nama :", nama)
print("umur :", umur)
print("tinggi badan :", tinggi_badan)

"""Input user""" # memasukkan function input di dalam print
print(input("gerald sedang apa?"))

# menggunakan variabel
input_nama = input("apa makanan favoritmu?")
print(input_nama)

"""operasi matematika"""
# setiap perhitungan harus menggunakan variabel terlebih dahulu
# penjumlahan (+)
# pengurangan (-)
# Perkalian (*)
# Pembagian (/) *kalau seperti // , maka output menjadi bilangan bulat (tidak memiliki pecahan atau desimal)

print("Hasilnya adalah")
a = 10
b = 20
c = a + b
print(c)

# operasi matematika versi input user
a = input("masukkan angka pertama :")
b = input("masukkan angka kedua :")
c = int(a) + int(b)
print("hasilnya adalah :", c)

# .find (mencari sesuatu dalam sebuah variabel)
nama_saya = "gerald"
print("berada dibaris", nama_saya.find("r"))

# len (mengetahui jumlah sesuatu dalam variabel)
nama_saya = "gerald"
print("jumlah huruf :", len("gerald")) # kalau semua huruf menjadi besar ketikkan print(nama_saya.upper())
# kalau cuma huruf besar dui awal kata ketikkan print(nama_saya.capitalize())

# .count (menghitung jumlah huruf dalam variabel)
nama_saya = "siti"
print("jumlah huruf i :", nama_saya.count("i"))