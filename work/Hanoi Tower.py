one = int(input())


def hanoi(n, i, k):
    if n == 1:
        print(i, "-", k)
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print(i, "-", k)
        hanoi(n-1, tmp, k)


hanoi(one, 1, 3)
# for i in range(one):
#     if one == 1:
#         one -= 1
#         # three += 1
#         print("1 - 3")
#     else:
#         two += 1
#         one -= 1
#         print("1 - 2")
#
# for i in range(two):
#     # three += 1
#     two -= 1
#     print("2 - 3")
