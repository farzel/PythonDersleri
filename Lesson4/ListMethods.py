# .append() dizi icerisine eleman eklemek icin kullanilir (JacaScript dilinde de ayni yontem gecerlidir.)
# .append() ekleme islemine diznin sonundan baslar eklenen her bir eleman dizinin son elemanidir.
sehirler = []

sehirler.append('ankara')
# bu alana insert yapacak.
sehirler.append('istanbul')
sehirler.append('edirne')
sehirler.append('istanbul')
sehirler.append('izmir')
sehirler.append('malatya')
print(sehirler[:])

# .insert() dizinin icerisinde belirtilen alana ekleme islemi yapar.(araya eleman ekleme)
sehirler.insert(1, 'sivas')
print(sehirler[:])
# 1. Parametre hangi index degerine
# 2. Parametre o index degerine hangi eleman eklenecek?
print(sehirler[:])
# .count() dizi icerisinde yer alan elemanlarin, liste icerisinde kac defa gectigini teslim eder.

print('dizi icerisinde istanbul',sehirler.count('istanbul'),'adet icermektedir')

# .pop() dizi icerisinde eleman silme; parametre verilirse verilen index degerindeki elemani siler, parametre verilmez ise dizinin en son elemanini siler.
# .pop() metodunun ozelligi silinen elemani geriye teslim eder.

# print(sehirler[:])
# print(sehirler.pop(1))
# print(sehirler[:])

# ['ankara', 'sivas', 'istanbul', 'edirne', 'istanbul', 'izmir', 'malatya']
# sivas
# ['ankara', 'istanbul', 'edirne', 'istanbul', 'izmir', 'malatya']

print(sehirler[:])
print(sehirler.pop())
print(sehirler[:])

# ['ankara', 'sivas', 'istanbul', 'edirne', 'istanbul', 'izmir', 'malatya']
# malatya
# ['ankara', 'sivas', 'istanbul', 'edirne', 'istanbul', 'izmir']

# .remove() dizi icerisinde eleman silme; eleman silmek icin objtect olarak nsne ister (pop index mantigiyla, remove ise object object mantigiyla calisir)
# index degeri uzerinden eleman silme islemi gerceklestirmez. Eger iceride ayni degere sahip(2 adet istanbul gibi) eleman var ise soldan saga dogru buldugu ilk elemani silecektir.
# .remove()metodu geriye silinen elemani teslim etmez!!!

sehirler = []

sehirler.append('ankara')
sehirler.append('istanbul')
sehirler.append('edirne')
sehirler.append('istanbul')
sehirler.append('izmir')
sehirler.append('malatya')
print(sehirler[:])
print(sehirler.remove('istanbul'))
print(sehirler[:])

# .sort() dizinin elemanlarini A'dan Z'ye , 0'dan 9'a siralama islemi yapar

sehirler = []

sehirler.append('ankara')
sehirler.append('istanbul')
sehirler.append('edirne')
sehirler.append('istanbul')
sehirler.append('izmir')
sehirler.append('malatya')
print(sehirler[:])
print(sehirler.sort())
print(sehirler[:])

# .reverse() dizi icerisindeki elemanlari tersine siralar, kesinlikle siralama islemi yapmaz. Diziyi oldugu gibi tersten yazdirir.

print(sehirler[:])
sehirler.reverse()
print(sehirler[:])

print(len(sehirler))
print(sehirler[:])
# del sehirler # sehirler dizisini tamamen siler, artik sonraki kod bloklarina bi elemena ulasamazsiniz!
# print(len(sehirler))
# print(sehirler[:])