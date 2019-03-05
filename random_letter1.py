spisok=['самовар', 'весна', 'лето']
import random
i=random.randint(0,2)

slovo=spisok[i]

k=len(slovo)

j=random.randint(0,k-1)

bukva=slovo[j]

a=list(slovo)

a[j]='?'
a= ''.join(a)
print(a)

variant=input('Введите букву: ')
if variant==bukva:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз.')
