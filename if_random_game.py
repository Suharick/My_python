import random
a=int(input('Введите число от 1 до 4: '))
b=random.randint(1,4)
if a==b:
    print('Победа')
else:
    if a>b:
        print('Больше')
    else:
        print('Меньшеё')
    
