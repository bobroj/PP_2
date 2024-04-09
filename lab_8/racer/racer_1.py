import pygame
import random
import sys
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
score = 0
cscore = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))    #создали окно
#список цветов
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorYELLOW = (255, 255, 0)

BACKGROUND = pygame.image.load("AnimatedStreet.png")

clock = pygame.time.Clock()  #выставление задержек

INC_SPEED = pygame.USEREVENT + 1  #создание ивента для увеличения скорости
pygame.time.set_timer(INC_SPEED, 1000)

class Player(pygame.sprite.Sprite):    #класс игровой машинки
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):   #класс вражеской машинки
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

#coin 
class Coin(pygame.sprite.Sprite):   
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("coin_png.png"), (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

SPEED = 5

enemies = pygame.sprite.Group()   #создани спрайт групп, чтоб управлять сразу несколькими спрайтами
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()

P1 = Player()  # присвоение классов
E1 = Enemy()
C1 = Coin()

enemies.add(E1)
coins.add(C1)
all_sprites.add(P1, E1, C1)

done = False

font = pygame.font.SysFont("Verdana", 36) # создание шрифта 

FPS = 60

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if E1.rect[1] + E1.rect[3] >= HEIGHT:
        score += 1
    # счетчик
    score_surface = font.render(str(score), True, colorBLACK) # создание текстовой поверхности тру для вкл сглаживания
    score_rect = score_surface.get_rect() #прямоугольник, ограничивающий текст
    score_rect.center = (25, 25) # установили центр для счетчика
    screen.blit(score_surface, score_rect)
    
    # текстовая поверхность для счетчика монет
    cscore_surface = font.render(str(cscore), True, colorYELLOW) # создание текстовой поверхности тру для вкл сглаживания        
    cscore_rect = cscore_surface.get_rect() #прямоугольник, ограничивающий текст
    cscore_rect.center = (WIDTH-25, 25) # установили центр для счетчика монет
    screen.blit(cscore_surface, cscore_rect)

    # taking coins:
    if pygame.sprite.spritecollideany(P1, coins):

        cscore += 1
        C1.rect.center = (random.randint(50, WIDTH - 50), 35)



    if pygame.sprite.spritecollideany(P1, enemies): # условие на столкновение  
        text_surface = font.render('Поражение :(', True, colorWHITE) # создание текстовой поверхности тру для вкл сглаживания
        text_rect = text_surface.get_rect() #прямоугольник, ограничивающий текст
        text_rect.center = (WIDTH // 2, HEIGHT // 2) # установили центр для текста

        screen.fill(colorRED)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        time.sleep(1)  #чтоб до закрытия игры показывался экран с поражением 
        pygame.quit()
        sys.exit()
       
    pygame.display.flip()
    clock.tick(FPS)