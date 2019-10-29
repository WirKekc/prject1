# 1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError,
# если оно больше 10 - IndexError. Обрабатываем ошибку, говорим пользователю, в чем его ошибка


# num = int(input())
# try:
#     if num%2 == 0:
#         raise ValueError('Четное число')
#     if num < 0:
#         raise TypeError("Число меньше 0")
#     if num > 10:
#         raise IndexError("Чичло больше 10")
# except ValueError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except IndexError as e:
#     print(e)


# 2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть.
# Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так

# list1 = [1, 'lol', "34", [1, 34, "hohohoh"], ("fghj", 345)]
# try:
#     print(list1[int(input("Введите индекс объекта: "))])
# except IndexError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)


# 1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0

# def sum_dif(x, y):
#     if x > 0 and y > 0:
#         return x + y
#     elif x < 0 and y < 0:
#         return x - y
#     else:
#         return 0
#
#
# print(sum_dif(-9, -5))

# Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
#
# def max_2(a, b, c):
#     if a < b and a < c:
#         print(b, c)
#     elif b < a and b < c:
#         print(a, c)
#     elif c < a and c < b:
#         print(a, b)
#
#
# max_2(15, 20, 113)
# ----------------------------------
# def function(x,y,z):
#     lst = [x,y,z]
#     lst.sort()
#     print(lst[1],lst[2])
# function(8,5,10)

# Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг.
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка,
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка

# def chet(b, *a):
#     nch, ch = [], []
#     b = bool(b)
#     for i in a:
#         if i%2 == 1:
#             nch.append(i)
#         else:
#             ch.append(i)
#     if b:
#         print(nch)
#     else:
#         print(ch)
#
#
# chet(False, 1, 2, 3, 4, 5, 6)

# Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. И возвращает оба

# def min_max(*nums):
#     mi = nums[0]
#     ma = nums[0]
#     for num in nums:
#         if num > ma:
#             ma = num
#         if num < mi:
#             mi = num
#     return mi, ma
#
#
# print(min_max(1, 2, -55, 1, 26, 85, 4, 25543, 46))

# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему

# def reg(string, case=True):
#     if case:
#         return string.upper()
#     else:
#         return string.lower()
#
#
# print(reg('HSGDJ'))

# Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue,
# который равен ':'. Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
# Для соединения между любых двух строк вставлять glue

# def fun(*strings, glue=':'):
#     a = []
#     for i in strings:
#         if len(i) > 3:
#             a.append(i)
#
#     return glue.join(a)
#
#
# print(fun('Hello', 'my', 'friend', 'popj', 'sdcw'))

# Игра уградай число
# import random
#
# rand = random.randint(0, 999)
# while True:
#     num = int(input('Введите число:'))
#     if num > rand:
#         print('Слишком большое. Попробуйте еще раз!')
#     elif num < rand:
#         print('Слишком маленькое. Попробуйте еще раз!')
#     else:
#         print('Поздравляю, Вы угадали!')
#         break

# ---------------------------------------------------------------------
# class Basket:
#     def __init__(self, size):
#         self.size = size
#
#     def change_size(self, size):
#         self.size = size
#
#     def get_size(self):
#         print('Basket size is {}'.format(self.size))
#
#     def put_in_basket(self, smth):
#         if smth <= self.size:
#             print('{} is in Basket'.format(smth))
#         else:
#             print('{} is to big for a Basket with size = {}'.format(smth, self.size))
#
#
# basket = Basket(123)
# basket.get_size()
#
# basket.change_size(55)
# basket.get_size()
#
# basket.put_in_basket(34)
# basket.put_in_basket(345)

# -------------------------------------------------------------------------------------
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека
#
# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#         self.friends = []
#
#     def know(self, person):
#         self.friends.append(person)
#         print("{} add in {}'s friends ".format(person.name, self.name))
#
#     def is_known(self, person):
#         if person in self.friends:
#             print("{} in {}'s friends".format(person.name, self.name))
#             return True
#         else:
#             print("{} not in {}'s friends".format(person.name, self.name))
#             return False
#
#
# d = Person(15, 'Dmitry')
# g = Person(17, 'Galina')
# d.know(g)
# d.is_known(g)
# g.is_known(d)

# -----------------------------------------------------------------------
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
#

# class Printer:
#     def __init__(self):
#         self.values = []
#
#     def log(self, *values):
#         self.values = [v for v in values]
#         print(self.values)
#
# class FormattedPrinter(Printer):
#     def formated_log(self, *values):
#         print('*********************************')
#         self.log(*values)
#         print('*********************************')
#
# d = FormattedPrinter()
# d.formated_log('lol', 'kek')

# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)
# Слегка дополнил задачу:
# Человек наследуется от животного.
# И у животных и у людей добавлен параметр агрессии.
# У животного и у человека есть метод Атаковать человека.
# Если параметр агрессии у нападающего и жертвы совпадает считается,
# что жертва отбилась и не считает нападавшего опасным.
# В противном случае жертва добавляет нападающего в перечень опасных для себя существ

class Animal:
    def __init__(self, name, aggression):
        self.name = name
        self.aggression = aggression
        self.dangerous = []

    def attack_human(self, human):
        if human.aggression < self.aggression:
            print('{} died.'.format(human.name))
        else:
            print('{} alive!'.format(human.name))

class Human(Animal):

    def is_dangerous(self, animal):
        if animal.aggression > self.aggression:
            self.dangerous.append(animal.name)
            print('Dangerous!!!')
        else:
            print('Not dangerous')
