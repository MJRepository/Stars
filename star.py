import setting as st
import random


def create_position(check_list, size) -> int:
    while True:
        xy = random.randrange(1, size)
        if xy not in check_list:
            return xy


class Star:

    x_pos = []
    y_pos = []

    def __init__(self):
        self.x = create_position(Star.x_pos, st.WIDTH)
        self.y = create_position(Star.y_pos, st.HEIGHT)
        self.size = random.randrange(1, 6)
        self.star_type = random.randrange(1, 4)
        self.color = None
        self.update_color()
        Star.x_pos.append(self.x)
        Star.y_pos.append(self.y)

    def draw(self, win):
        st.pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

    def update_color(self):
        self.color = (0, (123 - (self.star_type * random.randrange(22, 30))), (132 - (self.star_type * random.randrange(10, 30))))

    def update_position(self):
        self.x = self.x + (self.star_type * self.size)/2
        # self.x = self.x + self.star_type * (4-self.size) #Explosion
        self.y = self.y + self.star_type/2
        # Jeżeli wyjdzie po za ekran
        if self.x > st.WIDTH:
            self.x = self.x - st.WIDTH
        if self.y > st.HEIGHT:
            self.y = self.y - st.HEIGHT

    @staticmethod
    def show_xy():
        print(Star.x_pos)
        print(Star.y_pos)


class Comet(Star):

    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)
