# nested list atau list bersarang sering juga disebut multi dimensi  
# karena terdapat list didalam list

data_0 = [1,2]
data_1 = [3,4]

data_list_2D = [data_0, data_1]
print(f"list 2 dimensi = {data_list_2D}")

# kegunaannya untuk data berseri

peserta_1 = ["pulan1", 23, "laki-laki"]
peserta_2 = ["pulan2", 33, "laki-laki"]
peserta_3 = ["pulan3", 81, "wanita"]

list_peserta = [peserta_1,peserta_2,peserta_3]
print(f"list peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")