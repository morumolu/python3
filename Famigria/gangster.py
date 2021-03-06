# coding: utf-8

from enum import Enum, auto


class Gangster(object):
    def __init__(self, family, value, victory_points, serial, is_newcomer=True):
        self.family = family
        self.value = value
        self.victory_points = victory_points
        self.serial = serial
        self.location = Location.IN_DECK
        self.is_newcomer = is_newcomer

    def __str__(self):
        info = """No.{} : {}({}) VP: {} ,{}, IS_NEWCOMER: {}""".format(self.serial, self.family, self.value, self.victory_points, self.location, self.is_newcomer)
        return info

    def __repr__(self):
        return repr(self.family)

    def get_victory_points(self):
        return self.victory_points

    def move(self, location):
        self.location = location
        return

    def get_location(self):
        return self.location


class Location(Enum):
    ON_STREET = auto()
    IN_DECK = auto()
    IN_HAND = auto()
    IN_OFFICE = auto()
    DISCARDED = auto()


class Accountants(Gangster):
    def __init__(self, value, serial=0):
        super().__init__('Accountants', value, get_victory_points('Accountants', value), serial)


class Brutes(Gangster):
    def __init__(self, value, serial=0):
        super().__init__('Brutes', value, get_victory_points('Brutes', value), serial)


class Mercenaries(Gangster):
    def __init__(self, value, serial=0):
        super().__init__('Mercenaries', value, get_victory_points('Mercenaries', value), serial)


class Famiglia(Gangster):
    def __init__(self, value, serial=0):
        super().__init__('Famiglia', value, get_victory_points('Famiglia', value), serial)


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
