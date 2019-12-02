n1, n2 = map(int, input().split(' '))
field = [input() for i in range(n1)]
# field = []
# a = []
# for i in range(n1):
#     a.append(input())
#     for j in range(n2):
#         field.append(a[i][j])
changed_field = field


def print_field(f):
    [print(*f[i]) for i in range(n1)]


for i in range(len(field)):
    for j in range(len(field[i])):
        k = 0
        if field[i][j] == 'X':
            if field[i][j-1] == 'X':
                k += 1
            if field[i][(j+1)%n2] == 'X':
                k += 1
            if field[i-1][(j+1)%n2] == 'X':
                k += 1
            if field[i-1][j] == 'X':
                k += 1
            if field[i-1][j-1] == 'X':
                k += 1
            if field[(i+1)%n1][(j+1)%n2] == 'X':
                k += 1
            if field[(i+1)%n1][j] == 'X':
                k += 1
            if field[(i+1)%n1][j-1] == 'X':
                k += 1
            if k < 2 or k > 3:
                changed_field[i] = changed_field[i][:j] + '.' + field[i][j+1:]
        elif field[i][j] == '.':
            if field[i][j-1] == 'X':
                k += 1
            elif field[i][(j+1)%n2] == 'X':
                k += 1
            elif field[i-1][(j+1)%n2] == 'X':
                k += 1
            elif field[i-1][j] == 'X':
                k += 1
            elif field[i-1][j-1] == 'X':
                k += 1
            elif field[(i+1)%n1][(j+1)%n2] == 'X':
                k += 1
            elif field[(i+1)%n1][j] == 'X':
                k += 1
            elif field[(i+1)%n1][j-1] == 'X':
                k += 1
            if k == 3:
                changed_field[i] = changed_field[i][:j] + 'X' + field[i][j + 1:]
print_field(field)
print('-------------------')
print_field(changed_field)
print(field)
