from animals import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
         super().__init__(nama, makanan, hidup, berkembang_biak)
         self.warna_ular = warna_ular
         self.jenis_ular = jenis_ular 

    def cetak_ular(self):
         super().cetak()
         print(f'warna ular ini adalah warna{self.warna_ular} dan hewan ini jenisnya ular{self.jenis_ular}')

print('----- cetak ular -----')
print('----- object pertama -----')
kobra = ular('ular kobra', 'daging', 'darat', 'bertelur', 'hitam', 'berbisa')
kobra.cetak_ular()

#object kedua
print('----- object kedua -----')
piton = ular('ular piton', 'hewan-hewan besar','darat', 'bertelur', 'kuning', 'familia Pythonidae')
piton.cetak_ular()