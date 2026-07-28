saldo_awal = input("masukkan saldo awal :")
deposit = input("masukkan jumlah deposit :")

total_saldo = int(saldo_awal) + int(deposit)
hutang = 50000
print("total :", (total_saldo))

# buat kondisi jika saldo cukup untuk bayar hutang dan tidak cukup
if total_saldo >= 50000:
    print("keterangan : hutang lunas")
else:
    print("keterangan : belum cukup untuk membayar hutang")