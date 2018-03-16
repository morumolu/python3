# coding: utf-8

from itertools import combinations


def can_recruit(hand, recruit, reduce_value=0):
    if not recruit.is_newcomer:
        return False

    actual_value = recruit.value - reduce_value
    print('actual_value: {}'.format(actual_value))

    if actual_value <= 0:
        print('You can recruit {}({}) (actual value: {})'.format(
            recruit.family, str(recruit.value), str(actual_value)
        ))
        return True

    for recruiters in combinations(hand, 2):
        result = calc_recruiters_value(recruiters)

        if (recruit.family, actual_value) == result:
            print('Your {}({}) and {}({}) can recruit {}({}) (actual value: {})'.format(
                recruiters[0].family, str(recruiters[0].value),
                recruiters[1].family, str(recruiters[1].value),
                recruit.family, str(recruit.value),
                str(actual_value)
            ))

            return True

    return False


def calc_recruiters_value(recruiters):
    # ガードコード.
    if len(recruiters) != 2:
        return '', 0

    # 勧誘員のファミリーが同じ かつ ランクも同じであれば、勧誘できるランクはランク+1
    if recruiters[0].family == recruiters[1].family:
        if recruiters[0].value == recruiters[1].value:
            return recruiters[0].family, recruiters[0].value + 1

    # 勧誘員の片方が傭兵団
    if recruiters[0].family is 'Mercenaries':
        if recruiters[0].value - 1 >= recruiters[1].value:
            return recruiters[1].family, recruiters[1].value + 1

    elif recruiters[1].family is 'Mercenaries':
        if recruiters[1].value - 1 >= recruiters[0].value:
            return recruiters[0].family, recruiters[0].value + 1

    return '', 0
