# DragDots.py
import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw")
keep_going = True 
radius = 15
mousedown = False

while keep_going: # Game loop
    for event in pygame.event.get(): # Handling events
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, spot, radius)
    pygame.display.update() # update display

pygame.quit() # Exit
