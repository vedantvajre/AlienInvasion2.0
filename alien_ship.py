import pygame

from pygame.sprite import Sprite


class Aliens(Sprite):
    def __init__(self, ai_settings, screen):
        super(Aliens, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.rect.get_image()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.alien_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def screen_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
