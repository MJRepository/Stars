import random

import pygame
pygame.init()

WIDTH, HEIGHT = 1300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stars Simulation")

# STAR_COLOR = (0, 123, 132) # COLD_COOLor


class Star:

    x_pos = []
    y_pos = []

    def __init__(self):
        self.x = self.create_position(Star.x_pos, WIDTH)
        self.y = self.create_position(Star.y_pos, HEIGHT)
        self.size = random.randrange(1, 6)
        self.star_type = random.randrange(1, 4)
        self.color = None
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
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

    def update_color(self):
        self.color = (0, (123 - (self.star_type * random.randrange(22, 30))), (132 - (self.star_type * random.randrange(10, 30))))

    def update_position(self):
        self.x = self.x + (self.star_type * self.size)/2
        # self.x = self.x + self.star_type * (4-self.size) #Explosion
        self.y = self.y + self.star_type/2
        # Jeżeli wyjdzie po za ekran
        if self.x > WIDTH:
            self.x = self.x - WIDTH
        if self.y > HEIGHT:
            self.y = self.y - HEIGHT

    @staticmethod
    def show_xy():
        print(Star.x_pos)
        print(Star.y_pos)


def main():
    run = True
    clock = pygame.time.Clock()

    li_test = []
    for i in range(1, 500):
        li_test.append(Star())
    Star.show_xy()

    while run:
        clock.tick(12)

        WIN.fill((0, 0, 0))
        pygame.display.update()

        # Pętla do obsługi zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for star in li_test:
            star.update_color()
            star.update_position()
            star.draw(WIN)  #polar2.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
