"""IF ELSE ELIF"""
# == sama dengan
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan
# <= kurang dari sama dengan

usia = 24
if usia == 25: # contoh untuk ==
    print("belum boleh buat ktp")
else:
    print("sudah boleh")

usia = 25
if usia > 25: # contoh untuk >
    print("sudah menikah")
else:
    print("belum menikah")

"""untuk beberapa kondisi lebih dari satu"""
# memvalidasi sesuatu pernyataan

usia = 18 # sesuai umur saja:)
if usia == 0:
    print("belum lahir")
elif usia >= 1 and usia <= 5:
    print("beranjak balita")
elif usia >= 6 and usia <= 11:
    print("beranjak anak-anak")
elif usia >= 12 and usia <= 16:
    print("beranjak remaja")
elif usia >= 17 and usia <= 25:
    print("beranjak pemuda")
else:
    print("mungkin sudah orang tua")

# list/array
keluarga = ["ayah", "ibu", "adik", "kakak"]
print("list ke tiga terdapat", keluarga[3])
print("keseluruhan listnya adalah", len(keluarga))

for anggota_keluarga in keluarga:
    print(anggota_keluarga)

# while
angka_awal = 1
while angka_awal <= 10:
    print(angka_awal)
    angka_awal += 1 # sama halnya dengan angka awal = angka_awal + 1