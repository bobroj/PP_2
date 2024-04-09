import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)

color = colorWHITE

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_rad(x1, y1, x2, y2):
    r = pow(pow((max(x1, x2)-min(x1, x2)), 2) + pow((max(y1, y2)-min(y1, y2)), 2), 0.5) 
    print(r)
    return r 

done = False
isrect = False
iscirc = False
iser = False

while not done:

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False

        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
        # conditions for rect
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-50<=event.pos[0]<=WIDTH and event.pos[1]<50:
            isrect = True
            iscirc = False
            iser = False

        if event.type == pygame.MOUSEMOTION and isrect == True:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and isrect == True:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            base_layer.blit(screen, (0, 0))
        
        # FOR CIRCLE
            
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-100<=event.pos[0]<=WIDTH-50 and event.pos[1]<50:
            iscirc = True
            isrect = False
            iser = False

            print("circ")

        if event.type == pygame.MOUSEMOTION and iscirc == True:
            if LMBpressed:
                pygame.draw.circle(screen, color, (prevX, prevY), calculate_rad(prevX, prevY, currX, currY), THICKNESS) 
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and iscirc == True:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.circle(screen, color, (prevX, prevY), calculate_rad(prevX, prevY, currX, currY), THICKNESS)
            base_layer.blit(screen, (0, 0))

        #FOR ERASER:
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-150<=event.pos[0]<=WIDTH-100 and event.pos[1]<50:
            iscirc = False
            isrect = False
            iser = True
            print("eraser")

        if event.type == pygame.MOUSEMOTION and iser == True:
            if LMBpressed:
                pygame.draw.rect(base_layer, colorBLACK, (event.pos[0], event.pos[1], THICKNESS, THICKNESS))

        # THICKNESS
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
        
        # changing colors         
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<=50 and event.pos[1]<=50:
            color = colorBLUE
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 50<=event.pos[0]<=100 and event.pos[1]<=50:
            color = colorRED
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<=50 and 50<=event.pos[1]<=100:
            color = colorYELLOW
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 50<=event.pos[0]<=100 and 50<=event.pos[1]<=100:
            color = colorGREEN

    #surfaces for tools:
    rect_surf = pygame.Surface((50, 50))
    rect_surf.fill(colorWHITE)
    pygame.draw.rect(rect_surf, colorBLACK, (5, 5, 40, 40))
    pygame.draw.rect(rect_surf, colorWHITE, (10, 10, 30, 30))
    screen.blit(rect_surf, (WIDTH-50, 0))

    circ_surf = pygame.Surface((50, 50))
    circ_surf.fill(colorWHITE)
    pygame.draw.circle(circ_surf, colorBLACK, (25, 25), 20)
    pygame.draw.circle(circ_surf, colorWHITE, (25, 25), 16)
    screen.blit(circ_surf, (WIDTH-100, 0))

    eraser = pygame.image.load("eraser.png")
    screen.blit(eraser, (WIDTH-150, 0))

    #color surfaces
    blue_surf = pygame.Surface((50, 50))
    blue_surf.fill(colorBLUE)
    screen.blit (blue_surf, (0, 0))

    red_surf = pygame.Surface((50, 50))
    red_surf.fill(colorRED)
    screen.blit (red_surf, (50, 0))

    yellow_surf = pygame.Surface((50, 50))
    yellow_surf.fill(colorYELLOW)
    screen.blit (yellow_surf, (0, 50))

    green_surf = pygame.Surface((50, 50))
    green_surf.fill(colorGREEN)
    screen.blit (green_surf, (50, 50))

    pygame.display.flip()
    