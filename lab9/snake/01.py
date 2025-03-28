import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
colorBLACK = (0, 0, 0)
colorGRAY = (100, 100, 100)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)

def draw_grid():
    """Draws the grid on the screen."""
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    """Represents a point on the grid."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    """Handles snake movement, growth, and collisions."""
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.alive = True

    def move(self):
        """Moves the snake, checks for wall and self-collision."""
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
        """Draws the snake on the screen."""
        if not self.alive:
            return
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        """Checks if the snake eats food and grows accordingly."""
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
            return True
        return False

class Food:
    """Handles food spawning, drawing, and disappearing."""
    def __init__(self, snake):
        self.pos = Point(9, 9)
        self.weight = 1  # Default small food
        self.timer = None  # Timer for disappearing big food
        self.generate_random_pos(snake)

    def draw(self):
        """Draws the food on the screen."""
        if self.weight == 1:
            pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        else:
            pygame.draw.rect(screen, (255, 165, 0), (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Orange for big food

    def generate_random_pos(self, snake):
        """Generates a new position and decides food type (small/big)."""
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break

        # 20% chance of spawning a big food (weight 3)
        self.weight = 3 if random.random() < 0.2 else 1
        self.timer = pygame.time.get_ticks() if self.weight == 3 else None  # Start timer for big food

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
        
        # Check food disappearance (only for big food)
        if food.weight == 3 and food.timer:
            if pygame.time.get_ticks() - food.timer > 5000:  # 5 seconds
                food.generate_random_pos(snake)

        if snake.check_collision(food):
            score += food.weight  # Increase score based on food weight
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