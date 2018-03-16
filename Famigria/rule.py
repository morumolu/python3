# coding: utf-8

from itertools import combinations


def can_recruit(hand, recruit, reduce_value=0):
    """
    勧誘が可能であるかを調べて返す.
    :param hand: 手札.
    :param recruit: 勧誘対象.
    :param reduce_value: Brutesの効果値.
    :return: True: 勧誘可能, False: 勧誘不可
    """

    # 勧誘対象が新参でなければ不可.
    if not recruit.is_newcomer:
        return False

    # Brutesによる影響を加味した実質的なランクを算出.
    actual_value = recruit.value - reduce_value

    # 0以下であれば勧誘員を用いない勧誘が可能.
    if actual_value <= 0:
        return True

    # 勧誘員で勧誘する.
    if len(hand) < 2:
        return False

    # カードからの2枚ずつ取り出し, 勧誘可能か調べる.
    for recruiters in combinations(hand, 2):
        result = calc_recruiters_value(recruiters)

        if (recruit.family, actual_value) == result:
            return True

    return False


def calc_recruiters_value(recruiters):
    """
    勧誘員の組み合わせから, 勧誘できるカードを調べる.
    :param recruiters: 勧誘員
    :return: (family, value) 勧誘できない場合は('', 0)を返す.
    """
    # ガードコード: 勧誘員は2枚でなければならない.
    if len(recruiters) != 2:
        return '', 0

    # 勧誘員のファミリーが同じ かつ ランクも同じであれば、勧誘できるランクはランク+1.
    if recruiters[0].family == recruiters[1].family:
        if recruiters[0].value == recruiters[1].value:
            return recruiters[0].family, recruiters[0].value + 1

    # 勧誘員の片方が傭兵団で、ワイルドカードとしての条件を満たす場合の処理.
    if recruiters[0].family is 'Mercenaries':
        if recruiters[0].value - 1 >= recruiters[1].value:
            return recruiters[1].family, recruiters[1].value + 1

    elif recruiters[1].family is 'Mercenaries':
        if recruiters[1].value - 1 >= recruiters[0].value:
            return recruiters[0].family, recruiters[0].value + 1

    return '', 0
