# coding: utf-8


from random import shuffle

from gangster import Accountants, Brutes, Mercenaries, Famiglia, Location
from api import choose_cards

def main_flow():
    # 捨て札.
    discards = list()

    # ストリート.
    street = list()

    # プレイヤーの手札.
    a_hand = set()
    b_hand = set()

    # プレイヤーの事務所.
    a_office = set()
    b_office = set()

    # 山札を初期化.
    deck = generate_cards()

    for card in deck:
        print(card)

    # 山札から初期カードを抜く.

    for serial in (0, 15, 30, 45):
        card = search_cards_by_serial(deck, serial)
        deck.remove(card)
        card.location = Location.IN_HAND
        a_hand.add(card)

    for serial in (1, 16, 31, 46):
        card = search_cards_by_serial(deck, serial)
        deck.remove(card)
        card.location = Location.IN_HAND
        b_hand.add(card)

    # 山札をシャッフルする.
    shuffle(deck)

    # 山札から6枚ストリートに並べる
    for serial in range(6):
        card = deck.pop()
        card.location = Location.ON_STREET
        street.append(card)

    for turn in range(2):

        # 1. ストリートの補充.
        print("ストリート補充")
        print("ストリート")
        for i in street:
            print(i)

        i = choose_cards(1)

        card = street.pop(i)
        card.location = Location.IN_DISCARD
        discards.append(card)

        for serial in range(card.value):
            card = deck.pop()
            card.location = Location.ON_STREET
            street.append(card)

        print("ストリート補充")
        print("ストリート")
        for i in street:
            print(i)


        # 2. アカウンタンツ

        # 3. ブルーツ

        # 4. カードの獲得


    for serial in street:
        print(serial)


def generate_cards():
    families = ('Accountants', 'Brutes', 'Mercenaries', 'Famiglia')
    values = (0, 1, 2, 3, 4)
    amounts = (5, 4, 3, 2, 1)
    value_amounts = dict(zip(values, amounts))

    cards = []

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


def search_cards_by_serial(cards, serial):
    for card in cards:
        if card.serial == serial:
            return card

    return None


if __name__ == '__main__':
    main_flow()
