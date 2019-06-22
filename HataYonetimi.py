#Programci hatalari(Error)
#program kusurlari(Bug)
#Istisnalar (Exceptions)
#Mantiksal hatalar

try:
    telefon_numarasi = input('Lutfen telefion numaranizi giriniz:')
#telefon numarasi veri tabaniina kayit edildi
    print('Telefon numaraniz:',int(telefon_numarasi))
except ValueError:
    print('islem hatasi')
    print('Lutfen gecerli bir sayi giriniz')
except ZeroDivisionError:
    print('Islem Hatasi')
    print('sifira bolunme hatasi')
