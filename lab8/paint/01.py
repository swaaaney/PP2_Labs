import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Variables
LMBpressed = False
RMBpressed = False
MMBpressed = False
THICKNESS = 5
currX, currY, prevX, prevY = 0, 0, 0, 0
color = RED  # Default color

done = False
screen.fill(WHITE)  # Fill background with white

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left button (line)
                LMBpressed = True
                prevX, prevY = event.pos
            elif event.button == 3:  # Right button (rectangle)
                RMBpressed = True
                prevX, prevY = event.pos
            elif event.button == 2:  # Middle button (circle)
                MMBpressed = True
                prevX, prevY = event.pos
        
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                pygame.draw.line(screen, color, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                LMBpressed = False
            elif event.button == 3:
                RMBpressed = False
                currX, currY = event.pos
                width, height = currX - prevX, currY - prevY
                pygame.draw.rect(screen, color, (prevX, prevY, width, height), THICKNESS)
            elif event.button == 2:
                MMBpressed = False
                currX, currY = event.pos
                radius = ((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5
                pygame.draw.circle(screen, color, (prevX, prevY), int(radius), THICKNESS)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            if event.key == pygame.K_e:
                color = WHITE  # Eraser
            if event.key == pygame.K_1:
                color = RED
            if event.key == pygame.K_2:
                color = BLUE
            if event.key == pygame.K_3:
                color = BLACK
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()