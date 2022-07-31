'''
fungsi pada python adalah kumpulan kode yang di kelompokan menjadi 
satu kesatuan yang bisa di gunakan berkali-kali
'''

def selamat_sore():
    print("selamat sore!!")
    print("ini adalah fungsi")

selamat_sore()

# fungsi dengan parameter
'''sebuah fungsi juga bisa menerima parameter atau pun argumen
merupakan suatu nilai atau variable yang di lempar kedalam fungsi
untuk di proses lebih lanjut'''

def selamat_datang(nama):
    print(f"halo {nama}, jelek")

selamat_datang('adjat')

def tambah(angka_1,angka_2):
    '''ini adalah fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,9)
tambah(90, 90)

def say_hi(list_peserta):
    '''fungsi peserta'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota_pramuka = ["ucup","otong","dudung"]

say_hi(anggota_pramuka)

'''fungsi dengan return atau kembalian'''

# def nama_fungsi(argumen):
#       badang fungsi
#       return output

# fungsi kuadrat

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

print(kuadrat(9))

z = 19 + kuadrat(3)
print(z)