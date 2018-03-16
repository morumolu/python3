# coding: utf-8

# 標準入力のユーティリティ.


def choose_number(choises):
    """
    整数値を選択させる.
    :param choises: 選択肢
    :return: 選択された数値.
    """
    while True:
        input_string = input()

        if not input_string.isdecimal():
            continue

        if int(input_string) in choises:
            return int(input_string)


def choose_yes_no():
    """
    yes, noを選択させる.
    :return: True: yes, False: no
    """
    while True:
        input_string = input()

        if input_string in ('y', 'yes'):
            return True
        elif input_string in ('n', 'no'):
            return False
        else:
            continue
