import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

MUSIC_FOLDER = os.path.dirname(os.path.abspath(__file__))

playlist = [file for file in os.listdir(MUSIC_FOLDER) if file.endswith(".mp3")]

if not playlist:
    raise Exception("В папке с кодом нет MP3-файлов!")

current_track = 0

def load_track(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[index]))
    pygame.mixer.music.play()

load_track(current_track)

running = True
paused = False

while running:
    screen.fill(WHITE)

    track_name = font.render(f"Playing: {playlist[current_track]}", True, BLACK)
    screen.blit(track_name, (20, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()

            if event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                load_track(current_track)

            if event.key == pygame.K_LEFT: 
                current_track = (current_track - 1) % len(playlist)
                load_track(current_track)

    pygame.display.flip()


pygame.quit()