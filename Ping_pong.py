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
        
class Player(GameSprite):       
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >= 5:
            self.rect.x -= self.speed 
        if keys_pressed[K_d] and self.rect.x <= 640:
            self.rect.x += self.speed
