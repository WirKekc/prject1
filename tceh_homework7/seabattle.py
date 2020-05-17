SIZE_FIELD = 10
create_field = [['.' for i in range(SIZE_FIELD)] for j in range(SIZE_FIELD)]

class Player(object):
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn


class Field(object):
    def __init__(self, ships_number):
        # self.size = size
        self.ships_number = ships_number
        # marix = [['.' for i in range(self.size)] for j in range(self.size)]
        # print(marix)

    def print_field(self, field):
        [print(*field[i]) for i in range(SIZE_FIELD)]


class Ship(object):

    def one_deck(self, change_field, x, y):
        if x < 0 or x > 9 or y < 0 or y > 9:
            print('Координата X или Y неверна, введите их заного!')
            ship.one_deck(change_field, int(input('Введите х координату однопалубного корабля: ')),
                          int(input('Введите у координату однопалубного корабля: ')))
            return change_field

        for i in range(x-1, x+2):
            if i < 0 or i > 9:
                continue
            for j in range(y-1, y+2):
                if j < 0 or j > 9:
                    continue
                if change_field[i][j] == '1':
                    print('Сюда нельзя поставить корабль, выберите другое место!')
                    ship.one_deck(change_field, int(input('Введите х координату однопалубного корабля: ')),
                                  int(input('Введите у координату однопалубного корабля: ')))
                    return change_field

        change_field[x][y] = '1'
        Storage.player1_field(storage, change_field)
        return change_field


class Shoot(object):
    def __init__(self, shooter, coordinate, is_hit):
        self.shooter = shooter
        self.coordinate = coordinate
        self.is_hit = is_hit


class Storage(object):
    def player1_field(self, p_field):
        return p_field


storage = Storage()
field = Field(20)
field.print_field(create_field)
player1 = Player(input('Введите имя первого игорока: '), 1)
player2 = Player(input('Введите имя второго игорока: '), 2)
ship = Ship()
print('Создание кораблей игрока {}!'.format(player1.name))
print('Создание однопалубных кораблей!')
for i in range(4):
    print('Корабль {}'.format(i+1))
    field.print_field(ship.one_deck(create_field, int(input('Введите х координату однопалубного корабля: ')), int(input('Введите у координату однопалубного корабля: '))))


