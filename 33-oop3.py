"""
polymorphism adalah kemampuan untuk mengambil bentuk yang berbeda. Polymorphism
dalam python memungkinkan kita untuk mendefinisikan metode pada child class dengan menggunakan nama
yang sama seperti pada parent class.
"""

class Kucing:

    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + " meong-meong"

class Anjing:

    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + " guk-guk"

riri = Kucing("riri")
print(riri.respon())
bono = Anjing("bono")
print(bono.respon())

for binatang in [riri,bono]:
    print(binatang.respon())