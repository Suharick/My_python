film=upset('Введите название фильма (Пятница, Чемпионы,Пернатая банда): ')
data=upset('Вы покупаете билет сегодня/завтра: ')
time=int(upset('Введите время сеанса: '))
kolich=int(upset('Введите количество билетов: '))

def f(stoimost):
    if film=='Пятница':
        if time==12:
            if data=='завтра':
                if kolich>19:
                    return 250*0.75*kolich
                else:
                    return 250*0.95*kolich
            else:
                if kolich>19:
                    return 250*0.8*kolich
                else:
                    return 250*kolich
        elif time==16:
            if data=='завтра':
                if kolich>19:
                    return 350*0.75*kolich
                else:
                    return 350*0.95*kolich
            else:
                if kolich>19:
                    return 350*0.80*kolich
                else:
                    return 350*kolich
        elif time==20:
            if data=='завтра':
                if kolich>19:
                    return 450*0.75*kolich
                else:
                    return 450*0.95*kolich
            else:
                if kolich>19:
                    return 450*0.8*kolich
                else:
                    return 450*kolich
        else:
            return print('Такого сеанса нет.')
    if film=='Чемпионы':
        if time==10:
            if data=='завтра':
                if kolich>19:
                    return 250*0.75*kolich
                else:
                    return 250*0.95*kolich
            else:
                if kolich>19:
                    return 250*0.8*kolich
                else:
                    return 250*kolich
        if time==13 or 16:
            if data=='завтра':
                if kolich>19:
                    return 350*0.75*kolich
                else:
                    return 350*0.95*kolich
            else:
                if kolich>19:
                    return 350*0.8*kolich
                else:
                    return 350*kolich
        else:
            return print('Такого сеанса нет.')
    if film=='Пернатая банда':
         if time==10:
            if data=='завтра':
                if kolich>19:
                    return 350*0.75*kolich
                else:
                    return 350*0.95*kolich
            else:
                if kolich>19:
                    return 350*0.8*kolich
                else:
                    return 350*kolich
        if time==14 or 18:
            if data=='завтра':
                if kolich>19:
                    return 450*0.75*kolich
                else:
                    return 450*0.95*kolich
            else:
                if kolich>19:
                    return 450*0.8*kolich
                else:
                    return 450*kolich
        else:
            return print('Такого сеанса нет.')
    else:
        return print('Такого фильма нет.')

    
print('Итог: ',f(stoimost))            
                
        
