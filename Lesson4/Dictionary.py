# Dictionary key value formatinda datalari listelemek icin kullanilir. Json formatinda data tutar, MongoDb, WebApi (servisler), JavaScript (vue js, angular js, angular iom reactm react nativen cordova vs) gibi bir cok platform bunu destekler.

personeller = [
    {
        'Id'        : 1,
        'IndexNo'   : 0,
        'FirstName' : 'faruk',
        'LastName'  : 'guzel',
    },
    {
        'Id'        : 2,
        'IndexNo'   : 1,
        'FirstName' : 'ahmet',
        'LastName'  : 'guzel',
    },
    {
        'Id'        : 3,
        'IndexNo'   : 2,
        'FirstName' : 'ahmet faruk',
        'LastName'  : 'guzel',
    }
]
# listenin verilen index degerine gore o elemani ekrana yazdirma
print(personeller[0])
# {'Id' : 1,         'FirstName' : 'faruk',        'LastName'  : 'guzel',
# dizi icersiinde eger bir index degerindeki elemanin herhangi bir property'sini ekrana yazdirmak icin:
print(personeller[0]['FirstName'])
# Murat
print(personeller[0]['LastName'])
# Vuranok

# liste icerisinde yer alan bir elemani guncellemek istiyorsaniz
guncellenecekIndex = 2
guncellenecekKey = 'FirstName'

oldName = personeller[guncellenecekIndex][guncellenecekKey]

personeller[guncellenecekIndex][guncellenecekKey] ='Okan'
print(oldName,'adli personelin yeni adi: ', personeller[2]['FirstName'],'Olarak guncellenmistir.')

personeller.append(
    {
        'Id'        : 4,
        'IndexNo'   : 3,
        'FirstName' : 'cristiano',
        'LastName'  : 'ronaldo'
    }
)

print('personel adi:',personeller[3]['FirstName'] ,'\nPersonel soyadi:', personeller[3]['LastName'] )
#print(personeller[:])
print('Personelin Adi: {0}\nPersonel Soyadi: {1}'.format(personeller[3]['FirstName'],personeller[3]['LastName']))
# eger format icerisinde index degeri belirtmezseniz default olarak 0,1,2... gibi devam eder.
# format icierisinde verdiginiz ilk deger 0. index degeridir.
