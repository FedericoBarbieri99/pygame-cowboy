import pygame


class SpriteSheet(object):
    def __init__(self, loaded_sheet):
        self.sprite_sheet = loaded_sheet.convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
