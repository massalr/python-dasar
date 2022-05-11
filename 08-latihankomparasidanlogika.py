# latihan komparasi dan logika

# membuat gabungan area rentang dari sebuah angka

# ++++++++3--------10++++++++

inputUser = int(input("masukan angka lebih kurang dari 3 atau lebih besar dari 10 : "))
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print(f"kurang dari 3 adalah {inputUser} = {isKurangDari}")
isLebihDari = (inputUser > 10)
print(f"lebih dari 10 adalah {inputUser} = {isLebihDari}")

isCorrect = isKurangDari or isLebihDari
print(f"angka yang dimasukan : {isCorrect}")