# contoh generic
# string
nama = "computer"
format_str = f"hai {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2002.2
format_str = f"angka = {angka}"
print(format_str)

# bilangan jutaan
angka = 2000000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan decimal
angka = 2222.33422
format_str = f"decimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2222.33422
format_str = f"decimal = {angka:09.3f}"
print(format_str)

# persen
persen = 0.012
format_persen = f"persen = {persen:.2%}"
print(format_persen)