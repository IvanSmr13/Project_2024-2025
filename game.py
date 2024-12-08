import pygame

# Установка некоторых параметров
WIDTH = 800
HEIGHT = 600
FPS = 30

# Установка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # замена pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.image = pygame.image.load("tank.png")