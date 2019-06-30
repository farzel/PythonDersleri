try:
    sayi = int(input('sayi giriniz:'))
    print('tebrikler')
except:
    print('Hata aldik')
finally:
    print('er islemin sonucunda calisir')
    #Connection.close()