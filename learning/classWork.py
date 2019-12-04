# Написать генерор, который каждый раз возвращает новое случайное значение
# import random
# def genRand():
#     while True:
#         yield random.random()
#
# genRand()
# print(next(genRand()))
# print(next(genRand()))
# print(next(genRand()))

# Написать генератор, который работает как range()
# def genRange(start, stop, step=1):
#     while start <= stop:
#         yield start
#         start = start+step
#
#
# for i in genRange(1, 5, 2):
#      print(i)

# Написать генератор, который работает как map()
# def genMap(func, my_list):
#     for i in my_list:
#         yield func(i)
#
# for i in genMap(str, [2,123]):
#     print(i, type(i))

# Написать генератор, который работает как enumerate()
# def genEnumerate(my_list):
#     i = 0
#     for l in my_list:
#         yield (i, l)
#         i += 1
#
# names = ['Bob', 'Alice', 'Guido']
# for index, value in genEnumerate(names):
#     print(f'{index}: {value}')

# Написать генератор, который работает как zip()
def gen_zip(el1,el2):
    for i in range(len(el1)):
        yield (el1[i], el2[i])

a = [1,2,3]
b = ['a','b','c']
for i in gen_zip(a, b):
    print(i)