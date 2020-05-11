x = input().split()
koz = input()


def less(l, r):
    o =['1', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return o.index(l) < o.index(r)


if x[0][-1] == x[1][-1]:
    if less(x[0][:-1], x[1][:-1]) is False:
        print("First")
    else:
        print("Second")
elif koz == x[0][-1]:
    print("First")
elif koz == x[1][-1]:
    print("Second")
else:
    print("Error")


# Интересная реализация с tuple
# (c1, c2), m = input().replace('10', 'T', 2).split(), input()
# r1 = (c1[1] == m, '6789TJQKA'.find(c1[0]) * (c1[1] == c2[1]))
# r2 = (c2[1] == m, '6789TJQKA'.find(c2[0]) * (c1[1] == c2[1]))
# ans = 0 if r1 > r2 else 1 if r1 < r2 else 2
# print(['First', 'Second', 'Error'][ans])
