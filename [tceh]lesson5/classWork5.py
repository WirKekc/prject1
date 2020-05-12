# class Car:
#     pass
#
#
# c = Car()
# print(c, type(c))
#
#
# class Room:
#     number = 'Room 34'
#     floor = 4
#
#
# r = Room()
# r1 = Room()
# print(r.number, r1.number)
# print(r.floor, r1.floor)
#
#
# r.number = 12
# r.floor = '5 floor'
# print(r.number, r1.number)
# print(r.floor, r1.floor)
#
#
# class Door:
#     def open(self):
#         print('self', self)
#         print('Door is opened!')
#         self.opened = True
#
#
# d = Door()
# d.open()
#
# d1 = Door()
# d1.open()
#
# class Terminal:
#     def hello(self, user_name):
#         print('self is the object itself', self)
#         print('Hello', user_name)
#
# t = Terminal()
# t.hello('Nikita')
# t.hello('Vova')
#
#
# class Window:
#     is_opened = False
#
#     def open(self):
#         self.is_opened = not self.is_opened
#         print('Window is now', self.is_opened)
#
#
# w = Window()
# w1 = Window()
#
# print('Initial state', w.is_opened, w.is_opened)
#
# w.open()
# print('New state', w.is_opened, w1.is_opened)


# class TestClass:
#     def __init__(self):
#         print('Constructor is called!')
#         print('Self is the object itself!', self)
#
#
# t = TestClass()
# t1 = TestClass()

#
# class Table:
#     def __init__(self, number_of_legs):
#         print('New table has {} legs'.format(number_of_legs))
#
#
# t = Table(4)
# t1 = Table(3)
#
#
# class Chair:
#     def __init__(self, color):
#         self.color = color
#
#
# c = Chair('green')
# print(c, c.color)
#
# c1 = Chair('Red')
# print(c, c1.color)
# print('variable c did not change!', c.color)


# class Parent(object):
#     def __init__(self):
#         print('Parent inited')
#         self.value = 'Parent'
#
#     def do(self):
#         print('Parent do(): {}'.format(self.value))
#
#
# class Child(Parent):
#     def __init__(self):
#         print("Child inited")
#         self.value = 'Child'
#
#
# parent = Parent()
# parent.do()
#
# child = Child()
# child.do()

#
# class Calc(object):
#     def __init__(self, number):
#         self.number = number
#
#     def calc_and_print(self):
#         value = self.calc_value()
#         self.print_number(value)
#
#     def calc_value(self):
#         return self.number * 10 + 2
#
#     def print_number(self, value_to_print):
#         print('-----')
#         print('Number is', value_to_print)
#         print('-----')
#
#
# class CalcExtraValue(Calc):
#     def calc_value(self):
#         return self.number - 100
#
#
# c = CalcExtraValue(3)
# c.calc_and_print()

# --------------------------------------------------------------------
# Инкапсуляция

# class Example(object):
#     def __init__(self):
#         self.a = 1
#         self._b = 2
#         self.__c = 3
#         print('{} {} {}'.format(self.a, self._b, self.__c))
#
#     def call(self):
#         print('Called!')
#
#
# example = Example()
# print(example.a)
# print(example._b)
#
# try:
#     print(example.__c)
# except AttributeError as ex:
#     print(ex)

# --------------------------------------------------------------------
# Полиморфизм

# class Parent(object):
#     def call(self):
#         print('Parent')
#
#
# class Child(Parent):
#     def call(self):
#         print('Child')
#
#
# class Example(object):
#     def call(self):
#         print('Ex')
#
#
# def call_obj(obj):
#     obj.call()
#
#
# call_obj(Child())
# call_obj(Parent())

# Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
# В объекты класса карзины можно вмещать разные объект

class Basket:
    def objects(self, obj):
        l = []
        self.obj = obj
        if isinstance(self.obj, list):
            if len(obj) > 5:
                print('Объект не вмещается')
            else:
                l.append(self.obj)
                print('Объект добавлен в карзну')

        elif isinstance(self.obj, str):
            if len(obj) > 5:
                print('Объект не вмещается')
            else:
                l.append(self.obj)
                print('Объект добавлен в карзну')
        return l

c = Basket()
print(c.objects([1, 2, 3, 4, 5, 6]))
