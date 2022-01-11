import pygame
import random
import os.path
from spritesheet import SpriteSheet


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.seed = random.choice([0, 1])
        img = pygame.image.load(os.path.join("assets", "bandit.png")).convert_alpha()
        walking_sheet = img if self.seed == 0 else pygame.transform.flip(img, True, False)
        self.image = pygame.transform.scale(walking_sheet, (117, 96))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.left - self.rect.width if self.seed == 0 else self.screen_rect.right
        self.rect.bottom = self.screen_rect.bottom
        self.vel = speed if self.seed == 0 else -speed
        self.walking_animation = [SpriteSheet(walking_sheet).get_image(x, 0, 117, 96) for x in range(0, 468, 117)]

    def update(self):
        self.rect.x += self.vel
        self.image = self.walking_animation[(self.rect.x // 30) % len(self.walking_animation)]
