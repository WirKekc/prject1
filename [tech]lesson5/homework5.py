# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека


class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.know_list = []

    def know(self, person):
        self.know_list.append(person)

    def is_known(self, person):
        if person in self.know_list:
            print('Есть в друзьях')
        else:
            print('Нет в друзьях')


person1 = Person(30, 'Nick')
person2 = Person(25, 'Lise')
person3 = Person(43, 'Max')

person1.know(person2)
person1.is_known(person2)
person1.is_known(person3)
person3.is_known(person2)

# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *


class Printer(object):
    def log(self, *values):
        print(*values)


class FormattedPrinter(Printer):
    def log(self, *values):
        for value in values:
            print(f'*{value}*')


text1 = Printer()
text1.log('df', 'd')

text2 = FormattedPrinter()
text2.log('hhh', 'rytf')


# *ЗАДАЧА 3:
# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

# Слегка дополнил задачу:
# Человек наследуется от животного.
# И у животных и у людей добавлен параметр агрессии.
# У животного и у человека есть метод Атаковать человека.
# Если параметр агрессии у нападающего и жертвы совпадает считается,
# что жертва отбилась и не считает нападавшего опасным.
# В противном случае жертва добавляет нападающего в перечень опасных для себя существ

class Animal(object):
    def __init__(self, name, aggressive):
        self.name = name
        self.aggressive = aggressive

    def attack(self, animal):
        if animal.aggressive and not self.aggressive:
            self.dangerous_list.append(animal)
            print(f'Атака {animal.name} на {self.name} была успешной')
        else:
            print(f'Атака {animal.name} на {self.name} была провалена')


class Human(Animal):
    def __init__(self, name, aggressive):
        super().__init__(name, aggressive)
        self.dangerous_list = []

    def is_dangerous(self, animal):
        answer = {True: f'{animal.name} - Опсасно', False: f'{animal.name} - Не опасно'}
        return answer[animal in self.dangerous_list]


tiger = Animal('tiger', True)
jack = Human('Jack', False)
rocky = Human('Rocky', True)
bird = Animal('bird', False)

jack.attack(tiger)
print(jack.is_dangerous(tiger))

jack.attack(bird)
print(jack.is_dangerous(bird))

rocky.attack(tiger)
print(rocky.is_dangerous(tiger))
