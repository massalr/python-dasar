# list adalah tipe data koleksi atau kumpulan data yang bersifat
# ordered atau terurut dan changeable atau bisa dirubah

angka = [1,2,3,4,5]
print(angka)

data_str = ["kopi", "teh", "gula"]
print(data_str)

# kumpulan didalam list dapat di campur
data_campuran = [1, "kopi", 4, "teh manis"]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,20)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop
list_for = [i**2 for i in range(0,10)]
print(list_for)

# membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i != 8]
print(list_for_if)