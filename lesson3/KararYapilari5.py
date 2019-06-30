# Mantiksal operatorler

# and sorguya katilan her bir kosulun saglanmasi drumu
# or sorguya katilan herhangi bir kosulun saglanmasi durumu
# not sorguya olumsuzluk katar True is False, False ise True


if user_name == 'admin':

    if password == '123':
        print('Giris yaptiniz')
    else:
        print('Sifreniz yanlis')
else:
    print('Kullanici adiniz yanlis')
    pass

user_name = input('Lutfen kullanici adini giriniz:')
password = input('Lutfen sifrenizi girin')
if user_name == 'admin' and password == '123':
    print('Tebrikler')
else:
    print('Kullanici bilgilerinizi kontrol ediniz.')