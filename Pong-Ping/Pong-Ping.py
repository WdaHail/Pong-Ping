from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        global keys
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
      
font.init()
font = font.SysFont('Times New Roman', 36)
pI = font.render("PlayerI Выйграл!", True, (250, 250, 250))
pII = font.render("PlayerII Выйграл!", True, (250, 250, 250))

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
clock = time.Clock()
FPS = 70
color = (115, 144, 191)
speed_x = 5
speed_y = 4

playerI = Player('стенка.jpg', 70, 150, 35, 150, 6)
playerII = Player('стенка.jpg', 690, 150, 35, 150, 6)
ball = GameSprite('мяч.png',350, 250, 60, 60, 2)

run = True
finish = False
while run == True:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:                
        window.fill(color)    
        playerI.update_l()    
        playerI.reset()
        playerII.update_r()
        playerII.reset()
        ball.update
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(playerI, ball) or sprite.collide_rect(playerII, ball):
            speed_x *= -1

        if ball.rect.y <= 0 or ball.rect.y >= 550:
            speed_y *= -1

        if ball.rect.x <=0:
            window.blit(pII, (270, 250))
            finish = True
        if ball.rect.x >= 790:
            window.blit(pI, (260, 250))
            finish = True
    display.update()
display.update()