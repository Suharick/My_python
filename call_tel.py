kod=int(input('Введите код города: '))
minut=int(input('Введите кол-во минут: '))

def f(minut):
    if kod==343:
        return minut*15
    elif kod==381:
        return minut*18
    elif kod==473:
        return minut*13
    elif kod==485:
        return minut*11

print(f(minut))
