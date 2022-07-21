# operasi

# indek (0/-3) (1/-2)  (2/-1)
data = ["kopi", "teh", "susu"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) {data_terakhir}")

# mengambil info data jumlah
panjang_data = len(data)
print(f"panjangnya data adalah {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum di tambah = {data}")

data.insert(2, "kopi pahit")
print(f"data sesudah di tambah = {data}")

# menambah di akhir list
data.append("juice")
print(f"data di tambah lagi di akhir = {data}")

# menambah list dengan list
data_baru = ["teh tarik", "teh es"]
data.extend(data_baru)
print(f"data gabungan = {data}")

# menghapus data
data.remove("kopi")
print(f"data remove = {data}")

# meremove data paling akhir
data_akhir = data.pop()
print(f"remove data akhir = {data}")