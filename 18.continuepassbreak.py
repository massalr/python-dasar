# pass berfungsi sebagai dummy yang tidak di eksekusi

# angka = 0
# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass # ini tidak di eksekusi
#     print(angka)

# continue 

# angka = 0
# print(f"angka sekarang {angka}")

# while angka < 5:
#     angka += 1
#     print(f"angka sekarang {angka}") # aksi 1

#     if angka == 3:
#         print("ok juga!")
#         continue # akan membuat loop kembali ke semula
#     print("ok!!") # aksi 2

# print("selesai!!")

# break berfungsi untuk menghentikan kondisi selanjutnya

data_int = int(input("hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"hitungan = {angka}")

    if angka == data_int:
        print("ok!!")
        break
    print("ok banget")

print("selesai")