fraction = input().split('/')


def scf(a, b):
    print(a // b, end=" ")
    ost = a % b
    if ost > 0:
        scf(b, ost)


scf(int(fraction[0]), int(fraction[1]))