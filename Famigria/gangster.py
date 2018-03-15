# coding: utf-8

from enum import Enum, auto


class Gangster(object):
    def __init__(self, family, value, victory_points, image=None):
        self.family = family
        self.value = value
        self.victory_points = victory_points
        self.image = image
        self.location = Location.IN_DECK

    def __str__(self):
        info = """
        FAMILY: {}
        VALUE: {}
        VICTORY_POINTS: {}
        LOVATION: {}
        """.format(self.family, self.value, self.victory_points, self.location)

        return info

    def get_victory_points(self):
        return self.victory_points

    def is_street(self):
        return self.is_street


class Location(Enum):
    ON_STREET = auto()
    IN_DECK = auto()
    IN_HAND = auto()
    IN_OFFICE = auto()


class Accountants(Gangster):
    def __init__(self, value, image=None):
        family = 'Accountants'
        super().__init__(family, value, get_victory_points(family, value), image)

    def play(self):
        pass


class Brutes(Gangster):
    def __init__(self, value, image=None):
        family = 'Brutes'
        super().__init__(family, value, get_victory_points(family, value), image)

    def play(self):
        pass


class Mercenaries(Gangster):
    def __init__(self, value, image=None):
        family = 'Mercenaries'
        super().__init__(family, value, get_victory_points(family, value), image)

    def play(self):
        pass


class Famiglia(Gangster):
    def __init__(self, value, image=None):
        family = 'Famiglia'
        super().__init__(family, value, get_victory_points(family, value), image)

    def play(self):
        pass


def get_victory_points(family, value):
    if family is 'Famiglia':
        if value == 0:
            return 1
        elif value == 1:
            return 3
        elif value == 2:
            return 6
        elif value == 3:
            return 10
        elif value == 4:
            return 15
    else:
        if value == 0:
            return 0
        elif value == 1:
            return 1
        elif value == 2:
            return 3
        elif value == 3:
            return 6
        elif value == 4:
            return 10
        else:
            return None


if __name__ == '__main__':
    mario = Famiglia(1, 1)
    print(mario.value)

    ruigi = Famiglia(1, 1)
    print(ruigi.location)
