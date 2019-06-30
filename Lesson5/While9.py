from random import randint

# print(randint(1,50)) # max 49, min 1 degerini uretir

# sayisal loto: rastgele 6 adet sayi uretip bunu bir diziye ekleyiniz. ayni sayi dizi icerisinde geciyor ise tekrardan yeni bir numara uretiniz dizi icerisinde yer alan 6 rakam benzersiz olmalidir.

i = 0
nums = []

while i < 6:
    i += 1
    num = randint(1,49)
    if nums.count(num):
        i -= 1
    else:
        nums.append(num)
nums.sort()
print(nums)