import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800, 600))

done = False

color = (25, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

x=90
y=90

def color_change ():

    rr=random.randint(0,255)
    rg=random.randint(0,255)
    rb=random.randint(0,255)
    color = (rr, rg, rb)
    return color

while not done:
   
    pygame.draw.circle(screen, color, (x, y), 25)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    keys = pygame.key.get_pressed()

    if keys [pygame.K_RIGHT]:
        x+=20
    if keys [pygame.K_LEFT]:
        x-=20
    if keys [pygame.K_UP]:
        y-=20
    if keys [pygame.K_DOWN]:
        y+=20

    if keys[pygame.K_l] and not color_changed:
        color = color_change()
        color_changed = True  
    elif not keys[pygame.K_l]:
        color_changed = False

    if x>775:
        x = 775
    
    if x<25:
        x = 25

    if y>575:
        y = 575

    if y<25:
        y=25
    
    pygame.display.flip()
    clock.tick(20)
    screen.fill((255, 255, 255))