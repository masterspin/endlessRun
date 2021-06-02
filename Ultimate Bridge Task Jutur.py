# ultimateBT_Jutur.py

import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

W,H = 680,267
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Endless Run - Jutur')

bg = pygame.image.load(os.path.join('bg.png')).convert()
bg = pygame.transform.scale(bg, (680, int(266.666)))
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

        

class player(object):
    run = [pygame.image.load(os.path.join('player', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('player', str(x) + '.png')) for x in range(1,6)]
    fall = pygame.image.load(os.path.join('player', '0.png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
##    print(len(jumpList))
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
        self.falling=False

##    def jump(self):
##        if (self.onGround==False):
##            return
##        self.velocity=8                        
##        self.onGround= False
    
    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 0.45
            win.blit(self.jump[self.jumpCount//36], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.region = (self.x,self.y,self.width-44,self.height-27)
        elif self.falling:
            win.blit(self.fall,(self.x,self.y+10))
            self.region = (self.x,self.y+5,self.width-24,self.height-38)
            
        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.region = (self.x,self.y,self.width-44,self.height-30)
        pygame.draw.rect(win,(255,255,255),self.region,2)


class obstacle1(object):
    img = [pygame.image.load(os.path.join('Obstacle1',str(x)+'.png')) for x in range(0,18)]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.region = (self,x,y,width,height)
        self.count = 0
    def draw(self, win):
        self.region = (self.x+55,self.y+92,self.width-15,self.height-15)
        if self.count >= 51:
            self.count=0
        win.blit(pygame.transform.scale(self.img[self.count//3], (150,150)), (self.x,self.y))
        self.count+=1
        pygame.draw.rect(win,(0,0,255), self.region,2)
    def collide(self, rect):
        if rect[0]+rect[2] > self.region[0] and rect[0] < self.region[0] + self.region[2]:
            if rect[1] + rect[3] > self.region[1]:
                return True
            return False

class obstacle2(object):
    img = [pygame.image.load(os.path.join('Obstacle2',str(x)+'.png')) for x in range(0,18)]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.region = (self,x,y,width,height)
        self.count = 0
    def draw(self, win):
        self.region = (self.x+25,self.y+30,self.width+20,self.height+20)
        if self.count >= 51:
            self.count=0
        win.blit(pygame.transform.scale(self.img[self.count//3], (128,128)), (self.x,self.y))                    
        self.count+=1
        pygame.draw.rect(win,(255,0,0), self.region,2)
    def collide(self, rect):
        if rect[0]+rect[2] > self.region[0] and rect[0] < self.region[0] + self.region[2]:
            if rect[1] < self.region[1]+ self.region[3]:
                return True
            return False
    
        
        

class obstacle3(object):
    img = [pygame.image.load(os.path.join('Obstacle 3',str(x)+'.png')) for x in range(0,4)]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.region = (self,x,y,width,height)
        self.count = 0
    def draw(self, win):
        self.region = (self.x-1,self.y,34,30)
        if self.count >= 16:
            self.count=0
        win.blit(pygame.transform.scale(self.img[self.count//4], (32,28)), (self.x,self.y))
        self.count+=1
        pygame.draw.rect(win,(0,255,0), self.region,2)
    def collide(self, rect):
        if rect[0]+rect[2] > self.region[0] and rect[0] < self.region[0] + self.region[2]:
            if rect[1] + rect[3] > self.region[1]:
                return True
            return False


##def start():
##    global pause, score, bgspeed, obstacles, score
##    pause = 0
##    bgspeed = 30
##    obstacles = []
##    run = True
##    intro = True
##    while intro:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                    redrawGameWindow()
##        win.blit(bg, (0,0))
##        title = pygame.font.SysFont('arial',40,bold=True,italic=True)
##        text = title.render('Adventure Man Runner Game',1,(51,241,151))
##        tip = pygame.font.SysFont('arial',17,bold=True,italic=True)
##        click = tip.render('Click Anywhere To Start',1,(255,255,255))
##        win.blit(click,(W/2-click.get_width()/2,240))
##        win.blit(text,(W/2-text.get_width()/2,50))
##        pygame.display.update()

def redrawGameWindow():
    win.blit(bg,(bgX,0))
    win.blit(bg,(bgX2,0))
    player.draw(win)
    for i in obstacles:
        i.draw(win)

    font = pygame.font.SysFont('arial',20,bold=True)
    text = font.render('Score: '+str(score),1,(255,255,0))
    pen = pygame.font.SysFont('arial',17,bold=True)
    rules= pen.render('Jump: Up Arrow/Spacebar',1,(25,25,25))
    win.blit(rules,(10,10))
    win.blit(text,(600,10))
    pygame.display.update()

def scoreFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score
               
    return last

def stop():
    global pause, score, bgspeed, obstacles, score
    pause = 0
    bgspeed = 30
    obstacles = []
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                player.falling=False
                player.jumping = False       
        win.blit(bg, (0,0))
        scoreWrite = pygame.font.SysFont('arial',20,bold=True)
        tip = pygame.font.SysFont('arial',17, italic=True, bold =True)
        highScore = scoreWrite.render('High Score: ' + str(scoreFile()),1,(69,255,0))
        win.blit(highScore,(W/2-highScore.get_width()/2,113))
        newScore = scoreWrite.render('Score: ' + str(score),1,(64,224,208))
        win.blit(newScore,(W/2-newScore.get_width()/2,133))
        click = tip.render('Click Anywhere To Start Over',1,(255,255,255))
        win.blit(click,(W/2-click.get_width()/2,240))
        pygame.display.update()
    score = 0
        

           


#main loop
player = player(340,190,64,64)
pygame.time.set_timer(USEREVENT+1,1000)
pygame.time.set_timer(USEREVENT+2, random.randrange(3000,4000))
bgspeed=30
run = True


pause = 0
fallSpeed = 0
obstacles=[]





while run:
    score = bgspeed-30
##    start()
    if pause > 0:
        pause +=1
        if pause > fallSpeed *2:
            stop()
    for obstacle in obstacles:
        if obstacle.collide(player.region):
            player.falling = True
            if pause ==0:
                fallSpeed = bgspeed
                pause = 1
        obstacle.x-=4
        if obstacle.x < obstacle.width *-1:
            obstacles.pop(obstacles.index(obstacle))
    
    bgX-=4
    bgX2 -=4
    if bgX<bg.get_width()*-1:
        bgX = bg.get_width() #resetting the background to (0,0)
        
    if bgX2<bg.get_width()*-1: #compy of background to keep it look like it's continuous
        bgX2 = bg.get_width()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == USEREVENT+1:
            bgspeed+=1
        if event.type == USEREVENT+2:
            r = random.randrange(0,3)
            if r == 0:
                obstacles.append(obstacle1(720,90,60,60))
            elif r == 1:
                obstacles.append(obstacle2(720,70,60,60))
            else:
                obstacles.append(obstacle3(720,195,60,60))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(player.jumping):  
            player.jumping = True

    clock.tick(bgspeed)
    redrawGameWindow()
