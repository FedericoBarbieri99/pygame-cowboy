import pygame


class Bullet:

    def __init__(self, screen, player):
        self.screen = screen

        img = pygame.image.load("assets/bullet.png")
        self.image = img if player.orientation == 'Right' else pygame.transform.flip(img, True, False)
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.right if player.orientation == 'Right' else player.rect.left
        self.rect.centery = player.rect.centery - player.rect.centery/42
        self.vel = 10 if player.orientation == 'Right' else -10

    def update(self):
        self.rect.x += self.vel

    def blit_me(self):
        self.update()
        self.screen.blit(self.image, self.rect)
