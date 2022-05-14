# control flow atau pengatur alur program
# 1. if, 2. kondisi, 3. kondisinya
# elif
# else kondisi False

nama = input("tuliskan nama anda :")

if nama=="computer": # nama suatu kondisi
    print("oke, anda mendapatkan akses") # aksi True
elif nama=="error": # kondisi 2
    print("silahkan masuk") # aksi True
else:
    print(f"anda tidak mendapatkan akses {nama}") # aksi False
print(f"bye {nama}") # akhir dari program