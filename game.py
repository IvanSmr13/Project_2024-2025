import pygame
import random

# Установка некоторых параметров
WIDTH = 800
HEIGHT = 600
FPS = 30

PLAYER_H_SPEED = 5
PLAYER_V_SPEED = 3

ENEMY_SPEED = 5


# Установка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Класс "Игрок"
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Замена pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tank.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    
        
        

    def update(self):
        keys = pygame.key.get_pressed() # Метод, который получает состояние всех кнопок клавиатуры
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_H_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_H_SPEED
        if keys[pygame.K_UP] and self.rect.top < HEIGHT:
            self.rect.y += PLAYER_V_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom > 0:
            self.rect.y -= PLAYER_V_SPEED


# Класс "Противник"
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("") не нашел картинку
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), 0))

    def update(self):
        self.rect.y += ENEMY_SPEED
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100, -40)

# Инициализация игры
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World of tanks")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(Player)


# Фон игры
background_image = pygame.image.load('for_game.jpg')
while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)


# Сама игра
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()


    if pygame.sprite.spritecollide(player, enemies, False):
            game_over = True

all_sprites.draw(screen)





          
pygame.quit