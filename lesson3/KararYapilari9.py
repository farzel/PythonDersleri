# ornek: disaridan siparis alinacak olan kitap miktari girilsin. Siparis sayisi 20'den azsa toplam ucretten %5, 20-50 araliginda ise %10,
# 50-100 araliginda ise %15, 100'den fazla ise %25 indirim yapabilsin. Kitabin birim fiyati => 5tl
# Amac odenecek tutari kullaniciya gostermek
try:
    kitap = float(input('Siparis edeceginiz kitap sayisini giriniz:'))
    ucret = 5
    indirim1 = (kitap*ucret)-(kitap*ucret*0.05) #yerine 0.95 demek daha basit olur aynisi alt satirlar icin de gecerli
    indirim2 = (kitap*ucret)-(kitap*ucret*0.1)
    indirim3 = (kitap*ucret)-(kitap*ucret*0.15)
    indirim4 = (kitap*ucret)-(kitap*ucret*0.2)
    if kitap > 0 and kitap < 20:
        print('Odecek tutar:',indirim1)
    elif kitap >= 20 and kitap < 50:
        print('Odecek tutar:',indirim2)
    elif kitap >= 50 and kitap < 100:
        print('Odecek tutar:',indirim3)
    elif kitap >=100:
        print('Odecek tutar:',indirim4)
    else:
        print("Lutfen 0'dan buyuk bir deger giriniz.")
except Exception as error:
    print(error)
    print('Gecersiz giris.')