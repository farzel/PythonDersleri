sehirler = ['Adana','Ankara','Ardahan','Amasya','Edirne']

# dizi icerisinde yer alan elemanlarin ismi icerisinde 'm' harfi bulunanlarin yazdirilmasi

for sehir in sehirler:
    if 'm' in  sehir:
        print(sehir)
    else:
        print(sehir, 'icerisinde \'m\' harfi gecmemektedir.')