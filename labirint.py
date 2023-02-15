from pygame import*
window = display.set_mode((700,700))
display.set_caption('Angry_birds лабіринт')
picture = transform.scale(image.load('phon.jpg'),(700,500))


class GameSprite(sprite.Sprite):
    def __init__(self, picture,w,h,x,y):
        sprite.Sprite.__init__(self)
        self.image =transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x =x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

barriers = sprite.Group()

panel = GameSprite('panel2.png', 700,200,0,500)



barriers.add(GameSprite('stone.png', 350,50,50,300))
barriers.add(GameSprite('stone2.png', 50,275,150,145))
barriers.add(GameSprite('stone2.png', 50,100,250,400))
barriers.add(GameSprite('stone2.png', 50,250,450,250))
barriers.add(GameSprite('stone2.png', 50,170,545,255))
barriers.add(GameSprite('stone.png', 120,50,450,250))
barriers.add(GameSprite('stone2.png', 50,315,350,110))
barriers.add(GameSprite('stone.png', 130,50,250,110))
barriers.add(GameSprite('stone.png', 120,50,150,205))
barriers.add(GameSprite('stone.png', 125,50,350,150))
barriers.add(GameSprite('stone.png', 115,50,-25,145))
barriers.add(GameSprite('stone2.png', 50,105,300,-40))
barriers.add(GameSprite('stone2.png', 50,130,450,70))
barriers.add(GameSprite('stone2.png', 50,115,80,-20))
barriers.add(GameSprite('stone.png', 120,50,80,45))

player_angry4 = GameSprite('Finish.png', 45,45,495,300)

class Red(GameSprite):
    def __init__(self, picture,w,h,x,y,speed_x,speed_y):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.x_speed = speed_x
        self.y_speed = speed_y 
    def update(self):
        if player2.rect.x <= 700-45 and player2.x_speed > 0 or player2.rect.x >= 0 and player2.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for i in platforms_touched:
                self.rect.right = min(self.rect.right, i.rect.left) 
        elif self.x_speed < 0: 
            for i in platforms_touched:
                self.rect.left = max(self.rect.left, i.rect.right) 
        
        if player2.rect.y <= 500-45 and player2.y_speed > 0 or player2.rect.y >= 0 and player2.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for i in platforms_touched:
                self.y_speed = 0
                if i.rect.top < self.rect.bottom:
                    self.rect.bottom = i.rect.top
        elif self.y_speed < 0: 
            for i in platforms_touched:
                self.y_speed = 0 
                self.rect.top = max(self.rect.top, i.rect.bottom) 
    def fire(self):
        bullet = Bullet('egg.png',20,15,self.rect.right, self.rect.centery,15)
        bullets.add(bullet)

player2 = Red('Red.png', 45,45,10,450,0,0)

class Bullet(GameSprite):
    def __init__(self, picture, w,h,x,y, player_speed):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.speed = player_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >  710:
            self.kill()



wall = GameSprite('stone.png', 120,50,450,375)

class Enemy1(GameSprite):
    side = 'left'
    def __init__(self, picture, w,h,x,y, player_speed):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.speed = player_speed
    
    def update(self):
        if self.rect.y <= 200:
            self.side = 'down'
        if self.rect.y >= 450:
            self.side = 'up'
        
        if self.side == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy2(GameSprite):
    side = 'left'
    def __init__(self, picture, w,h,x,y, player_speed):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 0:
            self.side = 'right'
        if self.rect.x >= 100:
            self.side = 'left'
        
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy3(GameSprite):
    side = 'left'
    def __init__(self, picture, w,h,x,y, player_speed):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 350:
            self.side = 'right'
        if self.rect.x >= 650:
            self.side = 'left'
        
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy4(GameSprite):
    side = 'left'
    def __init__(self, picture, w,h,x,y, player_speed):
        GameSprite.__init__(self,picture,w,h,x,y)
        self.speed = player_speed

    def update(self):
        if self.rect.y <= 75:
            self.side = 'down'
        if self.rect.y >= 200:
            self.side = 'up'
        
        if self.side == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

player_angry= Enemy1('Chak.png',45,45,600,450,10)
player_angry2= Enemy2('Chak.png', 45,45,100,200,4)
player_angry3= Enemy3('Chak.png', 45,45,650,20,8.5)
player_angry5= Enemy4('Chak.png', 45,45,500,200,7)

monsters = sprite.Group()
monsters.add(player_angry)
monsters.add(player_angry2)
monsters.add(player_angry3)
monsters.add(player_angry5)

bullets = sprite.Group()

font.init()
font1 = font.SysFont('arial', 25)

gold_eggs = 0
white_eggs = 10

class Egg(GameSprite):
    def __init__(self, picture,w,h,x,y):
        GameSprite.__init__(self, picture,w,h,x,y)

eggs = sprite.Group()


eggs.add(GameSprite('gold_egg.png', 40,45,200,255))
eggs.add(GameSprite('gold_egg.png', 40,45,10,10))
eggs.add(GameSprite('gold_egg.png', 40,45,400,110))
eggs.add(GameSprite('gold_egg.png', 40,45,400,350))
eggs.add(GameSprite('gold_egg.png', 40,45,150,7))

run = True
finish = False

w_been=False

while run:
    
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
            
            elif i.key == K_SPACE:
                if gold_eggs >= 3:
                    if white_eggs > 0:
                        player2.fire()
                        white_eggs -= 1
            
        elif i.type == KEYUP:
            if i.key == K_LEFT or i.key == K_a:
                player2.x_speed = 0
            elif i.key == K_RIGHT or i.key == K_d:
                player2.x_speed = 0
            elif i.key == K_UP or i.key == K_w:
                player2.y_speed = 0
            elif i.key == K_DOWN or i.key == K_s:
                player2.y_speed = 0
    if not finish:
        window.blit(picture,(0,0))
        barriers.draw(window)
        bullets.draw(window)
        eggs.draw(window)
        bullets.update()
        player2.reset()
        player2.update()
        player_angry4.reset()
        panel.reset()
        
        ##############
        if not w_been:
            wall.reset()
        

        sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        sprite.groupcollide(bullets, barriers, True, False)
    
        if sprite.collide_rect(player2, player_angry4):
            finish = True
            img = image.load('winner.gif')
            window.blit(transform.scale(img, (700, 900)), (0, -100))
    
        if sprite.spritecollide(player2, monsters, False): 
            finish = True
            img = image.load('game_over.jpg')
            window.blit(transform.scale(img, (700, 900)), (0, -100))
        
        if sprite.spritecollide(player2, eggs, True):
            gold_eggs += 1
        coin = font1.render(f'{gold_eggs}', True, (0, 0, 0))
        window.blit(coin, (50, 625))
        
        
        if gold_eggs >= 3:
            if white_eggs > 0:
                for i in event.get():
                    if i.type == KEYDOWN:
                        if i.key == K_SPACE:
                            player2.fire()
                            white_eggs -= 1
        
        
        if gold_eggs < 3:
            patron = font1.render(f'{0}', True, (0, 0, 0))
        else:
            patron = font1.render(f'{white_eggs}', True, (0, 0, 0))
        window.blit(patron, (50, 550))

        
        if gold_eggs==5:
            if not w_been:
                w_been=True
                del wall
        
             

        time.delay(60)
        display.update() 