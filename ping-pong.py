from pygame import *

window = display.set_mode((700, 500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    

class Player(GameSprite):
    def updateu(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.x > 1:
            self.rect.x -= self.speed
        if key_pressed[K_DOWN] and self.rect.x < 635:
            self.rect.x += self.speed

    def updated(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.


game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False









    display.update()