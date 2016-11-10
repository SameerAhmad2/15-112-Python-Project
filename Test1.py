import pygame
import math
import random


pygame.init()
width = 600
height = 500
Screen = pygame.display.set_mode((width,height))
white = 255,255,255
frame = 1
gameExit = False
count = 1
angle = -90
def MoveZombie(mX,mY,x,y):
    Dist1 = mX - x
    Dist2 = mY - y
##    if Modulus(Dist1) and Modulus(Dist2)<100:
##        Dist1 += Modulus(Dist1) 
##        Dist2 += Modulus(Dist2) 
    x_change = Dist1/float(3000)
    y_change = Dist2/float(3000)    
    return (x_change,y_change) 

    

def AngleCalc(mX,mY,x,y):
    Vect1Cor = (1,0)
    Vect2Cor = (mX-(x),mY-(y))
    Angle = math.acos((Vect1Cor[0]*Vect2Cor[0] + Vect1Cor[1]*Vect2Cor[1])/(math.sqrt((mX-(x))**2 + (mY-(y))**2)))
    DegreeAngle = math.degrees(Angle)
    Screen.fill(white)
    if mY>y:
        angle = - DegreeAngle - 90
    else:
        angle = DegreeAngle - 90
    return angle
##
def Modulus(x):
    if x<0:
        x = -(x)
    return x
        
def Rotate(Img,Angle,x,y):
    global Screen
    ImgRect = Img.get_rect()
    NewImg = pygame.transform.rotate(Img,Angle)
    ImgRect = NewImg.get_rect().center
    Screen.blit(NewImg,(x,y))

def BrainZombie(x,y,frame,angle):
    Zombie = pygame.image.load("BrainZombie"+str(frame)+".png")
    Rotate(Zombie,angle,x,y)

def CapZombie(x,y,frame,angle):
    Zombie = pygame.image.load("CapZombie"+str(frame)+".png")
    Rotate(Zombie,angle,x,y)

x,y = (width/2)-32,(height/2)-32
x_change = 0
y_change = 0
mX , mY = 0 , 0
RandomNo1 = random.randint(20,25)
RandomNo2 = RandomNo1 - random.randint(3,22)
ListofBoundaryCoords = []
ListofZombieCoords = []

for i in range(width):
    ListofBoundaryCoords += [(i,0)]
for i in range(width):
    ListofBoundaryCoords += [(i,height)]
for i in range(height):
    ListofBoundaryCoords += [(0,i)]
for i in range(height):
    ListofBoundaryCoords += [(width,i)]

##for i in range(10):
##    (mX,mY) = pygame.mouse.get_pos()
##    start_x = random.choice(ListofBoundaryCoords)[0]
##    start_y = random.choice(ListofBoundaryCoords)[1]
##    ListofZombieCoords += [(start_x,start_y)]
##    if i<RandomNo2:
##        angle = AngleCalc(mX,mY,start_x,start_y)
##        BrainZombie(start_x,start_y,frame,angle)
##    else:
##        angle = AngleCalc(mX,mY,start_x,start_y)
##        CapZombie(start_x,start_y,frame,angle)
##print ListofZombieCoords
Zombie1 = pygame.image.load("BrainZombie"+str(frame)+".png")    
while not gameExit:
    if count%75 == 0:
        frame = frame%8 + 1
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    Screen.fill(white)
    (mX,mY) = pygame.mouse.get_pos()
    angle = AngleCalc(mX,mY,x,y)
    M_change = MoveZombie(mX,mY,x,y)
    x += M_change[0]
    y += M_change[1]
    Screen.fill(white)
    BrainZombie(x-32,y-32,frame,angle)
    CapZombie(x+50,y+50,frame,angle)
##    for i in range(0,len(ListofZombieCoords)):
##        x,y = ListofZombieCoords[i][0],ListofZombieCoords[i][1]
##        angle = AngleCalc(mX,mY,x,y)
##        if i<RandomNo2:
##            M_change = MoveZombie(mX,mY,x,y)
##            x += M_change[0]
##            y += M_change[1]
##            BrainZombie(x,y,frame,angle)
##        else:
##            M_change = MoveZombie(mX,mY,x,y)
##            x += M_change[0]
##            y += M_change[1]
##            CapZombie(x,y,frame,angle)
            
    pygame.display.update()
pygame.quit()
quit()
