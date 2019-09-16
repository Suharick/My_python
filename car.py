class Person:
    
    print('Добро пожаловать в автосалон!\n')
    def  __init__(self, name, adress, mobile, car):
       self.name=name
       self.adress=adress
       self.mobile=mobile
       self.car=car
       print(self.name, 'привез машину', self.car, 'на ремонт')


class Car:
    def __init__(self, car, maker, model, year):
        self.car=car
        self.maker=maker
        self.model=model
        self.year=year

    def price(self, money=0):
        
        if(self.car=='Mercedes'):
            money+=1000
        elif(self.car=='Porsche'):
            money+=1200
        else:
            money+=800
            

        if(self.maker=='Germany'):
            money+=500
        elif(self.maker=='USA'):
            money+=400
        else:
            money+=300
            

        if(self.year>=2010):
            money+=300
        else:
            money+=100


        if(self.model=='Колесо'):
            money+=1000
        elif(self.model=='Окно'):
            money+=900
        elif(self.model=='Двигатель'):
            money+=15000
        else:
            money=0
            print('К сожалению мы не можем это отремонтировать')

        print('Ваш ремонт будет стоить', money, 'рублей\n')



person1=Person('Марк', 'Москва, Красная площадь, 10', '89828765', 'Mercedes')

car1=Car('Mercedes', 'Germany', 'Колесо', 2013)

car1.price()


person2=Person('Боб', 'Санкт-Петербург, Ленина, 8', '89854768', 'BMW')

car2=Car('BMW','USA','Двигатель',2019)

car2.price()


person3=Person('Дэвид', 'Казань, Большевиков, 19', '89812348', 'Porsche')

car3=Car('Porsche','USA','Ручка',2017)

car3.price()
