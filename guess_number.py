import random
sayi = random.randint(1, 10)
can = int(input('Kaç can istersiniz: '))                  #SAYI TAHMİN UYGULAMASI
hak = can
sayac = 0
puan = 100

while hak > 0:
    hak -= 1 
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler. {sayac} defada  bildiniz! Toplam puaniniz: {100 - (100 / can  )*(sayac - 1)} ')
        break
    elif sayi > tahmin:
        print('Yukari')
    else:
        print('Aşaği')

    if hak == 0:
        print(f'Hakkiniz Bitti! Tutulan sayi : {sayi} ')