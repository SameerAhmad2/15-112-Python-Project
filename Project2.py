import pygame
import math
import random
from PIL import Image

def loadBZombieImg(frame):
    return pygame.image.load("BrainZombie"+str(frame)+".png")

def loadCZombieImg(frame):
    return pygame.image.load("CapZombie"+str(frame)+".png")

def RandomBorderPos():
    global ListofBoundaryCoords
    global width
    global height
    for i in range(width):
        ListofBoundaryCoords += [(i,0)]
        ListofBoundaryCoords += [(i,height)]
    for i in range(height):
        ListofBoundaryCoords += [(0,i)]
        ListofBoundaryCoords += [(width,i)]

def SummonZombie(mX,mY):
    global AllZombies
    global angle
    Zombie = BrainZombie(mX,mY,angle)
    AllZombies.append(Zombie)

#Class for the Brain Zombie Sprite

class BrainZombie(pygame.sprite.Sprite):
    global Screen
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 1
        self.x_pos = x
        self.y_pos = y
        self.angle = angle
        self.allFrames = []
        for i in range(8):
            self.allFrames.append(loadBZombieImg(self.frame+i))
        self.me = None
        
    def move(self,mX,mY):
        global FrameCount
        x_Dist = mX - self.x_pos
        y_Dist = mY - self.y_pos
        x_change = x_Dist/float(300000)
        y_change = y_Dist/float(300000)
        self.x_pos += x_change
        self.y_pos += y_change
        if FrameCount%50 == 0:
            self.frame = self.frame&8 + 1
        FrameCount += 1
        
    def rotate(self,mX,mY):
        Vect1 = (1,0)
        Vect2 = (mX-(self.x_pos),mY-(self.y_pos))
        Angle = math.acos((Vect1[0]*Vect2[0] + Vect1[1]*Vect2[1])/(math.sqrt((mX-(self.x_pos))**2 + (mY-(self.y_pos))**2)))
        DegAngle = math.degrees(Angle)
        if mY>y:
            angle = - DegAngle - 90
        else:
            angle = DegAngle - 90
        self.angle = angle
        for i in range(8):
            self.allFrames[i] = pygame.transform.rotate(self.allFrames[i],angle)
        
    def update(self):
        if self.me != None:
            Screen.fill(white)
        self.me = Screen.blit(self.allFrames[self.frame],(self.x_pos,self.y_pos))
       
class Player(pygame.sprite.Sprite):
    def __init__(self,Img,lives,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image - Img
        self.Life = lives
        self.x_pos = x
        self.y_pos = y
    def CheckLives(self):
        if self.Life == "0":
            self.kill()
##    def Update(self):
##
##    def Rotate(self):

pygame.init()
width,height = 600,500
Screen = pygame.display.set_mode((width,height))
white = 255,255,255
FrameCount = 0
gameExit = False
##count = 1
angle = -90
AllZombies = []
x,y = (width/2)-32,(height/2)-32
x_change = 0
y_change = 0
mX , mY = 0 , 0
RandomNo1 = random.randint(4,15)
RandomNo2 = RandomNo1 - random.randint(3,22)
ListofBoundaryCoords = []
##Brain1 = BrainZombie(frame,x,y,angle)
for i in range(RandomNo1):
    SummonZombie(width-32,height-32)
while not gameExit:
    Screen.fill(white)
    for Zomb in AllZombies:
        (mX,mY) = pygame.mouse.get_pos()
        Zomb.move(mX,mY)                
        Zomb.rotate(mX,mY)
        Zomb.update()


















    
