# DiscoDot.py
import pygame
import random


pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
GREEN = (0,255,0)    # RGB color triplet for GREEN
random.randint(0,255)
BLACK = (0,0,0)
radius = 50
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.circle(screen, GREEN, BLACK, (100,100), radius)
    pygame.display.update()


pygame.quit()
