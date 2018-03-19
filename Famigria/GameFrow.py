# coding: utf-8


from random import shuffle

from GameTable import GameTable
from Player import Player
from api import choose_yes_no, choose_number
from gangster import Location, Brutes
from rule import can_recruit


def main_flow():
    # ゲームのセットアップ.
    table, players = set_up()

    # メインルーチン.
    while True:
        for player in players:
            print('PLAYER: {}'.format(player.name))

            # 1. ストリートの補充.
            recruitment_phase(table, player)

            # 2. アカウンタンツ
            accountants_ability_phase(player)

            # 3. ブルーツ
            brutes_ability_phase(player)

            # 4. カードの獲得
            recruit_phase(table, player)

            # 能力のリセット.
            player.disable_brute_ability()


def search_cards_by_serial(cards, serial):
    for card in cards:
        if card.serial == serial:
            return card

    return None


def set_up():
    # テーブルクラス.
    table = GameTable()

    # プレイヤー初期化.
    players = (Player('A'), Player('B'))

    # 山札から初期カードを抜く.
    for serial in (1, 16, 31, 46):
        card = search_cards_by_serial(table.deck, serial)
        table.deck.remove(card)
        card.location = Location.IN_HAND
        players[0].hand.add(card)

    for serial in (2, 17, 32, 47):
        card = search_cards_by_serial(table.deck, serial)
        table.deck.remove(card)
        card.location = Location.IN_HAND
        players[1].hand.add(card)

    # 山札をシャッフルする.
    shuffle(table.deck)

    # 山札から6枚ストリートに並べる
    for serial in range(6):
        card = table.deck.pop()
        card.location = Location.ON_STREET
        table.street.append(card)

    return table, players


def recruitment_phase(table, player):
    while True:
        for index, card in enumerate(table.street):
            print('[{}]: {}'.format(index, card))

        # ストリートにランク0のカードがある場合は引き直しを許可しない.
        for card in table.street:
            if card.value is 0:
                return

        for recruit in table.street:
            if can_recruit(player.hand, recruit):
                print('捨てる？ (y/n)')
                should_discard = choose_yes_no()
                if not should_discard:
                    return

        print('何を捨てる？')

        discard_index = choose_number(choises=[i for i in range(len(table.street))])

        discarded_card = table.street.pop(discard_index)

        draw_num = discarded_card.value

        card.location = Location.DISCARDED
        table.discards.append(card)

        for card in table.street:
            card.is_newcomer = False

        for card in range(draw_num):
            card = table.deck.pop()
            card.location = Location.ON_STREET
            table.street.append(card)


def accountants_ability_phase(player):
    pass


def brutes_ability_phase(player):
    print('{:*^60}'.format('Bruteフェイズ'))

    hand = list(player.hand)
    brutes = list()

    for card in hand:
        if isinstance(card, Brutes) and card.value > 0:
            brutes.append(card)

    if len(brutes) == 0:
        return

    print('Brutesを利用しますか？')
    should_use_brutes = choose_yes_no()

    if not should_use_brutes:
        return

    print('どのBrutesを利用しますか？')
    print('{:-^60}'.format('手札'))
    for index, brute in enumerate(brutes):
        print('[{}]: {}'.format(index, brute))
    print('{:-^60}'.format(''))
    index = choose_number(choises=[i for i in range(len(brutes))])

    brute_ = brutes[index]

    player.hand = player.hand - brute_
    player.enable_brute_ability(brute_.value)

    player.office.add(brute_)

    return


def recruit_phase(table, player):
    hand_list = list(player.hand)

    print('{:*^60}'.format('獲得フェイズ'))

    print('{:-^60}'.format('ストリート'))
    for index, card in enumerate(table.street):
        print('[{}]: {}'.format(index, card))
    print('{:-^60}'.format(''))

    print('{:-^60}'.format('手札'))
    for index, card in enumerate(hand_list):
        print('[{}]: {}'.format(index, card))
    print('{:-^60}'.format(''))

    while True:
        print('どのカードを手札に引き入れる？>>')
        target = choose_number(choises=[i for i in range(len(table.street))])
        recruit = table.street[target]

        if recruit.is_newcomer and recruit.value <= 0:
            player.hand.add(recruit)
            table.street.remove(recruit)
            return

        else:
            while True:
                print('1まいめ？>>')
                index1 = choose_number(choises=[i for i in range(len(hand_list))])

                print('2まいめ？>>')
                index2 = choose_number(choises=[i for i in range(len(hand_list))])

                recruiters = {hand_list[index1], hand_list[index2]}

                if can_recruit(recruiters, recruit):
                    player.hand.add(recruit)
                    table.street.remove(recruit)
                    return
                else:
                    print('この組み合わせでは獲得できません')
                    continue


if __name__ == '__main__':
    main_flow()
