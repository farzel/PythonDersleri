# karar yapilari if - elif - else

# karsilastirma operatorleri

# == (Esittir operatoru) soldaki operatorun soldaki degere esit olma durumu
# ornek: 1==1 sonuc ==> True,
# ornek: 4==2 sonuc ==> False

# != (Esit degildir) soldaki degerin, sagdaki degere esit olmama dururmu
# ornek: 1 != 2 sonuc => True
# ornek: 1 != 1 sonuc => False

# > (Buyuktur) Soldaki degerin sagdaki degerden buyuk olma durumu
# ornek: 3 > 1 sonuc => True
# ornek: 1 > 2 sonuc => False

# < (kucukcuktur) soldaki degerin sagdaki degerden kucuk olma durumu
# ornek: 1 < 2 sonuc => True
# ornek: 4 < 1 sonuc => False

# >= (buyuk veya esit) soldaki degerin sagdaki degerden buyuk veya esit olma durumu
# ornek: 1 >= 1 sonuc => True(esitlik)
# ornek: 3 >= 2 sonuc => True(buyukluk)
# ornek: 1 >= 2 sonuc => False

# <= (kucuk veya esit) soldaki degerin sagdaki degerden kucuk veya esit olma durumu
# ornek: 1 <= 1 sonuc => True(esitlik)
# ornek: 1 <= 3 sonuc => True(kucukluk)
# ornek: 4 <= 1 sonuc => False

username = input('Lutfen kullanici adini giriniz:')
username = username.lower().replace("ı","i").replace("ç","c").replace("ş","s").replace("ö","o").replace("ğ","g")
print(username)
if(username=='admin'):
    print('Giris yaptiniz')
else:
    print('Kullanici adiniz hatali')
