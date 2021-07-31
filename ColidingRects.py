# OPP rect movement and collision with another rect

import pygame, sys, random
from pygame.locals import *


WIDTH, HEIGHT = 360, 480
FPS = 30

# colors

colors = [pygame.Color('black'),
 pygame.Color('white'),
 pygame.Color('red'),
 pygame.Color('green'),
 pygame.Color('blue'),
 pygame.Color('yellow'),
 pygame.Color('orange'),
 pygame.Color('purple'),
]

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rect Collision')
clock = pygame.time.Clock()

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 5
        
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        

player1 = Player(200, 300, 20, 20, colors[3])
player2 = Player(50, 100, 10, 10, colors[4])


        


def terminate():
    pygame.quit()
    sys.exit()
# game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player2.rect.x > player2.vel/2:
        player2.rect.x -= player2.vel
    elif keys[K_RIGHT] and player2.rect.x < WIDTH - player2.width:
        player2.rect.x += player2.vel
    elif keys[K_UP] and player2.rect.y > player2.vel/2:
        player2.rect.y -= player2.vel
    elif keys[K_DOWN] and player2.rect.y < HEIGHT - player2.height:
        player2.rect.y += player2.vel
        


    if player2.rect.colliderect(player1.rect):
        player1.image.fill(colors[5])
    else:
        player1.image.fill(colors[3])

    
    screen.fill(colors[0])
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)
    pygame.display.flip()
    clock.tick(FPS)


    
