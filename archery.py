import pygame
import time
import random

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)

hit_sound = pygame.mixer.Sound('hit.mp3')

screen = pygame.display.set_mode((1200,700)) 
pygame.display.set_caption('ARCHERY')

arrow_img = pygame.image.load('arrow.png')
picture = pygame.transform.scale(arrow_img, (164 ,164))

aim_img = pygame.image.load('aimboard.png')
picture_aim = pygame.transform.scale(aim_img, (164 ,164))

font = pygame.font.Font("freesansbold.ttf",32)
font1 = pygame.font.Font("freesansbold.ttf",60)

def show(x,y) :
    show = font.render(" SCORE : " + str(value) , True , (200,0, 0))
    screen.blit(show,(x,y))
    prevs = font.render(" PREVIOUS SCORE : " + str(prev) , True , (200,0, 0))
    screen.blit(prevs,(10,40))
    highs = font.render(" HIGH SCORE : " + str(high) , True , (200,0, 0))
    screen.blit(highs,(10,70))
    lifes = font.render("Life : " + str(life) , True , (200,0, 0))
    screen.blit(lifes,(20,100))
    if value>=0 and value<20:
        l1 = font.render("LEVEL 1", True , (200,0, 0))
        screen.blit(l1,(550,50))
    if value>=20 and value<40:
        l1 = font.render("LEVEL 2", True , (200,0, 0))
        screen.blit(l1,(550,50))
    if value>=40 :
        l1 = font.render("LEVEL 3", True , (200,0, 0))
        screen.blit(l1,(550,50))

def lost (x,y) :
    global game_over
    loses = font1.render(" GAME OVER " , True , (255,0, 0))
    screen.blit(loses,(x,y))
    restart = font1.render(" Press R to Restart " , True , (255,0, 0))
    screen.blit(restart,(350,350))
    game_over=True
    
value = 0
lose = 0
prev = 0
high = 0
life = 3
line_x1 = 0
line_y1 = 400
line_x2 = 200 
line_y2 = 400
arrow_x = 0
arrow_y = 318
aim_y_change = 0
option  = [1,-1] 
show_x = 10
show_y = 10
game_over=False

random_move = random.choice(option)

def arrow ( x,y) :
    screen.blit(picture ,(x,y))
aim_x = 1050
aim_y = 318

def aim (x,y) :
    screen.blit(picture_aim ,(x,y))

def call() :
    global line_x1 ,line_x2,line_y1,line_y2 ,state
    line_x1 = 0
    line_y1 = 400
    line_x2 = 200
    line_y2 = 400
    state = 'not ready'


state = 'not ready'
run = True
l = False
clock = pygame.time.Clock()

while run :
    screen.fill((0,150,150))
    aim( aim_x,aim_y)
    line = pygame.draw.line(screen, (0,0,0),(line_x1,line_y1),(line_x2,line_y2), 3)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key  == pygame.K_SPACE and l != True:
                state = 'ready'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r and game_over:
                line_x1 = 0
                line_y1 = 400
                line_x2 = 200
                line_y2 = 400
                value = 0
                lose = 0
                life = 3
                state = 'not  ready'
                game_over = False
                l = False

    if state == 'ready' :
        line_x1 += 4
        line_x2 += 4
    if line_x1 > 1200 :
        call()
        life -= 1
        lose += 1
    if line_x2 == aim_x+86 :
        if aim_y < 355 and aim_y > 285 :
            value += 9
        if (aim_y > 355 and aim_y < 370 ) or (aim_y > 260 and aim_y < 285 ):
            value += 4
        if 395 > aim_y and aim_y > 250 :
            value += 1
            time.sleep(1)
            call()
            hit_sound.play()
    aim_y +=random_move 
    if aim_y > 550 :
        random_move = -1
        if value>=20:
            random_move=-1.5
            if value>=40:
                random_move=-2
    if aim_y < 0 :
        random_move = 1
        if value>=20:
            random_move=1.5
            if value>=40:
                random_move= 2
    if lose >=3 :
        l = True
        state = 'not ready'
        prev=value
        if prev>high:
            high=value
        lost(400,250)

    arrow( arrow_x,arrow_y )
    show(show_x,show_y)
    pygame.display.update()
    clock.tick(300)
    
pygame.mixer.music.stop() 
pygame.quit()
quit()
 
    
