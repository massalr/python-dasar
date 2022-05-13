import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

nama = input("masukan nama anda : ")
tanggal = int(input("tanggal lahir \t:"))
bulan = int(input("bulan lahir \t:"))
tahun = int(input("tahun lahir \t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {tanggal_lahir}")
print(f"harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal {hari_ini}")
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
print(f"umur anda saat ini : {umur} atau {umur_tahun} tahun")
