while True:
    sifre = input('Lutfen sifre giriniz:')
    if not sifre:
        pass
    elif len(sifre) in range(3,8):
        print('yeni sifreniz:',sifre)
        break
    else:
        print('sifre 3 ile 8 karakter araliginda olmalidir.')
