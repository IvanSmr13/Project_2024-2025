import pygame

# Установка некоторых параметров
WIDTH = 800
HEIGHT = 600
FPS = 30

PLAYER_H_SPEED = 5
PLAYER_V_SPEED = 3


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

    def update(self):
        keys = pygame.key.get_pressed() # метод, который получает состояние всех кнопок клавиатуры
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_H_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_H_SPEED
        if keys[pygame.K_UP] and self.rect.top < HEIGHT:
            self.rect.y += PLAYER_V_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom > 0:
            self.rect.y -= PLAYER_V_SPEED