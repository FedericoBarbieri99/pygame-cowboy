# import pygame
import sys
from player import *
from bullet import *

pygame.init()

background = pygame.image.load("assets/background.png")
screen_size = background.get_rect().size
screen = pygame.display.set_mode(screen_size, vsync=1)
background = background.convert()
player = Player(screen)
bullets = []
clock = pygame.time.Clock()


def update_screen():

    screen.blit(background, [0, 0])
    player.blit_me()
    for bullet in bullets:
        bullet.blit_me()
        if bullet.rect.x not in range(screen_size[0]):
            bullets.pop(bullets.index(bullet))

    pygame.display.flip()


def event_handler():
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.orientation = 'Left'
            if event.key == pygame.K_RIGHT:
                player.orientation = 'Right'
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(screen, player))

        if event.type == pygame.QUIT:
            sys.exit()


while True:
    clock.tick(60)
    event_handler()
    update_screen()

