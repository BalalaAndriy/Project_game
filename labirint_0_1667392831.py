from pygame import*
window = display.set_mode((700,500))
display.set_caption('Angry_birds лабіринт')
picture = transform.scale(image.load('phon.jpg'),(700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, picture,w,h,x,y):
        sprite.Sprite.__init__(self)
        self.image =transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x =x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player1 = GameSprite('stone.png', 450,200,150,200)
player3 = GameSprite('stone2.png', 200,400,350,100)

class Red(GameSprite):
    def __init__(self, picture,w,h,x,y,speed_x,speed_y):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.x_speed = speed_x
        self.y_speed = speed_y 
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
player2 = Red('Red.png', 90,90,55,350,0,0)

run = True
while run:
    time.delay(50)
    window.blit(picture,(0,0))
    player1.reset()
    player2.reset()
    player3.reset()
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_LEFT or i.key == K_a:
                player2.x_speed = -5
            elif i.key == K_RIGHT or i.key == K_d:
                player2.x_speed = 5
            elif i.key == K_UP or i.key == K_w:
                player2.y_speed = -5
            elif i.key == K_DOWN or i.key == K_s:
                player2.y_speed = 5
        elif i.type == KEYUP:
            if i.key == K_LEFT or i.key == K_a:
                player2.x_speed = 0
            elif i.key == K_RIGHT or i.key == K_d:
                player2.x_speed = 0
            elif i.key == K_UP or i.key == K_w:
                player2.y_speed = 0
            elif i.key == K_DOWN or i.key == K_s:
                player2.y_speed = 0
    player2.update()
    display.update()