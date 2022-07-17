# perulangan while kondisinya boolean

# program ini jika dijalankan akan infinite loop kerna kondisinya True
# angka = 0

# while angka < 5:
#     print("teh manis hangat")

# print("selesai")

# untuk menghindari infinite loop, kondisi perulangan harus false dengan cara harus sama dengan aksi
angka = 0

while angka < 5:
    angka += 1
    print("teh manis hangat")
print("selesai")