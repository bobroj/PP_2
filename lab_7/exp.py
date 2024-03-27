import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800, 600))

done = False

color = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

x=90
y=90
angle = 0

image = pygame.image.load("mario.png")

def color_change ():

    rr=random.randint(0,255)
    rg=random.randint(0,255)
    rb=random.randint(0,255)
    color = (rr, rg, rb)
    return color

while not done:
   
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    screen.blit(image, (300, 300))
    image_rect = image.get_rect(center = (200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    keys = pygame.key.get_pressed()

    if keys [pygame.K_RIGHT]:
        x+=1
    if keys [pygame.K_LEFT]:
        x-=1
    if keys [pygame.K_UP]:
        y-=1
    if keys [pygame.K_DOWN]:
        y+=1

    if keys[pygame.K_l] and not color_changed:
        color = color_change()
        color_changed = True  
    elif not keys[pygame.K_l]:
        color_changed = False

    if x>740:
        pygame.draw.rect(screen, color, pygame.Rect(0, y, x-740, 60))
    if x==800:
        x=0
    
    if x<0:
        pygame.draw.rect(screen, color, pygame.Rect(800-abs(x), y, abs(x), 60))
    if x==-60:
        x=740

    if y>540:
        pygame.draw.rect(screen, color, pygame.Rect(x, 0, 60, y-540))
    if y==600:
        y=0

    if y<0:
        pygame.draw.rect(screen, color, pygame.Rect(x, 600-abs(y), 60, abs(y)))
    if y==-60:
        y=540
    
    angle+=1
    if angle == 360:
        angle = 0
    
    center = image_rect.center

    rotr=pygame.transform.rotate(image, angle)
    rot_rect = rotr.get_rect(center = center)

    screen.blit(rotr, rot_rect.topleft)

    pygame.display.flip()
    clock.tick(200)
    screen.fill(black)

    

    