#Задание_1
print("Задание 1:")
class Cat():
    name = ""
    color = ""
    weight = ""
    def Meow():
        print("Мяу!")

myCat = Cat()
myCat.name = "Kitty"
myCat.color = "White"
myCat.weight = "2 kilo"
Cat.Meow()
#Задание_2
print("Задание 2:")
class Animal():
    name = ""
    def __init__(self,newName):  # конструктор базового класса
        self.name = newName
        print("Родилось животное ", newName)
    def eat(self):
        print("Намнем")
    def setName(self,newName):
        self.name = newName
    def getName(self):
        print(self.name)
    def makeNoise(self):
        print(self.name, "говорит Гррр")
newAnimal = Animal("Акула")
newAnimal.getName()
newAnimal.setName("Хрюня")
newAnimal.eat()
newAnimal.makeNoise()
#Задание_3
print("Задание 3:")
class StringVar:
    def __init__(self):
         self.str = ''
    def set (self, newStr):
        self.str = newStr
    def get (self):
        return self.str
s = StringVar()
print(s.set('строка'))
print(s.get())
#Задание_4
print("Задание 4:")
from math import sqrt
class Point:
 def __init__(self, x, y):
  self.x = x
  self.y = y

 def x(self):
  return self.x

 def y(self):
  return self.y

 def d(self,point):
     return sqrt((self.x-point.x)**2+(self.y-point.y)**2)

newPoint = Point(2,2)
newestPoint = Point(4,4)
print("Растояние между точками равно ", newPoint.d(newestPoint))

#Задание_5
print("Задание 5")
class Animal():
    def __init__(self, name):
        self.name = name
        print("Родилось животное")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Родился кот')

    def makeNoise(self):
        print(self.name, "говорит мау")


myCat = Cat("Котик")
print("По имени",myCat.name)
myCat.makeNoise()
#Задание_6
print("Задание 6")
class Animal():
    def __init__(self, name):
        self.name = name
        print("Родилось животное")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Родился кот')

    def makeNoise(self):
        print(self.name, "говорит мау")
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Родилась собака')

    def makeNoise(self):
        print(self.name, "говорит гав")


myDog = Dog("Собачка")
print("По имени",myDog.name)
myDog.makeNoise()
#Задание_7
print("Задание 7")
class Animal():
    def __init__(self, name):
        self.name = name
        print("Родилось животное")
    def eat(self):
        print("Намнем")
    def makeNoise(self):
        print(self.name, "говорит что то на животном языке")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Родился кот')

    def makeNoise(self):
        print(self.name, "говорит мау")
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Родилась собака')

    def makeNoise(self):
        print(self.name, "говорит гав")

myCat = Cat("Котик")
myDog = Dog("Собачка")
myDog2 = Dog("Собачка2")
myAnimal = Animal("Петух")
myCat.name = "Барсик"
myDog.name = "Шарик"
myDog2.name = "Шарик2"
myCat.eat()
myCat.makeNoise()
myDog.eat()
myDog.makeNoise()
myDog2.eat()
myDog2.makeNoise()
myAnimal.eat()
myAnimal.makeNoise()














