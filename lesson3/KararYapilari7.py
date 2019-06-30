try:
    grade = float(input('Lufen notunuzu giriniz:'))
    mesaj = 'Harf notunuz:'
    if grade >= 0 and grade <=100:
        if grade <= 30 :
            mesaj += 'FF'
        elif grade <= 50:
            mesaj += 'DD'
        elif grade <= 70:
            mesaj += 'CC'
        elif grade <= 85:
            mesaj += 'BB'
        elif grade <= 100:
            mesaj += 'AA'
        else:
            print('')
    else:
        mesaj = 'Gecersiz not girdiniz.'
    print(mesaj)
except Exception as error:
    print(error)
    print('Hatali not girisi.')