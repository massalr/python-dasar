"""
mendefinisikan class harus menggunakan format CamelCase
"""

class Kulkas:

    penjual = "massal" # ini adalah class atribute

    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga

    def keterangan(self):
        print("{} harganya adalah {} dan penjualnya bernama {}".format(self.merek,self.harga,self.penjual))

barang = Kulkas("yamaha", 1000)
print(barang.harga)
print(barang.merek)
print(barang.keterangan())