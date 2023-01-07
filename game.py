import random
import pygame
import gamedata

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255)
green=(0,255,0)
purple=(255,0,255)

pygame.init()


font= pygame.font.Font(None,50)

screen_width = 700
screen_height= 400

screen = pygame.display.set_mode([screen_width, screen_height])

class red_block(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([20,15])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.score=0
        self.lives=2
        self.level=1
        
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:self.rect.y-=5
        if pressed[pygame.K_DOWN]:self.rect.y+=5
        if pressed[pygame.K_LEFT]:self.rect.x-=5
        if pressed[pygame.K_RIGHT]:self.rect.x+=5
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 380:
            self.rect.y = 380
        if self.rect.x > 700:
            self.rect.x = 700
        if self.rect.x < 0:
            self.rect.x = 0
    
       
    
        if pygame.sprite.spritecollide(self,black_block_list,False):
            self.rect.y=30
            self.rect.x=0
            self.lives-1        
            self.score+0
            print(self.score)
            print(self.lives)
            pygame.mixer.music.load('Glass.mp3')
            pygame.mixer.music.play(0)

        if pygame.sprite.spritecollide(self,b13_hit_list,False):
            self.level+=1
            pygame.mixer.music.load('TaDa.mp3')
            pygame.mixer.music.play(0)
            
#-----------------------------------------------------------------------------DeathLine------------------------------------------------------------------------------------------------------#
class black_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class win_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(purple)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


           

block = black_block(25,350)
b1=black_block(25,350)
b2=black_block(150,300)
b3=black_block(250,250)
b4=black_block(25,0)
b5=black_block(150,100)
b6=black_block(250,0)
b7=black_block(500,0)
b8=black_block(500,250)
b9=black_block(400,0)
b10=black_block(400,150)
b11=black_block(650,50)
b12=black_block(650,225)
b13=win_block(690,0)
b14=win_block(690,200)


all_sprites_list = pygame.sprite.Group()
black_block_list = pygame.sprite.Group()
red_block_list = pygame.sprite.Group()
black_block_hit_list=pygame.sprite.Group()

b1_list=pygame.sprite.Group()
b2_list=pygame.sprite.Group()
b3_list=pygame.sprite.Group()
b4_list=pygame.sprite.Group()
b5_list=pygame.sprite.Group()
b6_list=pygame.sprite.Group()
b7_list=pygame.sprite.Group()
b8_list=pygame.sprite.Group()
b9_list=pygame.sprite.Group()
b10_list=pygame.sprite.Group()
b11_list=pygame.sprite.Group()
b12_list=pygame.sprite.Group()

b13_hit_list=pygame.sprite.Group()
b14_hit_list=pygame.sprite.Group()

all_sprites_list.add(b1)
all_sprites_list.add(b2)
all_sprites_list.add(b3)
all_sprites_list.add(b4)
all_sprites_list.add(b5)
all_sprites_list.add(b6)
all_sprites_list.add(b7)
all_sprites_list.add(b8)
all_sprites_list.add(b9)
all_sprites_list.add(b10)
all_sprites_list.add(b11)
all_sprites_list.add(b12)
all_sprites_list.add(b13)
all_sprites_list.add(b14)

b1_list.add(b1)
b2_list.add(b2)
b3_list.add(b3)
b4_list.add(b4)
b5_list.add(b5)
b6_list.add(b6)
b7_list.add(b7)
b8_list.add(b8)
b9_list.add(b9)
b10_list.add(b10)
b11_list.add(b11)
b12_list.add(b12)
#b13_list.add(b13)
#b14_list.add(b14)
b13_hit_list.add(b13)
b14_hit_list.add(b14)

black_block_list.add(block)
black_block_list.add(b1)
black_block_list.add(b2)
black_block_list.add(b3)
black_block_list.add(b4)
black_block_list.add(b5)
black_block_list.add(b6)
black_block_list.add(b7)
black_block_list.add(b8)
black_block_list.add(b9)
black_block_list.add(b10)
black_block_list.add(b11)
black_block_list.add(b12)
black_block_hit_list.add(b13)
black_block_hit_list.add(b14)

all_sprites_list.add(block)

rect_change_x = 2
rect_change_y = 2



player = red_block()
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()

while not done and player.level==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(black)

    if player.level==2:
        done=True
    

    all_sprites_list.update()
    all_sprites_list.draw(screen)
   
     
    pygame.display.flip()
    clock.tick(60)
    
while done and player.level==2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True    
    screen.fill(black)
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    screen.blit(score,[0,50])  
    pygame.display.flip()

    clock.tick(60)

#-----------------------------------------------------------------------------level-2------------------------------------------------------------------------------------------------------#
class red_block(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([20,15])
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.level=1
        0
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:self.rect.y-=5
        if pressed[pygame.K_DOWN]:self.rect.y+=5
        if pressed[pygame.K_LEFT]:self.rect.x-=5
        if pressed[pygame.K_RIGHT]:self.rect.x+=5
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 380:
            self.rect.y = 380
        if self.rect.x > 700:
            self.rect.x = 700
        if self.rect.x < 0:
            self.rect.x = 0
    
        if pygame.sprite.spritecollide(self,black_block_list,False):
            self.rect.y=30
            self.rect.x=0            
            pygame.mixer.music.load('Glass.mp3')
            pygame.mixer.music.play(0)
            
        if pygame.sprite.spritecollide(self,b13_hit_list,False):
            pygame.mixer.music.load('TaDa.mp3')
            pygame.mixer.music.play(0)
            self.level+=1
        
            
        if pygame.sprite.spritecollide(self,moving_line_list,False):
            self.rect.y=30
            self.rect.x=0 
            pygame.mixer.music.load('Wrong.mp3')
            pygame.mixer.music.play(0)

class black_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class win_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class moving_line(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
    #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y = self.rect.y+1
    def update(self):

        self.rect.y=self.rect.y+5
        if self.rect.y > 400:
            self.rect.y=0
            
block = black_block(25,350)
b1=black_block(25,350)
b2=black_block(150,300)
b3=black_block(250,250)
b4=black_block(25,0)
b5=black_block(150,100)
b6=black_block(250,0)
b7=black_block(500,0)
b8=black_block(500,250)
b9=black_block(400,0)
b10=black_block(400,150)
b11=black_block(650,50)
b12=black_block(650,225)
b13=win_block(690,0)
b14=win_block(690,200)

m1=moving_line(250,0)
m2=moving_line(25,0)
m3=moving_line(500,0)
m4=moving_line(400,0)
m5=moving_line(650,0)
m6=moving_line(400,0)

all_sprites_list = pygame.sprite.Group()
black_block_list = pygame.sprite.Group()
red_block_list = pygame.sprite.Group()
black_block_hit_list=pygame.sprite.Group()
moving_line_list=pygame.sprite.Group()

b1_list=pygame.sprite.Group()
b2_list=pygame.sprite.Group()
b3_list=pygame.sprite.Group()
b4_list=pygame.sprite.Group()
b5_list=pygame.sprite.Group()
b6_list=pygame.sprite.Group()
b7_list=pygame.sprite.Group()
b8_list=pygame.sprite.Group()
b9_list=pygame.sprite.Group()
b10_list=pygame.sprite.Group()
b11_list=pygame.sprite.Group()
b12_list=pygame.sprite.Group()

b13_hit_list=pygame.sprite.Group()
b14_hit_list=pygame.sprite.Group()

all_sprites_list.add(b1)
all_sprites_list.add(b2)
all_sprites_list.add(b3)
all_sprites_list.add(b4)
all_sprites_list.add(b5)
all_sprites_list.add(b6)
all_sprites_list.add(b7)
all_sprites_list.add(b8)
all_sprites_list.add(b9)
all_sprites_list.add(b10)
all_sprites_list.add(b11)
all_sprites_list.add(b12)
all_sprites_list.add(b13)
all_sprites_list.add(b14)
all_sprites_list.add(m1)
all_sprites_list.add(m2)
all_sprites_list.add(m3)
all_sprites_list.add(m4)
all_sprites_list.add(m5)
all_sprites_list.add(m6)


b1_list.add(b1)
b2_list.add(b2)
b3_list.add(b3)
b4_list.add(b4)
b5_list.add(b5)
b6_list.add(b6)
b7_list.add(b7)
b8_list.add(b8)
b9_list.add(b9)
b10_list.add(b10)
b11_list.add(b11)
b12_list.add(b12)
#b13_list.add(b13)
#b14_list.add(b14)
b13_hit_list.add(b13)
b14_hit_list.add(b14)


black_block_list.add(block)
black_block_list.add(b1)
black_block_list.add(b2)
black_block_list.add(b3)
black_block_list.add(b4)
black_block_list.add(b5)
black_block_list.add(b6)
black_block_list.add(b7)
black_block_list.add(b8)
black_block_list.add(b9)
black_block_list.add(b10)
black_block_list.add(b11)
black_block_list.add(b12)
black_block_hit_list.add(b13)
black_block_hit_list.add(b14)

moving_line_list.add(m1)
moving_line_list.add(m2)
moving_line_list.add(m3)
moving_line_list.add(m4)
moving_line_list.add(m5)
moving_line_list.add(m6)
all_sprites_list.add(block)



player = red_block()
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()

while not done and player.level==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(black)

    if player.level==2:
        done=True
    

    all_sprites_list.update()
    all_sprites_list.draw(screen)
   
     
    pygame.display.flip()
    clock.tick(60)
    
while done and player.level==2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True    
    screen.fill(black)
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    screen.blit(score,[0,50])  
    pygame.display.flip()

    clock.tick(60)
#-------------------------------Level 3------------------------------------------#
class red_block(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([20,15])
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.level=1
        0
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:self.rect.y-=5
        if pressed[pygame.K_DOWN]:self.rect.y+=5
        if pressed[pygame.K_LEFT]:self.rect.x-=5
        if pressed[pygame.K_RIGHT]:self.rect.x+=5
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 380:
            self.rect.y = 380
        if self.rect.x > 700:
            self.rect.x = 700
        if self.rect.x < 0:
            self.rect.x = 0
    
       
    
        if pygame.sprite.spritecollide(self,black_block_list,False):
            self.rect.y=30
            self.rect.x=0
            pygame.mixer.music.play()
            pygame.mixer.music.load('Glass.mp3')
            pygame.mixer.music.play(0)
    
        if pygame.sprite.spritecollide(self,b13_hit_list,False):
            self.level+=1
            pygame.mixer.music.play()
            pygame.mixer.music.load('TaDa.mp3')
            pygame.mixer.music.play(0)

        if pygame.sprite.spritecollide(self,moving_line_list,False):
            self.rect.y=30
            self.rect.x=0 
            pygame.mixer.music.load('Wrong.mp3')
            pygame.mixer.music.play(0)

        if pygame.sprite.spritecollide(self,horizon_moving_line_list,False):
            self.rect.y=30
            self.rect.x=0
            pygame.mixer.music.play()
            pygame.mixer.music.load('Smash.mp3')
            pygame.mixer.music.play(0)

class black_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(green)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class win_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class moving_line(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
    #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(purple)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y = self.rect.y+1
    def update(self):

        self.rect.y=self.rect.y+5
        if self.rect.y > 400:
            self.rect.y=0

class horizon_moving_line(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
    #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([200,10])
        self.image.fill(purple)

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.x+1
        self.rect.y=y
    def update(self):

        self.rect.x=self.rect.x+5
        if self.rect.x > 700:
            self.rect.x=0
            
block = black_block(25,350)
b1=black_block(25,350)
b2=black_block(150,300)
b3=black_block(250,250)
b4=black_block(25,0)
b5=black_block(150,100)
b6=black_block(250,0)
b7=black_block(500,0)
b8=black_block(500,250)
b9=black_block(400,0)
b10=black_block(400,150)
b11=black_block(650,50)
b12=black_block(650,225)
b13=win_block(690,0)
b14=win_block(690,200)

m1=moving_line(250,0)
m2=moving_line(25,0)
m3=moving_line(500,0)
m4=moving_line(400,0)
m5=moving_line(650,0)
m6=moving_line(400,0)

hm=horizon_moving_line(0,50)
hm1=horizon_moving_line(10,155)
hm2=horizon_moving_line(20,250)
hm3=horizon_moving_line(30,350)

all_sprites_list = pygame.sprite.Group()
black_block_list = pygame.sprite.Group()
red_block_list = pygame.sprite.Group()
black_block_hit_list=pygame.sprite.Group()
moving_line_list=pygame.sprite.Group()
horizon_moving_line_list=pygame.sprite.Group()

b1_list=pygame.sprite.Group()
b2_list=pygame.sprite.Group()
b3_list=pygame.sprite.Group()
b4_list=pygame.sprite.Group()
b5_list=pygame.sprite.Group()
b6_list=pygame.sprite.Group()
b7_list=pygame.sprite.Group()
b8_list=pygame.sprite.Group()
b9_list=pygame.sprite.Group()
b10_list=pygame.sprite.Group()
b11_list=pygame.sprite.Group()
b12_list=pygame.sprite.Group()

b13_hit_list=pygame.sprite.Group()
b14_hit_list=pygame.sprite.Group()

all_sprites_list.add(b1)
all_sprites_list.add(b2)
all_sprites_list.add(b3)
all_sprites_list.add(b4)
all_sprites_list.add(b5)
all_sprites_list.add(b6)
all_sprites_list.add(b7)
all_sprites_list.add(b8)
all_sprites_list.add(b9)
all_sprites_list.add(b10)
all_sprites_list.add(b11)
all_sprites_list.add(b12)
all_sprites_list.add(b13)
all_sprites_list.add(b14)
all_sprites_list.add(m1)
all_sprites_list.add(m2)
all_sprites_list.add(m3)
all_sprites_list.add(m4)
all_sprites_list.add(m5)
all_sprites_list.add(m6)
all_sprites_list.add(hm)
all_sprites_list.add(hm1)
all_sprites_list.add(hm2)
all_sprites_list.add(hm3)


b1_list.add(b1)
b2_list.add(b2)
b3_list.add(b3)
b4_list.add(b4)
b5_list.add(b5)
b6_list.add(b6)
b7_list.add(b7)
b8_list.add(b8)
b9_list.add(b9)
b10_list.add(b10)
b11_list.add(b11)
b12_list.add(b12)
#b13_list.add(b13)
#b14_list.add(b14)
b13_hit_list.add(b13)
b14_hit_list.add(b14)


black_block_list.add(block)
black_block_list.add(b1)
black_block_list.add(b2)
black_block_list.add(b3)
black_block_list.add(b4)
black_block_list.add(b5)
black_block_list.add(b6)
black_block_list.add(b7)
black_block_list.add(b8)
black_block_list.add(b9)
black_block_list.add(b10)
black_block_list.add(b11)
black_block_list.add(b12)
black_block_hit_list.add(b13)
black_block_hit_list.add(b14)

moving_line_list.add(m1)
moving_line_list.add(m2)
moving_line_list.add(m3)
moving_line_list.add(m4)
moving_line_list.add(m5)
moving_line_list.add(m6)

horizon_moving_line_list.add(hm1)
horizon_moving_line_list.add(hm2)
horizon_moving_line_list.add(hm3)
horizon_moving_line_list.add(hm)

all_sprites_list.add(block)



player = red_block()
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()

while not done and player.level==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(black)

    if player.level==2:
        done=True
    

    all_sprites_list.update()
    all_sprites_list.draw(screen)
   
     
    pygame.display.flip()
    clock.tick(60)
    
while done and player.level==2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True    
    screen.fill(black)
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    screen.blit(score,[0,50])  
    pygame.display.flip()

    clock.tick(60)

#-------------------------------Level 4------------------------------------------#
class red_block(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([20,15])
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.level=1
        0
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:self.rect.y-=5
        if pressed[pygame.K_DOWN]:self.rect.y+=5
        if pressed[pygame.K_LEFT]:self.rect.x-=5
        if pressed[pygame.K_RIGHT]:self.rect.x+=5
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 380:
            self.rect.y = 380
        if self.rect.x > 700:
            self.rect.x = 700
        if self.rect.x < 0:
            self.rect.x = 0
    
       
    
        if pygame.sprite.spritecollide(self,black_block_list,False):
            self.rect.y=30
            self.rect.x=0            
    
        if pygame.sprite.spritecollide(self,b13_hit_list,False):
            self.level+=1

        if pygame.sprite.spritecollide(self,moving_line_list,False):
            self.rect.y=30
            self.rect.x=0 

        if pygame.sprite.spritecollide(self,horizon_moving_line_list,False):
            self.rect.y=30
            self.rect.x=0 

        if pygame.sprite.spritecollide(self,box_list,False):
            self.rect.y=30
            self.rect.x=0 

class black_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class win_block(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
        #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class moving_line(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
    #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([10,200])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y = self.rect.y+1
    def update(self):

        self.rect.y=self.rect.y+5
        if self.rect.y > 400:
            self.rect.y=0

class horizon_moving_line(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
    #call the parent class (sprite) contructor
        super().__init__()

        self.image=pygame.Surface([200,10])
        self.image.fill(purple)

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.x+1
        self.rect.y=y
    def update(self):
        self.rect.x=self.rect.x+9
        if self.rect.x > 700:
            self.rect.x=0

class box(pygame.sprite.Sprite):
    """This class represents the blcok"""
    def __init__(self, x,y):
    #call the parent class (sprite) contructor
        super().__init__()
        self.image=pygame.Surface([50,50])
        self.image.fill(purple)

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.x-1
        self.rect.y = self.rect.y-1
    def update(self):
       if self.rect.x > 700:
            self.rect.x=0

       self.rect.y=self.rect.y+5 
       if self.rect.y > 400:
            self.rect.y=0


            
block = black_block(25,350)
b1=black_block(25,350)
b2=black_block(150,300)
b3=black_block(250,250)
b4=black_block(25,0)
b5=black_block(150,100)
b6=black_block(250,0)
b7=black_block(500,0)
b8=black_block(500,250)
b9=black_block(400,0)
b10=black_block(400,150)
b11=black_block(650,50)
b12=black_block(650,225)
b13=win_block(690,0)
b14=win_block(690,200)

m1=moving_line(250,0)
m2=moving_line(25,0)
m3=moving_line(500,0)
m4=moving_line(400,0)
m5=moving_line(650,0)
m6=moving_line(400,0)

hm=horizon_moving_line(0,50)
hm1=horizon_moving_line(10,155)
hm2=horizon_moving_line(20,250)
hm3=horizon_moving_line(30,350)

bb1=box(50,0)
bb2=box(650,350)

all_sprites_list = pygame.sprite.Group()
black_block_list = pygame.sprite.Group()
red_block_list = pygame.sprite.Group()
black_block_hit_list=pygame.sprite.Group()
moving_line_list=pygame.sprite.Group()
horizon_moving_line_list=pygame.sprite.Group()
box_list=pygame.sprite.Group()

b1_list=pygame.sprite.Group()
b2_list=pygame.sprite.Group()
b3_list=pygame.sprite.Group()
b4_list=pygame.sprite.Group()
b5_list=pygame.sprite.Group()
b6_list=pygame.sprite.Group()
b7_list=pygame.sprite.Group()
b8_list=pygame.sprite.Group()
b9_list=pygame.sprite.Group()
b10_list=pygame.sprite.Group()
b11_list=pygame.sprite.Group()
b12_list=pygame.sprite.Group()


b13_hit_list=pygame.sprite.Group()
b14_hit_list=pygame.sprite.Group()

all_sprites_list.add(b1)
all_sprites_list.add(b2)
all_sprites_list.add(b3)
all_sprites_list.add(b4)
all_sprites_list.add(b5)
all_sprites_list.add(b6)
all_sprites_list.add(b7)
all_sprites_list.add(b8)
all_sprites_list.add(b9)
all_sprites_list.add(b10)
all_sprites_list.add(b11)
all_sprites_list.add(b12)
all_sprites_list.add(b13)
all_sprites_list.add(b14)
all_sprites_list.add(m1)
all_sprites_list.add(m2)
all_sprites_list.add(m3)
all_sprites_list.add(m4)
all_sprites_list.add(m5)
all_sprites_list.add(m6)
all_sprites_list.add(hm)
all_sprites_list.add(hm1)
all_sprites_list.add(hm2)
all_sprites_list.add(hm3)
all_sprites_list.add(bb1)
all_sprites_list.add(bb2)


b1_list.add(b1)
b2_list.add(b2)
b3_list.add(b3)
b4_list.add(b4)
b5_list.add(b5)
b6_list.add(b6)
b7_list.add(b7)
b8_list.add(b8)
b9_list.add(b9)
b10_list.add(b10)
b11_list.add(b11)
b12_list.add(b12)
#b13_list.add(b13)
#b14_list.add(b14)
b13_hit_list.add(b13)
b14_hit_list.add(b14)


black_block_list.add(block)
black_block_list.add(b1)
black_block_list.add(b2)
black_block_list.add(b3)
black_block_list.add(b4)
black_block_list.add(b5)
black_block_list.add(b6)
black_block_list.add(b7)
black_block_list.add(b8)
black_block_list.add(b9)
black_block_list.add(b10)
black_block_list.add(b11)
black_block_list.add(b12)
black_block_hit_list.add(b13)
black_block_hit_list.add(b14)

moving_line_list.add(m1)
moving_line_list.add(m2)
moving_line_list.add(m3)
moving_line_list.add(m4)
moving_line_list.add(m5)
moving_line_list.add(m6)

horizon_moving_line_list.add(hm1)
horizon_moving_line_list.add(hm2)
horizon_moving_line_list.add(hm3)
horizon_moving_line_list.add(hm)

box_list.add(bb1)
box_list.add(bb2)

all_sprites_list.add(block)



player = red_block()
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()

while not done and player.level==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(black)

    if player.level==2:
        done=True
    

    all_sprites_list.update()
    all_sprites_list.draw(screen)
   
     
    pygame.display.flip()
    clock.tick(60)
    
while done and player.level==2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True    
    screen.fill(black)
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    screen.blit(score,[0,50])  
    pygame.display.flip()

    clock.tick(60)
pygame.quit()  


