# def f(x):
#     x += 2
#     return x
#
#
# a = {}
# n = int(input())
# m = [(int(input())) for i in range(n)]
# # print(m)
# for i in range(n):
#     if m[i] in a:
#         print(a[m[i]])
#     else:
#         a.update({m[i]: f(m[i])})
#         print(a[m[i]])

# print(f(3))
#
# import sys
# chrCounter = 0
#
# for line in sys.stdin:
#     chrCounter += len(line)
#
# print(chrCounter)

# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
# import sys
# from functools import lru_cache
#
#
# def f(x):
#     x += 2
#     return x
#
# @lru_cache()
# def func(x):
#     return f(x)
#
#
# x = input() # Просто так. Можно и без него, но по условию нужен ввод
# for i in sys.stdin:
#     print(func(int(i)))
