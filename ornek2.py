try:
    sayi_bir = int(input('Lutfen birinci sayiyi giriniz: '))
    sayi_iki = int(input('Lutfen ikinci sayiyi giriniz: '))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    bolum = sayi_bir / sayi_iki
    carpim = sayi_bir * sayi_iki


    print('sayilarin toplami:',toplam,'\nSayilarin Farki:',fark,'\nSayilarin bolumu:',bolum,
          '\nSayilarin Carpimi:',carpim)

except (ValueError,SyntaxError):
    print('Value Error hatasi veya Syntax error hatasi')
except ZeroDivisionError:
    print('Zero Division error hatasi')
except FileExistsError:
    print('File Exist Error')
except:
    print('Hata mesaji')