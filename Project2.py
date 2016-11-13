import pygame
import math
import random
##import numpy
##import cv2
from PIL import Image
import ImageWriter

#**|** The relevant code was borrowed from http://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point

def HealthBar(Percentage):
    PlayerHealth = pygame.image.load(str(Percentage)+"%.png")
    return PlayerHealth
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

def SummonZombie(Type,x,y):
    global AllZombies
    global angle
    if Type == "Brain":
        Zombie = BrainZombie(x,y,angle)
    else:
        Zombie = CapZombie(x,y,angle)
    AllZombies.append(Zombie)

def Rotate(Img,x,y):
    (mX,mY) = pygame.mouse.get_pos()
    Vect1 = (1,0)
    Vect2 = (mX-x,mY-y)
    Angle = math.acos((Vect1[0]*Vect2[0] + Vect1[1]*Vect2[1])/(math.sqrt((mX-x)**2 + (mY-y)**2)))
    DegAngle = math.degrees(Angle)
    if mY>y:
        angle = - DegAngle - 90
    else:
        angle = DegAngle - 90
##    RotImg = pygame.transform.rotate(Img,angle)
    # **|**
##    image_center = (numpy.array(Img.shape)/2)
##    Rotation_Matrix = cv2.getRotationMatrix2D(image_center,angle,1.0)
##    RotImg = cv2.wrapAffine(Img,Rotation_Matrix,Img.shape,flags = cv2.INTER_LINEAR)
##    return RotImg

#Class for the Brain Zombie Sprite

class BrainZombie():
    global Screen
    def __init__(self,x,y,angle):
        self.frame = 1
        self.x_pos = x
        self.y_pos = y
        self.angle = angle
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("BrainZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.me = None
        
    def move(self,mX,mY):
        global FrameCount
        x_Dist = mX - self.x_pos
        y_Dist = mY - self.y_pos
        x_change = x_Dist/float(300)
        y_change = y_Dist/float(300)
        self.x_pos += x_change
        self.y_pos += y_change
        if FrameCount%5 == 0:
            self.frame = self.frame%8 + 1
        FrameCount += 1
        
    def rotate(self,mX,mY):
        Img = self.allFrames[self.frame - 1]
        NewImg = Rotate(Img,self.x_pos,self.y_pos)
        self.allFrames[self.frame - 1] = NewImg
        
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],(self.x_pos,self.y_pos))

class CapZombie():
    global Screen
    def __init__(self,x,y,angle):
        self.frame = 1
        self.x_pos = x
        self.y_pos = y
        self.angle = angle
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("CapZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.me = None
        
    def move(self,mX,mY):
        global FrameCount
        x_Dist = mX - self.x_pos
        y_Dist = mY - self.y_pos
        x_change = x_Dist/float(50)
        y_change = y_Dist/float(50)
        self.x_pos += x_change
        self.y_pos += y_change
        if FrameCount%5 == 0:
            self.frame = self.frame%8 + 1
        FrameCount += 1
        
    def rotate(self,mX,mY):
        Img = self.allFrames[self.frame - 1]
        NewImg = Rotate(Img,self.x_pos,self.y_pos)
        self.allFrames[self.frame - 1] = NewImg
        
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],(self.x_pos,self.y_pos))

class BlinkingZombie():
    global Screen
    def __init__(self,x,y,angle):
        self.frame = 1
        self.x_pos = x
        self.y_pos = y
        self.angle = angle
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("BlinkingZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.me = None
        
    def move(self,mX,mY):
        global FrameCount
        x_Dist = mX - self.x_pos
        y_Dist = mY - self.y_pos
        x_change = x_Dist/float(300)
        y_change = y_Dist/float(300)
        self.x_pos += x_change
        self.y_pos += y_change
        if FrameCount%5 == 0:
            self.frame = self.frame%8 + 1
        FrameCount += 1
        
    def rotate(self,mX,mY):
        Img = self.allFrames[self.frame - 1]
        NewImg = Rotate(Img,self.x_pos,self.y_pos)
        self.allFrames[self.frame - 1] = NewImg
        
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],(self.x_pos,self.y_pos))
       
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
width,height = 900,500
Screen = pygame.display.set_mode((width,height))
white = 255,255,255
FrameCount = 0
gameExit = False
##count = 1
NewZombieCount = -40
angle = -90
AllZombies = []
x,y = (width/2)-32,(height/2)-32
x_change = 0
y_change = 0
mX , mY = 0 , 0
RandomNo1 = random.randint(4,15)
Percentage = 100
##RandomNo2 = random.randint(4,9)
ListofBoundaryCoords = []
for i in range(width/2):
    ListofBoundaryCoords += [(i,0)]
for i in range(width/2,width):
    ListofBoundaryCoords += [(i,height)]
for i in range(height/2):
    ListofBoundaryCoords += [(0,i)]
for i in range(height/2,height):
    ListofBoundaryCoords += [(width,i)]
clock = pygame.time.Clock()
##Brain1 = BrainZombie(frame,x,y,angle)
for i in range(RandomNo1):
    RandomNo2 = random.randint(1,(width+height))
    (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
    SummonZombie("Brain",x,y)
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    Screen.fill(white)
    for Zomb in AllZombies:
        (mX,mY) = pygame.mouse.get_pos()
        Zomb.move(mX,mY)                
##        Zomb.rotate(mX,mY)
        Zomb.update()
    if NewZombieCount%3600 == 0 and NewZombieCount != 0:
        RandomNo2 = random.randint(1,(width+height))
        (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
        Decider = random.choice([1,2,3,4,5,6,7,8,9,10])
        if Decider < 4:
            SummonZombie("Cap",x,y)
        else: 
            SummonZombie("Brain",x,y)
    NewZombieCount += 1
    Screen.blit(HealthBar(Percentage),(width-210,height-140))    
    pygame.display.update()
    clock.tick(75)
pygame.quit()
quit()

















    
