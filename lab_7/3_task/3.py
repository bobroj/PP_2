import pygame
import time

pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800, 600))

sounds = ["-ot-vinta-bass-bossted.mp3", "amogus.mp3", "kazahstan-ugrojaet-nam-bombordirovkoi.mp3", "muzyika-s-proydennoy-missiey-iz-gta-san-andreas.mp3", "polskaya-korova.mp3"]
x = 0

play = pygame.image.load("play.png")
pause = pygame.image.load("pause.webp")
next = pygame.image.load("next.png")
prev = pygame.image.load("prev.png")

clock = pygame.time.Clock()

done = False

while not done:

    if x > (len(sounds)-1):
        x = 0 
    if x < 0:
        x = 4
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    keys = pygame.key.get_pressed()

    if keys [pygame.K_RIGHT] and not p:
        screen.blit(next, (135, 50))
        x = x+1
        p = True
    elif not keys [pygame.K_RIGHT]:
        p = False

    if keys [pygame.K_LEFT]:
        screen.blit(prev, (135, 50))
        x = x-1
        p = True
    elif not keys [pygame.K_LEFT]:
        p = False

    if keys [pygame.K_UP]:
        screen.blit(play, (135, 50))
        pygame.mixer.music.load(sounds[x])
        pygame.mixer.music.play()

    if keys [pygame.K_DOWN]:
        screen.blit(pause, (135, 50))
        pygame.mixer.music.stop()
        

    pygame.display.flip()
    clock.tick(10)
    screen.fill((250, 222, 224))
