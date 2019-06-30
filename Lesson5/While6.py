#disaridan girilen sayilarin birbirleriyle olan toplam degerini teslem eden uygulama (123 = 6)


num = input('Lutfen bir sayi giriniz:')
index = 0
result = 0
while index < len(num):
    result += int(num[index])
    index = index + 1
    print(result)