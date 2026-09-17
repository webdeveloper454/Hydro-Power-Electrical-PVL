import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooters")

BLACK = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
clock = pygame.time.Clock()
FPS = 30
font = pygame.font.SysFont("arial", 30)

class player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((60,40))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH //2
        self.rect.bottom = HEIGHT - 30
        self.speed = 6

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if key[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if key[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if key[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed       

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet) 

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(3, 6)           
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 13))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()  
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill() 

class HeartSystem:
    def __init__(self,max_hearts):
        self.max_hearts = max_hearts
        self.hearts = max_hearts
        self.heart_image = pygame.image.load("heart.png").convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (40, 40))

def lose_heart(self):
        self.hearts -= 1
        if self.hearts < 0:
            self.hearts = 0
def add_heart(self):
        if self.hearts < self.max_hearts:
            self.hearts += 1
def is_dead(self):
        return self.hearts <= 0
def draw(self, screen):
        for i in range(self.hearts):
            x = 10 + (i * 45)
            y = 10
            screen.blit(self.heart_image, (x, y))


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = player()
all_sprites.add(player)

for i in range(9):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
score = 0
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
pygame.quit()    