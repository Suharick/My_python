a=input('Введите первое число: ')
b=input('Введите второе число: ')
d=input('Введите операцию +,*,/,-: ')

def f(a,b,d):
    a=float(a)
    b=float(b)
    
    if d=='+':
        return a+b
    elif d=='*':
        return a*b
    elif d=='-':
        return a-b
    elif d=='/':
        return a/b    

try:
    f(a,b,d)
except ValueError:
    print("Ошибка в типе данных!")
except ZeroDivisionError:
    print('Ошибка деления на 0!')


print(f(a,b,d))

