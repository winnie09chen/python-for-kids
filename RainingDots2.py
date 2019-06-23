# RainingDots.py
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
timer = pygame.time.Clock()
colors = [0]*100
locations = [0]*100
sizes = [0]*100

# Store random values in colors, locations, sizes
for n in range(100):
    colors[n] =  (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255),)
    locations[n] = (random.randint(0,800), random.randint(0,600))
    sizes[n] = random.randint(10, 100)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.fill((0,0,0))
    for n in range(100):
        pygame.draw.circle(screen, colors[n], locations[n], sizes[n])
        new_x = locations[n][0]
        new_y = locations[n][1] + 1
        if new_y > 600:
            new_y -= 600
            colors[n] =  (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255),)
            sizes[n] = random.randint(10, 100)
            new_x = random.randint(0, 800)
        locations[n] = (new_x, new_y)
    pygame.display.update() 
    timer.tick(60)
pygame.quit()
