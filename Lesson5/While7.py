sayilar = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# dizi icerisinde yer alan elemanlari tek ve cift olarak ayirip ayri ayri dizilere eklemeniz ve islem sonucunda adetlerini kullaniciya bildiridiniz

i = 0
tek = []
cift = []
while i < len(sayilar):
    if sayilar[i] % 2 == 0:
        cift.append(sayilar[i])
    else:
        tek.append(sayilar[i])
    i = i + 1

print('Toplamda Tek Sayilarin adedi:',len(tek),'\nCift sayilarin adedi:',len(cift))