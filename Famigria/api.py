# coding: utf-8


def choose_cards(number=1):
    input = wait_for_input()
    return int(input)


def wait_for_input():
    input_string = input()
    return input_string


if __name__ == '__main__':
    print(wait_for_input())
