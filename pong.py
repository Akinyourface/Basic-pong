import pygame
from pygame.locals import *
import os
from random import randint
D_WMIN = 0
D_HMIN = 0
D_WMAX = 640
D_HMAX = 480

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 64, height = 10):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.deltax = 0
        self.deltay = 0

    def update(self):




        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 640:
            self.rect.right = 640
        self.rect.x += self.deltax
        self.rect.y += self.deltay

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 5, height = 5):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.streak = 0
        self.dir = 1 # 1 = leftdown, 2 = rightdown, 3 = leftup, 4 = rightup
    def update(self):
        hit_list = pygame.sprite.spritecollide(self, self.player, False)

        for col in hit_list:
            self.streak += 1
            if self.speed <= 10:
                self.speed += 1
            else:
                self.speed = 2
            if self.dir == 3:
                print("coll")
                self.dir = 2
            if self.dir == 4:
                print("coll")
                self.dir = 1
        
        if self.rect.x < 0 and self.dir == 1:
            self.dir = 2
            print("first")
        if self.rect.y > 480 and self.dir == 2:
            self.dir = 3
            print("second")
            
        if self.rect.x > 640 and self.dir == 3:
            self.dir = 4
            print("third")
        if self.rect.y < 0 and self.dir == 4:
            self.dir = 1
            self.reset()
            self.streak = 0
            self.speed = 2
            pygame.time.delay(3000)
            print("fourth")
            
        if self.rect.x < 0 and self.dir == 4:
            self.dir = 3
            print("fifth")
        if self.rect.y > 485 and self.dir == 3:
            self.dir = 4
            print("sixth")
            
        if self.rect.x > 640 and self.dir == 2:
            self.dir = 1
            print("seventh")
        if self.rect.y < 0 and self.dir == 3:
            self.dir = 2
            self.streak = 0
            self.reset()
            self.speed = 2
            pygame.time.delay(3000)
            print("eighth")

        if self.rect.y > 480 and self.dir == 1:
            self.dir = 4
            print("ninth")


        











        
        if self.dir == 1:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        if self.dir == 2:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if self.dir == 3:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        if self.dir == 4:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        
    def reset(self):
        self.rect.x = randint(10, 630)
        self.rect.y = randint(10, 470)
        self.dir = randint(1, 4)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 12, height = 12):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (710, 10)
pygame.mixer.music.load("test.ogg")
pygame.mixer.music.play()
pygame.font.init()
display = pygame.display.set_mode([640, 480], pygame.NOFRAME)
isRunning = True
player = Player(470, 10)
ball = Ball(10, 10)
clock = pygame.time.Clock()
buffer = pygame.Surface((640, 480))
player_sprite_list = pygame.sprite.Group()
bullet_sprite_list = pygame.sprite.Group()
enemy_sprite_list = pygame.sprite.Group()
ball.player = player_sprite_list
player_sprite_list.add(player)
bullet_sprite_list.add(ball)
myfont = pygame.font.SysFont("monospace", 15)




while isRunning:
    label = myfont.render(str(ball.streak), 1, (255, 0, 0))
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for events in pygame.event.get():
    
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                isRunning = False
            if events.key == pygame.K_a:
                player.deltax = -10
            if events.key == pygame.K_d:
                player.deltax = 10
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_a:
                player.deltax = 0
            if events.key == pygame.K_d:
                player.deltax = 0

    player_sprite_list.update()
    bullet_sprite_list.update()






    display.fill((0,0,0))
    player_sprite_list.draw(display)
    bullet_sprite_list.draw(display)
    display.blit(label, (10, 10))
    pygame.display.update()


pygame.quit()

