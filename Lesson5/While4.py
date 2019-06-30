# 1 ile 1000 arasinda yer alan tek ve cift sayilarin adedini ekrana yazdiriniz.

index = 1
teksayilarintoplami = 0
ciftsayilarintoplami = 0

while index <= 1000:
    if index % 2 ==0:
        ciftsayilarintoplami = ciftsayilarintoplami + 1
    else:
        teksayilarintoplami = teksayilarintoplami + 1
    index = index + 1
print('Tek sayilarin toplami:',teksayilarintoplami,'\nCift sayilarin toplami:',ciftsayilarintoplami)
