import math
a=int(input('Введите количество цифр после запятой: '))
def g(a):
    return f'{math.pi:.{a}f}'
print(g(a))
