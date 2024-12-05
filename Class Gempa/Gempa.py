class Gempa:
    #konstruktor inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # method penentu skala gempa
    def dampak(self):
        #logika/ stetement
        if self.skala < 2: 
            print('tidak berasa')
        elif 2 <= self.skala <= 4:
            print('gempa berdampak bangunan retak')
        elif 4 <= self.skala <= 6:
            print('gempa berdampak bangunan roboh')
        elif self.skala > 6:
            print('gempa besar berpotensi tsunami')
        
        #tampilka lokasi dan skala gempa
        print(f'lokasi gempa: {self.lokasi}')
        print(f'skala gempa: {self.skala}')