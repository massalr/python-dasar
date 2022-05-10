data = input("masukan data: ")
print("data adalah :", data," type data :", type(data))

# mengambil data tipe integer
angka = int(input("masukan angka: "))
print("angka adalah:", angka, "type data:", type(angka))


# untuk data boolean di casting dulu ke int lalu ke bool
biner = bool(int(input("masukan nilai bool :")))

print("data = ", biner, "type ", type(biner))