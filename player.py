import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.right_facing = pygame.image.load("assets/player.png").convert_alpha()
        self.left_facing = pygame.transform.flip(self.right_facing, True, False)
        self.image = self.right_facing
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.orientation = 'Right'
        self.alive = True

    def update(self):
        if self.orientation == "Right":
            self.image = self.right_facing
        elif self.orientation == "Left":
            self.image = self.left_facing

    def die(self):
        for x in range(self.image.get_width()):
            for y in range(self.image.get_height()):
                color = self.image.get_at((x, y))
                color.r = 255
                color.b = 100
                self.image.set_at((x, y), color)
        self.screen.blit(self.image, self.rect)
