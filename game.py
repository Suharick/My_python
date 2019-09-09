import random

class Game:

    print("Создано игровое поле 7*7. Игроки могут передвигаться на одну клетку, пока не соберут доп. бонусы.\n")

    # Настройка персонажа
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name=name
        self.life=2
        self.speed=1
        print('Игрок', self.name,'с координатами', x, y)
        
    # Перемещение игрока по игровому ограниченному полю
    def run(self, delta_x, delta_y):
        self.x = (self.x + delta_x)%8
        self.y = (self.y + delta_y)%8
        if(self.x == 0):
            self.x = 1
        if(self.y == 0):
            self.y = 1
        print('Игрок', self.name,'переместился на', self.x, self.y )
        
    # Уменьшение здоровья на 1
    def helf0(self):
        self.life-=1
        print("Здоровье игрока ", self.name, " = ", self.life)
        if(self.life<=0):
            print(self.name, 'убит')

    # Увеличение здоровья на 1
    def helf1(self):
        self.life+=1
        print("Здоровье игрока ", self.name, " = ",self.life)

    # Увеличение скорости на 1
    def faster(self):
        self.speed+=1
        print("Скорость игрока ", self.name, " = ",self.speed)
        
    # Получение координат
    def getcoord(self):
        return (self.x, self.y)
    
    # Стрельба
    def shoot(self, other):
        print('Перестрелка... ')
        print('(игрок', self.name, 'стреляет в', other.name, ')')
        k1=other.getcoord()
        k2=self.getcoord()
        if(k1[0]==k2[0] or k1[1]==k2[1]):
            print('Выстрел удачен')
            other.helf0()
        else:
            print('Промах')

#Создание возможности летать            
        
class Plane(Game):
    def fly(self):
        self.speed=7
        print("Умеет летать.")


# Создание игроков

player1=Plane(1,1,"Plane")
player1.fly()

player2=Game(3,5,"Car")

player3=Game(7,6,"Ship")

# Создание бонусов

print('\n')
print('Бонус здоровья (3,4)')
print('Бонус скорости (7,4)\n')

#player.run(5,-1)

#Начало игры
print('Start game\n')
player1.run(0,1)
player2.run(0,-1)
player2.helf1()
player3.run(0,-1)

player1.run(0,2)
player1.shoot(player3)
player2.shoot(player1)
player2.run(0,-1)
player3.run(0,-1)
player3.faster()
player3.shoot(player1)
