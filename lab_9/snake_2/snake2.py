import pygame
import random 
import time
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600

CELL = 30

font = pygame.font.SysFont("Verdana", 36) # создание шрифта

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL))

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

fscore = 0
level = 0
live = 0

togive = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food): 
        global fscore
        global level
        global togive
        global FPS
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.spawn() 
            fscore += 1
            togive = True
        if head.x == dfood.pos.x and head.y == dfood.pos.y:
            print("Got dfood!")
            self.body.append(Point(head.x, head.y))
            dfood.spawn() 
            fscore += 3
            togive = True
        if fscore%3==0 and togive == True:
            level += 1
            FPS += 1
            togive = False


class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    def spawn(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

class Dfood:
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def spawn(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

FPS = 5
clock = pygame.time.Clock()

dfood = Dfood()
food = Food()
snake = Snake()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
    
    live += 1
    print(live)
    if live == 20:
        dfood.spawn()
    if live > 30:
        live = 0

    if snake.body[0].x >= WIDTH / CELL or snake.body[0].x < 0 or snake.body[0].y >= HEIGHT / CELL or snake.body[0].y < 0:
        text_surface = font.render('Поражение :(', True, colorWHITE) # создание текстовой поверхности тру для вкл сглаживания
        text_rect = text_surface.get_rect() #прямоугольник, ограничивающий текст
        text_rect.center = (WIDTH // 2, HEIGHT // 2) # установили центр для текста

        screen.fill(colorRED)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        time.sleep(1)  #чтоб до закрытия игры показывался экран с поражением 
        done = True


    draw_grid_chess()

    # level 
    level_surface = font.render(f"Level: {str(level)}", True, colorRED) # создание текстовой поверхности тру для вкл сглаживания
    level_rect = level_surface.get_rect() #прямоугольник, ограничивающий текст
    level_rect.center = (WIDTH-90, 25) # установили центр для счетчика
    screen.blit(level_surface, level_rect)
    # счетчик
    fscore_surface = font.render(str(fscore), True, colorBLACK) # создание текстовой поверхности тру для вкл сглаживания
    fscore_rect = fscore_surface.get_rect() #прямоугольник, ограничивающий текст
    fscore_rect.center = (25, 25) # установили центр для счетчика
    screen.blit(fscore_surface, fscore_rect)

    snake.move()
    snake.check_collision(food)
    snake.check_collision(dfood)

    snake.draw()
    food.draw()
    dfood.draw()

    pygame.display.flip()
    clock.tick(FPS)


