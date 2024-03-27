import pygame
import datetime 

pygame.init()
screen = pygame.display.set_mode((1400, 1050))

fon = pygame.image.load("mainclock.png")
larm = pygame.image.load("leftarm.png")
rarm = pygame.image.load ("rightarm.png")

okno = fon.get_rect(center = (700, 525))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    date = datetime.datetime.now()

    hour = date.hour
    min = date.minute 
    sec = date.second
    
    min_angle = -(6*(min+9))
    sec_angle = -6*sec

    minrot = pygame.transform.rotate(rarm, min_angle)
    minrect = minrot.get_rect()
    minrect.center = okno.center

    secrot = pygame.transform.rotate(larm, sec_angle)
    secrect = secrot.get_rect()
    secrect.center = okno.center

    screen.blit (fon, okno)
    screen.blit (minrot, minrect)
    screen.blit (secrot, secrect)

    pygame.display.flip() 

