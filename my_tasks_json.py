import json


print('1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
a=int(input('Выберете действие: '))
lst = []
with open('data.json') as file:
    lst = json.load(file)


while a!=3:
    if a==1:
        s1=input('Сформулируйте задачу: ')
        s2=input('Добавьте категорию к задаче: ')
        s3=input('Добавьте время к задаче: ')

        el = {
            'name' : s1,
            'category' : s2,
            'time' : s3
            }
        
        lst.append(el)
        with open('data.json', 'w') as file:
            json.dump(lst, file)

    elif a==2:
        with open('data.json', 'r') as file:
            print(file)


    print('1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
    a=int(input('Выберете действие: '))

print('Задачи сохранены в файл!')
