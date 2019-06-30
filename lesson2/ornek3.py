#Hata mesaji

try:
    sayi = int(input('Lutfen sadece sayisal veri giriniz: '))
    print('gelen sayi',int(sayi))
    #sayi = sayi / 0
    sayi = str(sayi)/0
    print('Islem sonu')
    print('islem sonu')
except ValueError as ex:
    print('ValueError')
    print('Sistem hata mesaji',ex)
except ZeroDivisionError as ex:
    print('ZeroDivisionError')
    print('Sistem hata mesaji', ex)
except Exception as ex:
    print('except')
    print('Sitem hata mesaji:', ex)

