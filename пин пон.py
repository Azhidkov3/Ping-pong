#Создай собственный Шутер!
#Нет.
from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, image_sprite, player_x, player_y, player_speed, height, width):
        super().__init__()
        self.image = transform.scale(image.load(image_sprite),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x<650:
            self.rect.x += self.speed
window = display.set_mode((700, 500))
display.set_caption('Вьетнамские влешбеки')
background = image.load('back.jpg')
background = transform.scale(background, (700, 500))
player = Player('rocket.png', 150, 150, 20, 50, 150)
game = True
clock = time.Clock()
font.init()
font2 = font.SysFont('Arial', 30)
game_over = font2.render('You lose', True, (255, 0, 0))
you_win = font2.render('You win', True, (255, 0, 0))
FPS = 60
finish = False
while game == True:
    player.reset()
    player.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        player.reset()
        player.update()
        clock.tick(FPS)
        display.update()

