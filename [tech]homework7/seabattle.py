class Player(object):
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn


class Field(object):
    def __init__(self, size, ships_number):
        self.size = size
        self.ships_number = ships_number


class Ship(object):
    def __init__(self, length, field_place):
        self.length = length
        self.field_place = field_place


class Shoot(object):
    def __init__(self, shooter, coordinate, is_hit):
        self.shooter = shooter
        self.coordinte = coordinate
        self.is_hit = is_hit

