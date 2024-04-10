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

def calc_square(x1, y1, x2, y2):
    width_square = abs(x2 - x1)
    height_square = abs(y2 - y1)
    side_length = min(width_square, height_square)
    x2 = x1 + side_length * (1 if x2 > x1 else -1)
    y2 = y1 + side_length * (1 if y2 > y1 else -1)
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

def calc_rtri(x1, y1, x2, y2):
    x3 = x1
    y3 = y2
    return [(x1, y1), (x2, y2), (x3, y3)]

def calc_eqtri(x1, y1, x2, y2):
    x3 = x1 - (x2 - x1)
    y3 = y2
    return [(x1, y1), (x2, y2), (x3, y3)]

def calc_rh(x1, x2, y1, y2):
    height = abs(y2 - y1)
    if y2 > y1:
        if x2 > x1:
            return [(x1, (y1 + height / 2)), ((x1 + (abs(x2-x1) / 2)), y2), (x2, (y1 + height / 2)), ((x1 + (abs(x2-x1) / 2)), y1)]
        else:
            return [(x1, (y1 + height / 2)), ((x2 + (abs(x2-x1) / 2)), y2), (x2, (y1 + height / 2)), ((x2 + (abs(x2-x1) / 2)), y1)]
    
    else:
        if x2 > x1:
            return [(x1, (y2 + height / 2)), ((x1 + (abs(x2-x1) / 2)), y2), (x2, (y2 + height / 2)), ((x1 + (abs(x2-x1) / 2)), y1)]
        else:
            return [(x1, (y2 + height / 2)), ((x2 + (abs(x2-x1) / 2)), y2), (x2, (y2 + height / 2)), ((x2 + (abs(x2-x1) / 2)), y1)]

done = False
isrect = False
iscirc = False
iser = False
issq = False
isrtri = False
iseqtri = False
isrb = False

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
            issq = False
            isrtri = False
            iseqtri = False
            isrb = False

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
            issq = False
            isrtri = False
            isrb = False
            iseqtri = False

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
            issq = False
            isrtri = False
            iseqtri = False
            isrb = False
            print("eraser")

        if event.type == pygame.MOUSEMOTION and iser == True:
            if LMBpressed:
                pygame.draw.rect(base_layer, colorBLACK, (event.pos[0], event.pos[1], THICKNESS, THICKNESS))
        # SQUARE
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-150<=event.pos[0]<=WIDTH-100 and 50<event.pos[1]<100:
            isrect = False
            iscirc = False
            iser = False
            issq = True
            isrtri = False
            isrb = False
            iseqtri = False

        if event.type == pygame.MOUSEMOTION and issq == True:
            if LMBpressed:
                pygame.draw.polygon(screen, color, calc_square(prevX, prevY, currX, currY), 5)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and issq == True:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.polygon(screen, color, calc_square(prevX, prevY, currX, currY), 5)
            base_layer.blit(screen, (0, 0))

        # RIGHT TRIANGLE
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-100<=event.pos[0]<=WIDTH-50 and 50<event.pos[1]<100:
            isrect = False
            iscirc = False
            iser = False
            issq = False
            isrb = False
            isrtri = True
            iseqtri = False

        if event.type == pygame.MOUSEMOTION and isrtri == True:
            if LMBpressed:
                pygame.draw.polygon(screen, color, calc_rtri(prevX, prevY, currX, currY), 5)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and isrtri == True:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.polygon(screen, color, calc_rtri(prevX, prevY, currX, currY), 5)
            base_layer.blit(screen, (0, 0))   
        
        # EQUILATERAL TRIANGLE
            
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-50<=event.pos[0] and 50<event.pos[1]<100:
            isrect = False
            iscirc = False
            iser = False
            isrb = False
            issq = False
            isrtri = False
            iseqtri = True

        if event.type == pygame.MOUSEMOTION and iseqtri == True:
            if LMBpressed:
                pygame.draw.polygon(screen, color, calc_eqtri(prevX, prevY, currX, currY), 5)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and iseqtri == True:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.polygon(screen, color, calc_eqtri(prevX, prevY, currX, currY), 5)
            base_layer.blit(screen, (0, 0))

        # RHOMBUS
            
        if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-200<=event.pos[0]<=WIDTH-150 and event.pos[1]<50:
            isrect = False
            iscirc = False
            iser = False
            isrb = True
            issq = False
            isrtri = False
            iseqtri = False

        if event.type == pygame.MOUSEMOTION and isrb == True:
            if LMBpressed:
                pygame.draw.polygon(screen, color, calc_rh(prevX, currX, prevY, currY), 5)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and isrb == True:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.polygon(screen, color, calc_rh(prevX, currX, prevY, currY), 5)
            base_layer.blit(screen, (0, 0))

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
    rect = pygame.image.load("rect.png")
    screen.blit(rect_surf, (WIDTH-50, 0))
    screen.blit(rect, (WIDTH-50, 0))

    circ_surf = pygame.Surface((50, 50))
    circ_surf.fill(colorWHITE)
    pygame.draw.circle(circ_surf, colorBLACK, (25, 25), 20)
    pygame.draw.circle(circ_surf, colorWHITE, (25, 25), 16)
    screen.blit(circ_surf, (WIDTH-100, 0))

    eraser = pygame.image.load("eraser.png")
    screen.blit(eraser, (WIDTH-150, 0))

    square = pygame.image.load("square.png")
    screen.blit(square, (WIDTH-150, 50))

    rtri = pygame.image.load("rtri.jpg")
    screen.blit(rtri, (WIDTH-100, 50))

    eqtri = pygame.image.load("eqtri.png")
    screen.blit(eqtri, (WIDTH-50, 50))

    rb = pygame.image.load("rb.jpg")
    screen.blit(rb, (WIDTH-200, 0))

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
    