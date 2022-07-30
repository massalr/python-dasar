# dictionary adalah assosiative array mengaksesnya menggunakan
# identifier atau key

data_dict = {
    'key1':'value1',
    'key2':'value2'
}

print(data_dict)
# bisa di akses key nya
print(data_dict['key2'])

print("="*10,"Operator Dictionary","="*10)

data_dicty = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
}

# panjang dictionary
lendicty = len(data_dicty)
print(f"panjang dictionary {lendicty}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dicty
print(f"apakah {KEY} ada di data_dicty: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dicty["cup"])
print(data_dicty.get("cup"))
print(data_dicty.get("kis","key tidak ditemukan")) # cek key dengan message

# mengupdate data 
data_dicty.update({"camel putih":"rokok akan membunuhmu"})
print(data_dicty)

# delete data
del data_dicty["camel putih"]
print(data_dicty)

print("="*10,"Looping Dictionary","="*10)

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep surucup",
}

for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables

keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"key={key}, value={value}")

print("="*10,"Copy Dictionary","="*10)

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep surucup",
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup si cucup"
print(f"teman-teman: {teman_teman}\n")
print(f"friends : {friends}\n")

print("="*10,"Multi Keys & Nesting Dictionary","="*10)

import datetime

mahasiswa1 = {
    'nama':'ucup surucup',
    'nim':'19022003',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,2,23)
}

mahasiswa2 = {
    'nama':'dudung surudung',
    'nim':'19022004',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2001,3,30)
}

mahasiswa1 = {
    'nama':'asep surecep',
    'nim':'19022005',
    'sks_lulus':120,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,8,22)
}

data_mahasiswa = {
    'MAH001':'mahasiswa1',
    'MAH002':'mahasiswa2',
    'MAH003':'mahasiswa3'
}

print(f"{'KEY':<6} {'nama':<17} {'SKS':<3} {'beasiswa':<9} {'lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")