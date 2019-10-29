def number(num):
    a1 = ' -- '
    a2 = '|  |'
    a3 = '    '
    a4 = '   |'
    a5 = '|   '

    d = {'0': [a1, a2, a2, a3, a2, a2, a1],
         '1': [a3, a4, a4, a3, a4, a4, a3],
         '2': [a1, a4, a4, a1, a5, a5, a1],
         '3': [a1, a4, a4, a1, a4, a4, a1],
         '4': [a3, a2, a2, a1, a4, a4, a3],
         '5': [a1, a5, a5, a1, a4, a4, a1],
         '6': [a1, a5, a5, a1, a2, a2, a1],
         '7': [a1, a4, a4, a3, a4, a4, a3],
         '8': [a1, a2, a2, a1, a2, a2, a1],
         '9': [a1, a2, a2, a1, a4, a4, a1]}
    return d[num]


a = input()
matrix = []
for i in range(len(a)):
    matrix.append(number(a[i]))

for x in range(len(matrix)):
    print("X" + "-----"*len(a)+"X")
    for y in range(len(matrix[x])):
        print("|", end="")
        for k in range(len(a)):
            print(matrix[x+k][y], end=" ")
        print("|", end="")
        print()
    print("X" + "-----" * len(a) + "X")
    break
