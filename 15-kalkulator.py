# kalkulator

print(30*"_")
angka1 = float(input("masukan angka pertama : "))
operator = input("operator (+,-,x,/) : ")
angka2 = float(input("masukan angka kedua : "))

# percabangannya

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil : {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil : {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2
    print(f"hasil : {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasil : {hasil}")
else:
    print("yang anda masukan salah")

print("end")