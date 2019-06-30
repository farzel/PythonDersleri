# disaridan girilen metni harf harf alt alta yazdiriniz

text = input('Lutfen metninizi giriniz:')
result = ' '
for i in text:
    print(i) #result = i + ' '

print('-'.join(text))