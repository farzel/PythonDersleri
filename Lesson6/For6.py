# sifrenin 3 defa yanlis girilmesi halinde kullaniyi uyaran uygulama
from builtins import print
for i in range(3):
    pw = input('Lutfen sifrenizi giriniz:')
    if i == 2: #sifre 3 defa yanlis girildi
        print('Sifrenizi 3 defa yanlis girdiniz')
    elif not pw: #alan bos gecilirse
        print('Parola bos gecilemez')
    elif len(pw) in range(3,8): #parola 3 ile 8 karakter araliginda olmalidir.
        print('Parolaniz:',pw,'olarak belirlenmistir.')
        break
    else:
        print('wp')


