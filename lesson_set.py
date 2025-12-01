# str # не изменяемый, упорядочный
# int # не
# bool # не изменяемый
# complex #не изменяемый
# float #не изменяемый
# list # изменяемый, упорядочный
# set # изменяемый
# dict # изменяемый
# frozenset
# tuple # не изменяемый

# set1 = {'sdfghjkl', 3456, 0, 1, 22, 22}
# print(set1)
#
# dict1 = {
#     'name': 'Aslan',
#     'age': 18,
#     'surname': 'Bakytov'
# }
#
# print(dict1)
#
#
# names = ['Айбек', 'Асель', 'Айбек', 'Мирлан', "Аскат", 'Анас']


#
# unique_names = set(names)
#
# print(unique_names
#
#
# dict1 = {
#     'name': 'Aslan',
#     'age': 18,
#     'surname': 'Bakytov'
# }
#
# print(dict1.values()) # вернет только значении
# print(dict1.keys()) # вернет ключи
# print(dict1.clear()) #очищает словарь
#
# frozenset

# # for - когда мы заранее знаем, сколько раз нужно повторить
# for i in range(1, 102, 2): # первое число это старт(start), второе это стоп(stop), третье это шаг(step)
#     print(i)
#
# # while - когда повторяем пока выполнится условие
# x = 1
# while x <= 100: # пока x меньше или равно 100
#     print("Счет: ", x)
#     x += 2  # увеличивает x на 2


# for i in range(1, 11):
#     print('Проверяем число', i)
#     if i == 7:
#         print(" нашел число 7 Останавливаюсь")
#         break # остановить цикл полностью

# for x in range(1,11):
#     if x == 3:
#         continue # пропустить одну итерацию
#     print("Число: ", x)

# x = 1
# while True:
#     print('x = ', x)
#     x += 1

# for i in range(1,11):
#     if i % 2 != 0:
#         print(i, "---  не четные числа")

# def say_hello(name, age,):
#     print("Привет меня зовут", name, 'мне', age)
#
# say_hello('Аскат', 18)
# say_hello('Баяман', 14)

# def add(san1, san2):
#     print(san1 + san2)
#
# add(4,5)






# def add_numbers(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total
#
# print(add_numbers(2,4,6))
# print(add_numbers(1,2,3,4,5))
#
# def  show_info(**kwargs):
#     print(kwargs)
# show_info(name='Омар', age=14, city="Бишкек")
#


def check_password():
    while True:
        password = input("Введите пароль: ")
        if password == "python123":
            print("Пароль верный! Добро пожаловать!")
            break
        else:
            print("Неверный пароль, попробуйте снова.")

check_password()
