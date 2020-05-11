num = int(input())
num_list = []


def sequence(n):
    if num_list.count(n) < n and len(num_list) < num:
        num_list.append(n)
        sequence(n)
    elif num_list.count(n) == n:
        sequence(n+1)


sequence(1)
print(*num_list)


# def gen():
#     i = 0
#     while True:
#         i += 1
#         for _ in range(i):
#             yield i
#
# a = gen()
# for j in range(int(input())):
#     print(next(a), end=' ')