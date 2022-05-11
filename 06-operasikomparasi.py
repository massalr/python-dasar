# operasi komparasi untuk membandingkan nilai
# setiap hasil dari operasi komparasi adalah boolean
# >,<.>=,<=,==,!=,is,is not

a = 4
b = 2

print("======lebih besar dari >")
hasil = a > 3
print(f"{a} > 3 = {hasil}")
hasil = b > 3
print(f"{b} > 3 = {hasil}")
hasil = b > 2
print(f"{b} > 2 = {hasil}")

print("======kurang dari <")
hasil = a < 3
print(f"{a} < 3 = {hasil}")
hasil = b < 3
print(f"{b} < 3 = {hasil}")
hasil = b < 2
print(f"{b} < 2 = {hasil}")

print("======lebih dari sama dengan >=")
hasil = a >= 3
print(f"{a} >= 3 = {hasil}")
hasil = b >= 3
print(f"{b} >= 3 = {hasil}")
hasil = b >= 2
print(f"{b} >= 2 = {hasil}")

print("======kurang dari sama dengan <=")
hasil = a <= 3
print(f"{a} <= 3 = {hasil}")
hasil = b <= 3
print(f"{b} <= 3 = {hasil}")
hasil = b <= 2
print(f"{b} <= 2 = {hasil}")

print("======sama dengan ==")
hasil = a == 4
print(f"{a} == 4 = {hasil}")
hasil = b == 4
print(f"{b} == 4 = {hasil}")

print("======tidak sama dengan")
hasil = a != 4
print(f"{a} != 4 = {hasil}")
hasil = b != 4
print(f"{b} != 4 = {hasil}")

# 'is' sebagai komparasi object atau data yg ada di memori
print("====== object identity is")
x = 5
y = 5
print(f"nilai {x} = x", 'id = x', hex(id(x)))
print(f"nilai {y} = x", 'id = x', hex(id(y)))
hasil = x is y
print(f"{x} is {y} = {hasil}")

print("====== object identity is not")
x = 5
y = 5
print(f"nilai {x} = x", 'id = x', hex(id(x)))
print(f"nilai {y} = x", 'id = x', hex(id(y)))
hasil = x is not y
print(f"{x} is not {y} = {hasil}")