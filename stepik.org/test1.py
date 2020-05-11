# print('Hellow world')
# a = [1, 3, 2, 5]
# try:
#     print(a.index(3))
# except ValueError:
#     print(None)

# a = int(input())
# if a == -10 or (-5 < a <= 3) or (8 < a < 12) or (16 <= a):
#     print(True)
# else:
#     print(False)

# a = "hi, man!"
# print(a[0].upper())
#
#
# def t():
#     print('true')
#     return True
#
# def f():
#     print('false')
#     return False
#
# if t() and f():
#     print('t and f')
#
# if f() and t():
#     print('f and t')
#
# if t() or f():
#     print('t or f')
#
# if f() or t():
#     print('f or t')

# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(sum_all(1,300,5))

# import random
#
# def random_err():
#     random_num = random.randint(0, 2)
#     try:
#         if random_num == 0:
#             raise ValueError('ValueError')
#         if random_num == 1:
#             raise TypeError('TypeError')
#         if random_num == 2:
#             raise RuntimeError('RuntimeError')
#     except ValueError as e0:
#         print(e0)
#     except TypeError as e0:
#         print(e0)
#     except RuntimeError as e0:
#         print(e0)
#
# random_err()

# def list_sort(nums):
#     a = []
#     try:
#         for i in nums:
#             a.append(int(i))
#     except ValueError as e:
#         print(e)
#
#     return sorted(a)
#
#
# print(list_sort([5, 7, 9, 5, '4', 'sgf']))


