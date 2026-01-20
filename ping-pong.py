from pygame import *

font.init()

window = display.set_mode((700, 500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('fone.jpg'), (700, 500))

clock = time.Clock()

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER_1 LOSE', True, (180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font1.render('PLAYER_2 LOSE', True, (180, 0, 0))

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
    def updater(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_LEFT] and self.rect.x > 1:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
        
    def updated(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 600:
            self.rect.x += self.speed




platforma1 = Player('platforma.jpg', 250, 20, 200, 20, 7)
platforma2 = Player('platforma.jpg', 250, 470, 200, 20, 7)
ball = GameSprite('ball.png', 350, 250, 40, 40, 3)

speed_x = 3
speed_y = 3


finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        platforma1.updated()
        platforma2.updater()
        window.blit(background, (0,0))

        if ball.rect.x > (700-50) or ball.rect.x < 0:
            speed_x *= -1

        if sprite.collide_rect(ball, platforma1) or sprite.collide_rect(ball, platforma2):
            speed_y *= -1

        if ball.rect.y == 0:
            finish = True
            window.blit(lose1, (250, 200))
        
        if ball.rect.y == 490:
            finish = True
            window.blit(lose2, (250, 200))


        platforma1.draw()
        platforma2.draw()
        ball.draw()




    display.update()
    clock.tick(60)