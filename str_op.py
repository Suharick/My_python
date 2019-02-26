s = "У лукоморья 123 дуб зеленый 456"
print('Индексы буквы Я: ',s.find('я'),'\n')
print('Буква У встречается ',s.count('у'),'раз\n')
if s.isalpha()=='true':
    print('Строка состоит из букв.\n')
else:
    print(s.upper(),'\n')
if len(s)>4:
    print(s.lower(),'\n')
print(s.replace("У","О"),'\n')
