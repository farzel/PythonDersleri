#ornek: disaridan girilen urun adina gore kullaniciya o urunun hangi reyonda yer aldigini soyleyen uygulama yaziniz.
# domate biber patlican = manav reyonu
# dis macunu parfum sampuan = kozmetik reyonu
# cep telefonu bilgisayar tablet = teknioloji reyonu

try:
    urun = input('Lutfen urunun adini giriniz:')# input().lower() yazabilirsin
    urun = urun.lower().replace("ı","i").replace("ş","s").replace("ü","u")
    if urun == 'dotames' or urun == 'patlican' or urun == 'biber':
        print(urun,'Manav reyonunda yer almaktadir.')
    elif urun == 'dis macunu' or urun == 'parfum' or urun == 'sampuan':
        print(urun,'Kozmetik reyonunda yer almaktadir.')
    elif urun == 'bilgisayar' or urun == 'cep telefonu' or urun == 'tablet':
        print(urun,'Teknoloji reyonunda yer almaktadir.')
    else:
        print('Bu urun stoklarda bulunmamaktadir.')
except Exception as error:
    print(error)
    print('Gecersiz urun ismi.')