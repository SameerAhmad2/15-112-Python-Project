import pygame
import ImageWriter
import math

##class BrainZombie(pygame.sprite.Sprite):
##    def __init__(self,frame):
##        self.imagedisp = 1
##    def loadFrame(self,frame)        
##        self.imagedisp =

pygame.init()
width,height = 900,600
white = 255,255,255
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ZomBusters: The Realm Of The Dead")
x,y =(width/2 - 32),(height/2 - 32)
screen.fill(white)
x_change = 0.5
y_change = 0.75
##x_Dist = x_Cursor - x
gameExit = False
frame = 1
ZombieWidth = 64
y2 = y + 100
def Rotate(Img,angle):
    pygame.transform.rotate(Img,angle)

def Zombie(x,y,frame,angle):
    ZombieImg1 = pygame.image.load("BrainZombie"+str(frame)+".png")
##    ZombieImg2 = pygame.image.load("CapZombie"+str(frame)+".png")
    ZombieImg1Rot = pygame.transform.rotate(ZombieImg1,angle)
##    ZombieImg2Rot = pygame.transform.rotate(ZombieImg2,angle)
    screen.blit(ZombieImg1Rot,(x,y))
##    screen.blit(ZombieImg2Rot,(x,y2))
count = 0
angle = -90
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEMOTION:
            x_Cursor,y_Cursor = pygame.mouse.get_pos()
            cursorAngle = math.atan2(y_Cursor,x_Cursor)
            imageAngle = math.atan2(y+32,x+32)
            DiffAngle =cursorAngle-imageAngle
            CursorMagnitude = math.sqrt((x_Cursor**2) + (y_Cursor**2))
            RelativeMagnitude = math.sqrt(((x_Cursor**2)-((x+32)**2)) + ((y_Cursor**2)-((y+32)**2)))
            Angle1 = math.asin((CursorMagnitude/RelativeMagnitude)*math.sin(DiffAngle))
            RadRotAngle = Angle1 + DiffAngle - math.pi/2
            DegRotAngle = math.degrees(RadRotAngle)
            screen.fill(white)
            Zombie(x,y,frame,-DegRotAngle)
            angle = DegRotAngle
        else:
            screen.fill(white)
            Zombie(x,y,frame,angle)
##    screen.fill(white)
##    x = x%width
##    y = y%width
##    Zombie(x,y,frame,angle)
##    x += x_change
##    y += y_change
    if count%50 == 0:
        frame = frame%8 + 1
    pygame.display.update()
    count += 1
    if x >(width-ZombieWidth):
        x_change = -(x_change)
        angle = 90
    if x<0:
        x_change = -(x_change)
        angle = -90
    print frame
pygame.quit()
quit()
#Function to switch between fullscreen mode   (pygame.display.toggle_fullscreen())
