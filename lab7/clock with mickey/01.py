import pygame
import datetime
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

image_folder = os.path.join(os.getcwd(), "lab7", "clock with mickey")

clock_bg = pygame.image.load(os.path.join(image_folder, "clock.png"))
minute_hand = pygame.image.load(os.path.join(image_folder, "min_hand.png"))
second_hand = pygame.image.load(os.path.join(image_folder, "sec_hand.png"))


minute_hand = pygame.transform.scale(minute_hand, (700, 800))
second_hand = pygame.transform.scale(second_hand, (600, 800))

clock_center = (WIDTH // 2, HEIGHT // 2)


running = True
while running:

    now = datetime.datetime.now()
    second_angle = - (now.second * 6)
    minute_angle = - (now.minute * 6 + now.second * 0.1) 

    second_angle -= 90
    minute_angle -= 90

    screen.blit(clock_bg, (0, 0))

    sec_rotated = pygame.transform.rotate(second_hand, second_angle)
    sec_rect = sec_rotated.get_rect(center=clock_center)
    screen.blit(sec_rotated, sec_rect)

    min_rotated = pygame.transform.rotate(minute_hand, minute_angle)
    min_rect = min_rotated.get_rect(center=clock_center)
    screen.blit(min_rotated, min_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()