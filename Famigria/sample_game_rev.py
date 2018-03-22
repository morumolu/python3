# coding:utf-8

from enum import IntEnum, auto
from typing import Tuple, List


class Grid(IntEnum):
    WALL = auto()
    SPACE = auto()
    BALL = auto()
    GOAL = auto()
    MAN = auto()


def main() -> None:
    raw_map = """\
#############
#           #
#        .  #
#     P     #
#       O   #
####    O   #
#           #
#   O ###   #
#     #.#   #
#     #     #
#     #     #
#############\
"""

    stage = text2stage(raw_map)
    draw(stage)

    while True:
        direction = get_input()
        stage = update_game(stage, direction)
        draw(stage)


def get_input() -> Tuple[int, int]:
    directions = {'w': (0, -1), 's': (0, +1), 'a': (-1, 0), 'd': (+1, 0)}

    while True:
        input_char = input()

        if input_char not in directions.keys():
            print("illegal input")
            continue

        return directions[input_char]


def update_game(stage: List[List[Grid]], direction: Tuple[int, int]) -> List[List[Grid]]:
    dist_0 = search_obj(stage, Grid.MAN)
    dist_1 = dist_0[0] + direction[0], dist_0[1] + direction[1]
    dist_2 = dist_0[0] + 2 * direction[0], dist_0[1] + 2 * direction[1]

    dist_grid_1 = stage[dist_1[1]][dist_1[0]]
    dist_grid_2 = stage[dist_2[1]][dist_2[0]]

    if dist_grid_1 == Grid.WALL:
        return stage

    elif dist_grid_1 == Grid.BALL:
        if dist_grid_2 == Grid.WALL:
            return stage

        elif dist_grid_2 == Grid.BALL:
            return stage

        else:
            stage[dist_0[1]][dist_0[0]] = Grid.SPACE
            stage[dist_1[1]][dist_1[0]] = Grid.MAN
            stage[dist_2[1]][dist_2[0]] = Grid.BALL

            if dist_grid_2 == Grid.GOAL:
                print('CLEAR!')

            return stage

    else:
        stage[dist_0[1]][dist_0[0]] = Grid.SPACE
        stage[dist_1[1]][dist_1[0]] = Grid.MAN
        return stage


def draw(stage: List[List[Grid]]) -> None:
    print(stage2text(stage))
    return


def text2stage(text: str) -> List[List[Grid]]:
    grid_text = {'#': Grid.WALL, ' ': Grid.SPACE, 'O': Grid.BALL, '.': Grid.GOAL, 'P': Grid.MAN}

    stage = []
    for line in text.split('\n'):
        row = []
        for c in line:
            row.append(grid_text[c])
        stage.append(row)

    return stage


def stage2text(stage: List[List[Grid]]) -> str:
    text_grid = {Grid.WALL: '#', Grid.SPACE: ' ', Grid.BALL: 'O', Grid.GOAL: '.', Grid.MAN: 'P'}

    text = ''
    for line in stage:
        for grid in line:
            text += text_grid[grid]
        text += '\n'

    return text


def search_obj(stage: List[List[Grid]], grid_obj: Grid) -> Tuple[int, int]:
    for y, line in enumerate(stage):
        for x, c in enumerate(line):
            if c == grid_obj:
                return x, y


if __name__ == '__main__':
    main()
