import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Shapes")

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Variables
LMBpressed = False
RMBpressed = False
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
            if event.button == 1:  # Left button for lines and triangles
                LMBpressed = True
                prevX, prevY = event.pos
            elif event.button == 3:  # Right button for rectangles, squares, and rhombuses
                RMBpressed = True
                prevX, prevY = event.pos
        
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX, currY = event.pos
                pygame.draw.line(screen, color, (prevX, prevY), (currX, currY), THICKNESS)
                prevX, prevY = currX, currY
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                LMBpressed = False
                currX, currY = event.pos
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LSHIFT]:  # Right triangle
                    pygame.draw.polygon(screen, color, [(prevX, prevY), (currX, prevY), (prevX, currY)], THICKNESS)
                elif keys[pygame.K_LCTRL]:  # Equilateral triangle
                    side = abs(currX - prevX)
                    height = math.sqrt(3) / 2 * side
                    pygame.draw.polygon(screen, color, [(prevX, prevY), (prevX + side, prevY), (prevX + side // 2, prevY - height)], THICKNESS)
            
            elif event.button == 3:
                RMBpressed = False
                currX, currY = event.pos
                width, height = currX - prevX, currY - prevY
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LSHIFT]:  # Square
                    side = min(abs(width), abs(height))
                    pygame.draw.rect(screen, color, (prevX, prevY, side, side), THICKNESS)
                elif keys[pygame.K_LCTRL]:  # Rhombus
                    d1, d2 = abs(width), abs(height)
                    pygame.draw.polygon(screen, color, [(prevX, prevY - d2 // 2), (prevX + d1 // 2, prevY), (prevX, prevY + d2 // 2), (prevX - d1 // 2, prevY)], THICKNESS)
                else:  # Rectangle
                    pygame.draw.rect(screen, color, (prevX, prevY, width, height), THICKNESS)
        
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
