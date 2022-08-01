'''latihan fungsi'''
import os

# program menghitung luasdan keliling persegi panjang

# membuat header program
def header():
    '''header'''
    os.system("clear")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''mengambil input user'''
    lebar = int(input("masukan nilai lebar : "))
    panjang = int(input("masukan nilai panjang : "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar + panjang)

def display(message, value):
    '''fungsi diplay'''
    print(f"hasil perhitungan {message} = {value}")

    
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)
    isContinue = input("apakah lanjut? y/n ")
    if isContinue == "n":
        break

print("program selesai")