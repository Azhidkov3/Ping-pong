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
        if keys[K_RIGHT] and self.rect.x<550:
            self.rect.x += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x<550:
            self.rect.x += self.speed
class Ball(GameSprite):
    def __init__(self, image_sprite, player_x, player_y, player_speed, height, width):
        super().__init__(image_sprite, player_x, player_y, player_speed, height, width)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.x > 690:
            self.speed_x *= -1
window = display.set_mode((700, 500))
display.set_caption('Вьетнамские влешбеки')
background = image.load('back.jpg')
background = transform.scale(background, (700, 500))
player = Player('rocket.png', 150, 450, 20, 50, 150)
ball = Ball('ball.png', 50, 50, 3, 35, 35)
player2 = Player2('rocket.png', 150, 50, 20, 50, 150)
game = True
clock = time.Clock()
font.init()
font2 = font.SysFont('Arial', 30)
game_over = font2.render('You lose', True, (255, 0, 0))
you_win = font2.render('You win', True, (255, 0, 0))
FPS = 60
finish = False
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0, 0))
        player.reset()
        ball.reset()
        player2.reset()
        player.update()
        ball.update()
        player2.update()
        if sprite.collide_rect(player, ball):
            ball.speed_y *= -1
        if sprite.collide_rect(player2, ball):
            ball.speed_y *= -1
        if ball.rect.y < 0:
            finish = True
            window.blit(game_over, (300, 300))
        if ball.rect.y > 500:
            finish = True
            window.blit(you_win, (300, 300))
        clock.tick(FPS)
        display.update()