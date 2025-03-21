import pygame
import random
import time
import os

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Game")

def load_image(name, size=None):
    path = os.path.join(os.getcwd(), "lab8", "racer", name)
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size) if size else image

background = load_image("AnimatedStreet.png")
player_img = load_image("Player.png")
enemy_img = load_image("Enemy.png")
coin_img = load_image("coin.png", (30, 30)) 

pygame.mixer.music.load(os.path.join(os.getcwd(), "lab8", "racer", "background.wav"))
pygame.mixer.music.play(-1)  
crash_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "lab8", "racer","crash.wav"))

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

FPS = 60
clock = pygame.time.Clock()
PLAYER_SPEED = 5
ENEMY_SPEED = 5
COIN_SPEED = 4
score = 0  

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(PLAYER_SPEED, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -random.randint(50, 150)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = -random.randint(50, 150)

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) 

    player.move()
    enemy.move()
    coin.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        pygame.time.delay(int(crash_sound.get_length() * 1000))
        screen.fill("red")
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        time.sleep(2)
        running = False

    if pygame.sprite.spritecollide(player, coin_sprites, True):
        score += 1
        new_coin = Coin()
        all_sprites.add(new_coin)
        coin_sprites.add(new_coin)


    score_text = font_small.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (WIDTH - 100, 10))

    pygame.display.flip() 
    clock.tick(FPS)  

pygame.quit()