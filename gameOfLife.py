n1, n2 = map(int, input().split(' '))
field = [input() for i in range(n1)]

# field = [['.' for i in range(n1)] for j in range(n2)]


def print_field():
    [print(*field[i]) for i in range(n1)]
k = 0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == 'X':
            if field[i][j-1] == 'X':
                k+=1
            elif field[i][(j+1)%n2] == 'X':
                k+=1
            elif field[i-1][(j+1)%n2] == 'X':
                k+=1
            elif field[i-1][j] == 'X':
                k+=1
            elif field[i-1][j-1] == 'X':
                k+=1
            elif field[(i+1)%n1][(j+1)%n2] == 'X':
                k+=1
            elif field[(i+1)%n1][j] == 'X':
                k+=1
            elif field[(i+1)%n1][j-1] == 'X':
                k+=1
        if
print_field()
print(field)
