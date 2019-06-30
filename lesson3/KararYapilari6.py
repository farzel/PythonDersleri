# ornek: Disaridan girilen not araligi
#  0 - 30  => FF
# 30 - 50  => DD
# 50 - 70  => CC
# 70 - 85  => BB
# 85 - 100 => AA notunu aldiniz uyarisini kullaniciya veriniz.
try:
    grade = float(input('Lufen notunuzu giriniz:'))
    mesaj = 'Harf notunuz:'
    if grade <= 30 and grade >= 0:
        mesaj += 'FF'
    elif grade <= 50 and grade > 30:
        mesaj += 'DD'
    elif grade <= 70 and grade > 50:
        mesaj += 'CC'
    elif grade <= 85 and grade > 70:
        mesaj += 'BB'
    elif grade <= 100 and grade > 85:
        mesaj += 'AA'
    else:
        mesaj = 'Gecersiz not girdiniz.'
    print(mesaj)
except Exception as error:
    print(error)
    print('Hatali not girisi.')