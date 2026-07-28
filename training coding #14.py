# if newline
nama = input("Masukkan nama anda : ")
if nama == "gerald" : print("Nama yang di masukkan benar") # kondisi if
print("Terima kasih:)")

nama = input("Siapa namanya : ")

# program if else indentation
if nama == "gerald":
    print("Hallo gerald")
else:
    print("Nama anda salah")
print(f"terima kasih yaa:) {nama}")

# elif statement
print("\n", 5*"=", "Mencari Nama", 5*"=")

nama = input("Masukkan Nama : ")
if nama == "gerald":
    print("nama gerald ditemukan")
elif nama == "alok":
    print("nama alok ditemukan")
elif nama == "anis":
    print("nama anis ditemukan")
elif nama == "bahlil":
    print("nama bahlil ditemukan")
else:
    print("nama tidak ditemukan")
print("Program selesai")