import pygame
from color_palette import *
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.alive = True

    def move(self):
        if not self.alive:
            return
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL:
            self.alive = False

        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                self.alive = False

    def draw(self):
        if not self.alive:
            return
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            return True
        return False

class Food:
    def __init__(self, snake):
        self.pos = Point(9, 9)
        self.generate_random_pos(snake)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break

FPS = 5
clock = pygame.time.Clock()
snake = Snake()
food = Food(snake)
score = 0
level = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1
    
    if snake.alive:
        snake.move()
        if snake.check_collision(food):
            score += 1
            food.generate_random_pos(snake)
            if score % 3 == 0:
                level += 1
                FPS += 1
    
    screen.fill(colorBLACK)
    draw_grid()
    snake.draw()
    food.draw()

    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    if not snake.alive:
        game_over_text = font.render("Game Over", True, colorRED)
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
