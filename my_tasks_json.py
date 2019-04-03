def reader(filename):
    '''
    Чтение содержимого json файла 
    '''
    import json    
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e
def writer(filename, numbers):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)

print('1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
a=int(input('Выберете действие: '))
filename = 'data.json'
if reader(filename) == None:
    numbers = []
else: numbers = reader(filename)

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
        numbers.append(el)
        writer(filename, numbers)

    elif a==2:
        print(reader(filename))
    print('1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
    a=int(input('Выберете действие: '))
print('Задачи сохранены в файл!')

