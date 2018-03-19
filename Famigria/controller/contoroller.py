import pygame


class Display(object):
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height


class Area(object):
    def __init__(self, screen, name, x, y, w, h):
        self.screen = screen
        self.name = name

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.color = (0, 128, 255)

    def draw(self):
        self.area = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.color, self.area)

    def selected(self, screen):
        print(self.name)


class HandArea(object):
    def __init__(self, cards, side):
        self.cards = cards

        if side == 1:
            self.y = 100
        elif side == 2:
            self.y = 500

    def draw(self):
        for index, card in enumerate(self.cards):
            card.y = self.y
            card.x = index * 64
            card.draw()


class OfficeArea(object):
    def __init__(self, cards, side):
        self.cards = cards
        if side == 1:
            self.y = 0
        elif side == 2:
            self.y = 600

    def draw(self):
        for index, card in enumerate(self.cards):
            card.y = self.y
            card.x = index * 64
            card.draw()


class StreetArea(object):
    def __init__(self, cards):
        self.cards = cards
        self.x = 200
        self.y = 300

    def add(self, card):
        self.cards += card

    def draw(self):
        for index, card in enumerate(self.cards):
            card.y = self.y
            card.x = self.x + index * 64
            card.draw()


class CardArea(Area):
    def selected(self, screen):
        print(self.name)


class DeckArea(Area):
    def selected(self, screen):
        print("deck")


class DiscardArea(Area):
    def selected(self, screen):
        print("discard")


def click(x, y, items):
    for item in items:
        if (item.x < x < item.x + item.w) and (item.y < y < item.y + item.h):
            return item
    return None


def main():
    pygame.init()

    disp = Display(800, 640)
    screen = pygame.display.set_mode((disp.WIDTH, disp.HEIGHT))
    pygame.display.set_caption('Famiglia')

    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()

    is_done = False

    while not is_done:

        deck_area.draw()
        discard_area.draw()
        street_area.draw()
        a_hand_area.draw()
        a_office_area.draw()
        b_hand_area.draw()
        b_office_area.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_done = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                clicked_obj = click(x, y, items)

                if clicked_obj is not None:
                    clicked_obj.selected(screen)

        pygame.display.flip()
        clock.tick(60)


def clicked(x, y):
    pass


if __name__ == '__main__':
    main()
