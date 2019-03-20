print('Простой todo: \n 1. Добавить задачу. \n 2. Вывести список задач. \n 3. Выход.')

a=int(input('Укажите число: '))
result=[]
x=[]

while a!=3:
    if a==1:
        zadacha=input('Сформулируйте задачу: ')
        kategoria=input('Добавьте категорию к задаче: ')
        vrema=input('Добавьте время к задаче: ')
        x='Задача: '+zadacha+' Категория: '+kategoria+' Дата: '+vrema
        result.append(x)
        x=[]
    elif a==2:
        print(result,'\n')

    a=int(input('Укажите число: '))
