import random

def print_field(f):
    for i in range(len(f)):
        print(f[i], end=' ')
        if (i+1) % 3 == 0:
            print()


def rand_field(f):
    rf = []
    for i in f:
        if isinstance(i, int):
            rf.append(i)
    return rf


def win(f):
    list_win = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8],
               [0, 3, 6],
               [1, 4, 7],
               [2, 5, 8],
               [0, 4, 8],
               [2, 4, 6]]
    for i in range(len(list_win)):
        x = 0
        o = 0
        for j in range(len(list_win[i])):
            if f[list_win[i][j]] == 'x':
                x += 1
            if f[list_win[i][j]] == 'o':
                o += 1
            if x == 3:
                return True
            if o == 3:
                return False


field = [i for i in range(9)]
# rfield = field
print_field(field)
while True:
    move = input('Введите номер клекти, в которой хотите поставить крестик (х): ')
    if move == 'exit':
        break
    field[int(move)] = 'x'
    rfield = rand_field(field)
    if rfield != []:
        rand = random.choice(rfield)
    field[rand] = 'o'
    if win(field) is True:
        print_field(field)
        print('Поздравляю, Вы выйграли!')
        break
    elif win(field) is False:
        print_field(field)
        print('Сожалею, Вы проиграли!')
        break
    elif rfield == []:
        print_field(field)
        print('Ничья!')
        break
    print_field(field)