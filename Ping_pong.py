from pygame import *
window = display.set_mode((700,500))
display.set_caption('ping_pong')
background = transform.scale(image.load('стол.png'),(700,500))
window.blit(background,(0,0))
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('1 игрок проиграл', True, (255, 0, 0 ))
lose2 = font1.render('2 игрок проиграл', True, (255, 0, 0 ))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()   
        self.rect.x = player_x
        self.rect.y = player_y
        self.wight = player_width
        self.height = player_height

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
class Player(GameSprite):       
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y <= 450:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y <= 450:
            self.rect.y += self.speed

ball = GameSprite('ball.png', 250, 250, 15, 50, 50)
raketka1 = Player('ракетка.png', 30, 30, 15, 10, 100)
raketka2 = Player('ракетка.png', 650, 10, 15, 10, 100)
speed_x = 5
speed_y = 5

finish = False
game = True
while game:
   


    if finish != True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= 450 or ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(raketka1, ball) or sprite.collide_rect(raketka2, ball):
            speed_x *= -1
        
        if ball.rect.x <= -50:
            window.blit(lose1, (200, 200))
            finish = True
        if ball.rect.x >= 700:
            window.blit(lose2, (200, 200))
            finish = True
        raketka1.update_l()
        raketka2.update_r()
        raketka1.reset()
        raketka2.reset()
        ball.reset()
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    time.delay(50)
        
