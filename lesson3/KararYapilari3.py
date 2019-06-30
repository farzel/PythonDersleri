# ornek: Disaridan girilen sayinin tek veya cift olma durumunun kontrol edilmes. Eger sayi tek ise kullaniciya sayi tektir, cift ise sayi cifttir uyarisi veriniz.
try:
    num = float(input('Lutfen sayinizi giriniz:'))
    if num % 2 == 0:
        print('sayiniz cift.')
    else:
        print('sayiniz tek.')
except Exception as exp:
    print(exp)
    print('belirlenemeyen hata tipi.')
