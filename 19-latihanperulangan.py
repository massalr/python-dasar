# latihan perulangan membuat segitiga


sisi = 10

# menggunakan for
count = 1 # dummy variable
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir for")

# menggunakan while
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir dari while")

# hanya angka ganjil
count = 1
while True:
    if count%2:
        # akan print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir dari keganjilan")

# segitiga sama kaki
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir dari segitiga sama kaki")

