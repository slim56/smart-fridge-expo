#Author:Caleb Reed
#Title: Shoot the spider
#Desc: Making a game using pygame that resembles shoot the spider from the first quarter

# Import the pygame module
import pygame

# Import random for random numbers
import random
from random import randint

# Import key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("wizard.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf,(50,50))
        self.rect = self.surf.get_rect()

    # keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        #Creating a bullet
        '''
        if pressed_keys[K_SPACE]:
            bullet = Bullet(p.rect.centerx, p.rect.top)
            self.bullets.add(bullet)
            '''

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("spider.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf,(50,50))
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.rect.midtop = (0, randint(SCREEN_HEIGHT//2, SCREEN_HEIGHT))
        self.speed = random.randint(1, 2)

    # Move the sprite based on speed
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pass
    


# Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create our 'player'
player = Player()

# Create groups to hold enemy sprites, and every sprite
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep our main loop running
running = True

# Our main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == KEYDOWN and event.key == K_SPACE:
            bullet = Bullet(p.rect.centerx, p.rect.top)
            bullebts.add(bullet)
            
        elif event.type == ADDENEMY:
            
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    
    enemies.update()

    
    screen.fill((0, 0, 0))


    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    
    if pygame.sprite.spritecollideany(player, enemies):
        
        player.kill()
        running = False

    # Flip everything to the display
    pygame.display.flip()

