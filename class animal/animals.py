class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak (self):
        print(f'hewan {self.nama} ini makanan{self.makanan}, hewan ini juga hidup di{self.hidup}dan berkembang biak dengan cara{self.berkembang_biak}')

c1 = animal('buaya', 'daging', 'amphibi', 'berttelur')
c1.cetak()