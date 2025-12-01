# # Создаем класс Student (Шаблон для студентов)
# class Student:
#     def __init__(self, id, name, surname, age):
#         # __init__ - это конструктор который задает свойства обьекта
#         self.id = id # Айди студента
#         self.name = name # Имя студента
#         self.surname = surname # Фамилия студента
#         self.age = age # возраст
#
#     def info(self): #Метод info выводит информацию про студента
#         print(f'ID Студента: {self.id}, имя и фамилия {self.name}'
#               f' {self.surname} возраст: {self.age} ')
#
#
# #Создаем обьекты на основе класса
# student_id1 = Student(1, "Аскат", "Бурханов", 18)
# student_id2 = Student(2, "Чынгыз", "Токтобаев", 14)
# #Вызываем метод info для каждого обьекта
# student_id1.info()
# student_id2.info()


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#         print('Создано животное')
#
# class Dog(Animal):
#     def __init__(self, name, bread):
#         super().__init__(name)
#         self.bread = bread
#         print('Создано собака')
#
# s = Dog('Рекс', 'Овчарка')

# print(s.name, s.bread)

# class Human:
#     def __int__(self, name):
#         self.name = name
#         print('Создан Человек')
#
#     def introduce(self):
#         print(f'Я человек, меня зовут {self.name}')
#
#
# class Teacher(Human):
#     def __init__(self, name, subject):
#         super().__int__(name)
#         self.subject = subject
#         print("Создан учитель")
#
#     def introduce(self):
#         print(f'Я учитель {self.name}, я преподаю {self.subject}')
#
#
# h = Human("Айбек")
# t = Teacher('Мария', 'Английский')
# t2 = Teacher('Манас', 'Немецкий')
#
#
# print()
# people = [h, t, t2]
#
# for person in people:
#     person.introduce()
#

# class User:
#     def __init__(self,name, age, balance):
#         self.__name = name
#         self.__age = age
#         self.__balance = balance
#
#     def set_age(self, new_age):
#         if new_age < 0:
#             print('Возраст не может быть отрицательным')
#         else:
#             self.__age = new_age
#
#     def set_balance(self, new_balance):
#         if new_balance < 0:
#             print("'Баланс не может быть отрицательным")
#         else:
#             self.__balance = new_balance
#
#     def get_info(self):
#         return f'Имя {self.__name}, Возраст: {self.__age}, Баланс: {self.__balance} сом '
#
#
# name = input("VVedite imya:")
# age = int(input("Vedite vozrast: "))
# balance = int(input("Vedite balance: "))
#
# user = User(name, age, balance)
#
# print('\n Старые данные')
# print(user.get_info())
#
# new_age = int(input('Vedite novyi vozrast: '))
# user.set_balance(new_age)
#
#
# print('Obnavlennye dannye')
# print(user.get_info())


class User:
    def __init__(self, name, age, balance):
        self.__name = name
        self.__age = age
        self.__balance = balance

    def set_age(self, new_age):
        if new_age < 0:
            print('Возраст не может быть отрицательным')
        else:
            self.__age = new_age

    def set_balance(self, new_balance):
        if new_balance < 0:
            print("Баланс не может быть отрицательным")
        else:
            self.__balance = new_balance

    def get_info(self):
        return f'Имя: {self.__name}, Возраст: {self.__age}, Баланс: {self.__balance}'


name = input('Введите Имя: ')
age = int(input('Введите возраст: '))
balance = int(input('Введите баланс: '))
user = User(name, age, balance)

print('\n Старые данные')
print(user.get_info())

new_age = int(input('Введите новый возраст: '))
user.set_age(new_age)

new_balance = int(input('Введите новый баланс: '))
user.set_balance(new_balance)

print('\n Новые данные')
print(user.get_info())
