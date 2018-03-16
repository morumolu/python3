# coding: utf-8

from gangster import Accountants, Brutes, Mercenaries, Famiglia


# ゲームテーブルクラス.
# 山札, 捨て札, ストリートの要素を持つ.
class GameTable(object):
    def __init__(self):
        self.deck = self.generate_deck()
        self.street = list()
        self.discards = list()

    @staticmethod
    def generate_deck():
        """
        山札の初期化.
        :return:
        """
        families = ('Accountants', 'Brutes', 'Mercenaries', 'Famiglia')
        values = (0, 1, 2, 3, 4)
        amounts = (5, 4, 3, 2, 1)
        value_amounts = dict(zip(values, amounts))

        cards = list()

        serial = 1

        for family in families:
            for value, amounts in value_amounts.items():
                for i in range(amounts):

                    card = None

                    if family is 'Accountants':
                        card = Accountants(value, serial)

                    elif family is 'Brutes':
                        card = Brutes(value, serial)

                    elif family is 'Mercenaries':
                        card = Mercenaries(value, serial)

                    elif family is 'Famiglia':
                        card = Famiglia(value, serial)

                    cards.append(card)
                    serial += 1

        return cards
