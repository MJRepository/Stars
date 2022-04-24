import pygame

pygame.init()

WIDTH, HEIGHT = 1300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK_TICKS = 60
pygame.display.set_caption("Stars Simulation")


def n_step(step) -> int:
    if step > 12:
        step = 0
    else:
        step = step + 1
    return step


def check_step(step, often, func):
    if step % often == 0:
        func()