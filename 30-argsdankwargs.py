'''*args adalah istilah untuk menyebut jumlah argumen yang tidak
bisa di tentukan atau berubah-ubah'''

print("-"*10, "fungsi biasa")

def sapa_teman(nama1,nama2,nama3):
    print(f"hallo {nama1}")
    print(f"hallo {nama2}")
    print(f"hallo {nama3}")

sapa_teman("boy", "girl", "men")

print("-"*10, "menggunakan *args")

def sapa_teman(*nama):
    for i in nama:
        print("hallo", i)

sapa_teman("budi", "joko", "sari", "yudi")

def jumlah(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

print( jumlah(5,7))
print( jumlah(9,90))
print( jumlah(500,79898))
# perulangan for di dalam fungsi untuk mengakses setiap element di tuple

print("-"*10, "**kwargs")

def fungsi (**kwargs):
    '''fungsi biasa aja'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} yang tingginya {tinggi} dan berat {berat}")

fungsi(nama="surrender", tinggi=180, berat=80)

'''
perbedaan antara args dan kwargs ada di penulisan named argument atau named parameter,
jika dalam args argumen fungsi di tulis langsung dengan nilai saja, maka dalam
kwargs argumen fungsi tersebut di tulis dalam bentuk pasangan nama dan value, parameter
kwargs akan berbentuk type dictionary
'''