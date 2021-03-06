import pygame
import os.path
from utils import resource_path


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        img = pygame.image.load(resource_path(os.path.join("assets", "bullet.png"))).convert_alpha()
        self.image = img if player.orientation == 'Right' else pygame.transform.flip(img, True, False)
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.right if player.orientation == 'Right' else player.rect.left
        self.rect.centery = player.rect.centery - player.rect.centery/42
        self.vel = 10 if player.orientation == 'Right' else -10

    def update(self):
        self.rect.x += self.vel
