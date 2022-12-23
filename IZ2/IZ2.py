# Задание 7 Разработать класс «Записная книжка». Предусмотреть
# возможность работы с переменным числом студентов, поиска записи по
# какому-либо признаку (фамилия, дата рождения, номер телефона и .д.),
# добавление и удаление записей, сортировки по разным полям.

class studgroup():
    students=[]
    def __init__(self):
        pass
    def Push(self):
        Name=input('Фамилия')
        BrDate=input('Дата рождения')
        Phone=input('Номер телефона')
        a=[Name,BrDate,Phone]
        self.students.append(a)
    def Removal(self):
        NameDel=input("Введите фамилию на удаление")
        for i in self.students:
            if NameDel in i:
                self.students.remove(i)
                print('Удалено')
            else:
                print('Такого студента нет')
    def FindName(self):
        NameFind=input('Введите имя студента')
        for i in self.students:
            if NameFind in i:
                print(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')
            else:
                print('Такой записи нет')
    def sorting(self):
        self.students.sort()
    def see(self):
        for i in self.students:
            print(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')

Spisok=studgroup()
Spisok.Push()
Spisok.Push()
Spisok.Push()
Spisok.see()
