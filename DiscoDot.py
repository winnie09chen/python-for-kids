# DiscoDot.py
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])

timer = pygame.time.Clock()
keep_going = True

radius = 50
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    colour = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        )    # RGB color triplet for random colour
    pygame.draw.circle(screen, colour, (100,100), radius)
    pygame.display.update()
    timer.tick(10)

pygame.quit()
