print('Selamat datang di aplikasi sederhana')
print('Pilih menu')
menu1 = print('1. perkalian')
menu2 = print('2. cek ganjil genap')

inputMenu = int(input('Pilih : '))

while True :
    if inputMenu == 1 :
        print('menu ini sedang di maintenance')
        break
    elif inputMenu == 2 : 
        Input = input('Masukkan Bilangan Bulat : ')
        Numbers = int(Input)
        if Numbers % 2 == 0 : print('Genap')
        else : print('Ganjil')
