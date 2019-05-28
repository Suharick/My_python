import math

with open('temp.txt') as file:
    data=[]
    text=file.readlines()
    for i in text:
        data.append(float(i))
    maxim_temp=max(data)
    minim_remp=min(data)
    sr=sum(data)/len(data)
    
print('Максимальная температура: ',maxim_temp,' Минимальная температура: ',minim_remp,'Средняя температура: ',sr,
      'Уникальные температуры: ',len(set(data)))

