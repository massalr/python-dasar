# looping list

print("for loop")

kumpulan_angka = [3,5,2,5,6,7,9]

for angka in kumpulan_angka:
    print(f"angka : {angka}")

print("\nfor loop dengan range")

kumpulan_angka = [3,5,2,5,6,7,9]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

print("\nwhile loop")

kumpulan_angka = [3,5,2,5,6,7,9]

panjang = len(kumpulan_angka)
i=0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

print("\nlist comprehension")

data = ["pulan", 2,3,2]
[print(f"data={i}") for i in data]

# enumerate
print("\nEnumerate")
data_list = ["pulan",1,2,3]

for index,data in enumerate(data_list):
    print(f"index={index},data={data}")