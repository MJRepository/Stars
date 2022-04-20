import random

import pygame
pygame.init()

WIDTH, HEIGHT = 1300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stars Simulation")

# STAR_COLOR = (0, 123, 132) # COLD


class Star:

    x_pos = []
    y_pos = []

    def __init__(self):
        self.x = self.create_position(Star.x_pos, WIDTH)
        self.y = self.create_position(Star.y_pos, HEIGHT)
        self.size = random.randrange(1, 6)
        self.star_type = random.randrange(1, 4)
        Star.x_pos.append(self.x)
        Star.y_pos.append(self.y)

    def create_position(self, check_list, size) -> int:
        check = True    # Flaga do sprawdzania kodu
        # !?Lambda
        while check:
            xy = random.randrange(1, size)
            if xy not in check_list:
                check = False
        return xy

    def draw(self, win):
        STAR_COLOR = (0, (123 - (self.star_type * random.randrange(22, 30))), (132 - (self.star_type * random.randrange(10, 30))))
        pygame.draw.circle(win, STAR_COLOR, (self.x, self.y), self.size)

    @staticmethod
    def show_xy():
        print(Star.x_pos)
        print(Star.y_pos)


def main():
    run = True
    clock = pygame.time.Clock()

    # WIN.fill((0, 0, 0))
    li_test = []
    for i in range(1, 500):
        li_test.append(Star())
    Star.show_xy()

    while run:
        clock.tick(10)
        WIN.fill((0, 0, 0))
        pygame.display.update()

        # Pętla do obsługi zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for star in li_test:
            star.draw(WIN)

        #polar2.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
