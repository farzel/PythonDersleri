try:
    sayi_bir = int(input('Lutfen bolunecek sayiyi giriniz:'))
    sayi_iki = int(input('Lutfen bolunecek olan sayiyi griiniz:'))
except ValueError as exp:
    print('Islem hatasi :', exp)
else:
    try:
        print(sayi_bir/sayi_iki)
    except ZeroDivisionError:
        print('Sayi 0 degerine bolunemez!')