import pygame
import random


class Enemy:

    def __init__(self, screen):
        self.screen = screen
        self.seed = random.choice([0, 1])
        img = pygame.image.load("assets/bandit.png")
        self.image = img if self.seed == 0 else pygame.transform.flip(img, True, False)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.left if self.seed == 0 else self.screen_rect.right
        self.rect.bottom = self.screen_rect.bottom
        self.vel = 10 if self.seed == 0 else -10

    def update(self):
        self.rect.x += self.vel

    def blit_me(self):
        self.update()
        self.screen.blit(self.image, self.rect)