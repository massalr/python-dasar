# operasi dan manipulasi string

# menyambung string (concatenate)
nama_pertama = "computer"
nama_tengah = "D"
nama_akhir = "error"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + "=" + str(panjang))

# operator untuk string
# mengecek apakah ada komponen char di string
r = "r"
status = r in nama_lengkap
print(r + " ada di " + nama_lengkap + "=" + str(status))

# mengulang string
print("ty"*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-(-3) : " + nama_lengkap[-3])
print("index ke-[3:6] : " + nama_lengkap[3:7])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

assci_code = ord(" ")
print("ASCII code untuk spasi : " + str(assci_code))
data = 119
print("char untuk ASCII code 119 : " + chr(data))

# operator dalam bentuk method
nama = "computer error"
nama = nama.count(r)
print(nama)
nama = "computer error"
nama = nama.upper()
print(nama)

# pengecekan isX method

salam = "hallo"
apakah_lower = salam.islower()
print(salam + " apakah lower : " + str(apakah_lower))

# isalpha() : untuk mengecek semua huruf
# isalnum() : huruf dan angka
# isdecimal() : angka saja
# isspace() : spasi, tab, newline
# istitle() : semua kata dimulai dengan huruf besar