a = input().lower().split()
[print(i, a.count(i)) for i in set(a)]
# b = list(set(a))
# for i in range(len(b)):
#     print(b[i], a.count(b[i]))

