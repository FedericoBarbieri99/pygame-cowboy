import pygame


class Player:

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.orientation = 'Right'

    def blit_me(self):
        if self.orientation == "Right":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Left":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
