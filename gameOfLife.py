n1, n2 = map(int, input().split(' '))
field = [input() for i in range(n1)]
changed_field = field.copy()


def print_field(f):
    [print(f[i]) for i in range(n1)]


def scope(f, el):
    k = 0
    if f[i][j] == el:
        if f[i][j - 1] == 'X':
            k += 1
        if f[i][(j + 1) % n2] == 'X':
            k += 1
        if f[i - 1][(j + 1) % n2] == 'X':
            k += 1
        if f[i - 1][j] == 'X':
            k += 1
        if f[i - 1][j - 1] == 'X':
            k += 1
        if f[(i + 1) % n1][(j + 1) % n2] == 'X':
            k += 1
        if f[(i + 1) % n1][j] == 'X':
            k += 1
        if f[(i + 1) % n1][j - 1] == 'X':
            k += 1
    return k


for i in range(len(field)):
    for j in range(len(field[i])):
        if scope(field, 'X') < 2 or scope(field, 'X') > 3:
            changed_field[i] = changed_field[i][:j] + '.' + field[i][j + 1:]
        if scope(field, '.') == 3:
            changed_field[i] = changed_field[i][:j] + 'X' + field[i][j + 1:]

print_field(changed_field)


# Пример другого решения
# Преобразуем вход в единицы и нули, чтобы соседей можно было посчитать относительно простым вызовом суммы.
# Так как сумма по диапазонам загребает в том числе и текущую клетку, её значение отнимаем.

# neighrange = (-1, 0, 1)
# n, m = (int(x) for x in input().split())
# a = [[int(c == 'X') for c in input()] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         x = a[i][j]
# Сумма из диапозона от -1 до 1 идет по квадрату вокруг выбираемого элемента и отнимается сам элемент.
# Матрица предварительно преобразована в 0 и 1
#         neighbors = sum(a[(i+di) % n][(j+dj) % m] for di in neighrange for dj in neighrange) - x
#         if x and neighbors == 2 or neighbors == 3:
#             print('X', end='')
#         else:
#             print('.', end='')
#     print()