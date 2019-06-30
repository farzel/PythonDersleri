#ornek: disaridan girilen kelimenin uzunluk degeri 8 karakter veya daha uzun bir karakter ise onaylandi, degil ise daha uzun bir sifre giriniz.

word = input('lutfen bir kelime giriniz:')#len(input()) da olur
if len(word) >= 8:
    print('sifreniz onaylandi')
    print("Sifreniz:",word)
else:
    print('Daha uzun bir sifre giriniz.')
