# date and time (latihan)

import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}")

tanggal_lahir = dt.date(2007,5,28)
print(tanggal_lahir)
print(f"Hari ini adalah hari = {tanggal_lahir:%A}")

import datetime as dt
print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal kemerdekaan indonesia : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Jatuh pada hari : {tanggal_lahir:%A}")
print(f"Umur anda adalah = {umur_tahun} Tahun , {umur_bulan_sisa} Bulan")