# encoding: utf-8


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = set()
        self.office = set()
        self.victory_points = 0
        self.brute_value = 0

    def __str__(self):
        # sorted(self.hand, key=attrgetter('family'))

        hand = list()
        for card in self.hand:
            hand.append(card.family + '(' + str(card.value) + ')')
        hand_info = ', '.join(hand)

        office = list()
        for card in self.office:
            office.append(card.family + '(' + str(card.value) + ')')
        office_info = ', '.join(office)

        victory_points = 0
        for card in self.hand | self.office:
            victory_points += card.victory_points

        info = """
        PLAYER: {}
        VICTORY_POINTS: {}
        HAND: {}
        OFFICE: {}
        """.format(self.name, victory_points, hand_info, office_info)
        return info

    def enable_brute_ability(self, brute_value):
        self.brute_value = brute_value

    def disable_brute_ability(self):
        self.brute_value = 0