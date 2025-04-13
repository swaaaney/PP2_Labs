import pygame
import random
import psycopg2

WIDTH, HEIGHT = 600, 600
CELL = 30

# Цвета
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234",
    port=5432
)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS snake_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    score INTEGER,
    level INTEGER
)
''')
conn.commit()

def draw_grid(screen):
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, GRAY, (i * CELL, j * CELL, CELL, CELL), 1)

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

    def draw(self, screen):
        if not self.alive:
            return
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
            return True
        return False

class Food:
    def __init__(self, snake):
        self.pos = Point(9, 9)
        self.weight = 1
        self.timer = None
        self.generate_random_pos(snake)

    def draw(self, screen):
        color = GREEN if self.weight == 1 else ORANGE
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break

        self.weight = 3 if random.random() < 0.2 else 1
        self.timer = pygame.time.get_ticks() if self.weight == 3 else None

def run_game(username):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    food = Food(snake)
    clock = pygame.time.Clock()
    FPS = 5
    score = 0
    level = 1

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
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
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        print("Paused.")
                    else:
                        print("Unpaused.")

        if not paused and snake.alive:
            snake.move()

            if food.weight == 3 and food.timer:
                if pygame.time.get_ticks() - food.timer > 5000:
                    food.generate_random_pos(snake)

            if snake.check_collision(food):
                score += food.weight
                food.generate_random_pos(snake)
                if score % 3 == 0:
                    level += 1
                    FPS += 1

        screen.fill(BLACK)
        draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)

        font = pygame.font.SysFont("Verdana", 20)
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

        if not snake.alive:
            game_over_text = font.render("Game Over", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

    # Сохраняем результат
    cur.execute("SELECT * FROM snake_users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        cur.execute("UPDATE snake_users SET score = %s, level = %s WHERE username = %s", (score, level, username))
    else:
        cur.execute("INSERT INTO snake_users (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
    conn.commit()

    pygame.quit()
    return score, level