from animals import *

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
         super().__init__(nama, makanan, hidup, berkembang_biak)
         self.jenis_bulu = jenis_bulu
         self.bunyi = bunyi

    def cetak_burung(self):
         super().cetak()
         print(f'hewan ini berbulu{self.jenis_bulu} dan hewan ini berbunyi{self.bunyi}')

print('----- cetak burung -----')
print('----- object pertama -----')
beo = burung('burung beo', 'biji-bijian','udara', 'bertelur', 'biru and orang', 'kamu jelek')
beo.cetak_burung()

#object kedua
print('----- object kedua -----')
merpati = burung('burung merpati', 'biji-bijian','udara', 'bertelur', 'putih', 'cuakss')
merpati.cetak_burung()