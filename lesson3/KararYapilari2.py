# ornek: girilen not degeri 0'dan kucuk ise 0'dan kucuk not giremezsiniz. 100'den buyuk bir deger giremezsiniz 100'den buyuk not girisi yapamazsiniz uyari verdiren uygulama yazin.



try:
    grade = float(input('Lutfen notunuzu girin:'))
    if(grade < 0):
        print("0'dan kucuk not giremezsiniz.")
    elif(grade > 100):
        print("100'den buyuk not giremezsiniz.")
    else:
        print('Notunuz:', grade)
except ValueError as exp:
    print('Lutfen sayisal veri giriniz.')
except Exception as exp:
    print('Belirlenemeyen bir hata cesidi')