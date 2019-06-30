for i in range(10,20):
    for a in range(2, i):
        if i % a == 0:
            j = i/a
            print('{} esittir {}*{}'.format(i,a,int(j)))
            break
        else:
            print(i,'asal sayidir')

