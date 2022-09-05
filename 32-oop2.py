"""
inheritance adalah pewarisan dari class induk ke keturunannya
"""

class Mahasiswa: # class induk

    status = "mahasiswa"

    def __init__(self, nama, kelas):
        self.nama=nama
        self.kelas=kelas

    def keterangan(self):
        print("{} dikelas {} adalah seorang {}".format(self.nama,self.kelas,self.status))

class Nilai(Mahasiswa): # class keturunan yang mewarisi
    
    def __init__(self, nama, kelas):
        super().__init__(nama, kelas)
        self.nilai_update = []
    def input_nilai(self, tambah):
        return self.nilai_update.append(tambah)

budi = Nilai("budi", 14)
budi.keterangan()
budi.input_nilai(90)
print(budi.nilai_update)