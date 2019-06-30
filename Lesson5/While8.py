# disaridan girilen metin icerisinde yer alan sessli ve sessiz karakterleri ayristiriniz ve kullaniciya metin icerisinde kac adet sesli, kac adet sessiz harf oldugunu bildiriniz

text = input('Lutfen metninizi giriniz:').lower()

sesli = ['a','e','i',"i","u","ü","o","ö"]
i = 0
sh = []
nsh = []

while i <len(text):
    if sesli.count(text[i]):
        sh.append(text[i])
    else:
        nsh.append(text[i])
    i = i + 1

print('Toplam sesli sayi adedi:', len(sh), 'Toplam sessiz sayi adedi:', len(nsh))