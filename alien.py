import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.alien_speed_factor

    def update(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right <= screen_rect.right:
            self.x += self.speed_factor
            self.rect.x = self.x
        elif self.rect.right >= screen_rect.right:
            self.x -= self.speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)