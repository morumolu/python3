# coding: utf-8

from gangster import Accountants, Brutes, Mercenaries, Famiglia


def main_flow():
    deck = init_cards()

    for card in deck:
        print(card)


def init_cards():
    gangsters = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}

    cards = []

    for value, number in gangsters.items():
        for i in range(number):
            cards.append(Accountants(value=value))
            cards.append(Brutes(value=value))
            cards.append(Mercenaries(value=value))
            cards.append(Famiglia(value=value))

    return cards


if __name__ == '__main__':
    main_flow()
