print('---- celcius ke fahrenheit ----')
def celcius_ke_fahrenheit(celcius):
    print(celcius*9/5 + 32)
celcius_ke_fahrenheit(0)

print('---- mencari bilangan genap ----')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('---- melihat keterangan lulus atau tidak ----')
#rata' nilai kelulusan 70
def skor(nilai):
    if nilai >= 70:
        print('lulus')
    else:
        print('gagal')

skor(80)
skor(40)

print('----menampilkan bilangan ganjil yang kurang argumen ----')
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=' ')
bil_ganjil(20)