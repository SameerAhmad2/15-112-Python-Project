
#    15-112: Principles of Programming and Computer Science
#    Final Project: Zombusters: The Realm Of The Dead
#    Name      : Sameer Ahmad
#    AndrewID  : sjahmad

#    File Created: November 3, 4:56pm
#    Modification History:
#    Start             End
#    04/11 1:30pm      04/11 4:14pm
#    04/11 9:45pm      05/11 12:23am
#    05/11 5:00pm      05/11 7:31pm
#    08/11 4:30pm      08/11 9:07pm
#    09/11 8:32pm      09/11 11:20pm
#    10/11 11:23pm     10/11 2:43am
#    11/11 3:39pm      11/11 7:32pm
#    11/11 8:45pm      11/11 10:05pm
#    12/11 2:34pm      12/11 5:12pm
#    13/11 5:18pm      13/11 7:07pm
#    13/11 9:56pm      14/11 12:15am
#    14/11 1:23pm      14/11 2:53pm
#    19/11 5:37pm      19/11 7:03pm
#    20/11 2:52pm      20/11 3:44pm
#    20/11 6:18pm      20/11 9:35pm
#    21/11 6:21am      21/11 9:45am
#    21/11 11:21am     21/11 12:17pm
#    21/11 6:30pm      21/11 11:13pm
#    22/11 6:17pm      22/11 8:12pm
#    22/11 9:56pm      23/11 1:27am
#    23/11 8:48am      23/11 11:54am
#    23/11 7:12pm      23/11 11:43pm

#(@@@) This code was taken from http://pygame.org/wiki/RotateCenter?parent=

import pygame
import math
import random
import Tkinter
from PIL import ImageTk,Image
import ImageWriter
import Login
import tkMessageBox


#**|** The relevant code was borrowed from http://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
#Function to return the Modulus of X

##def PlayScreen(Entry):
##    global wnd          
##    global UsernameStr
##    global PasswordStr
##    global socket
##    ItWorked = Login.login(socket,str(UsernameStr.get()),str(PasswordStr.get()))
##    if ItWorked:
##        initMenu()
##    else:
##        tkMessageBox.showinfo(title="Telepathic Trafficking",message="The dead have stopped you from entering their dimension... Try Again")
####        Entry[0].delete('1.0',"end")
####        Entry[1].delete('1.0',"end")

#Start Screen
def Intro_Screen():
    
    intro = True
    Background = pygame.image.load("ZombieBG.jpg")
    PassivePlay = pygame.image.load("PassivePlay.png")
    ActivePlay = pygame.image.load("ActivePlay.png")
    PassiveQuit = pygame.image.load("PassiveQuit.png")
    ActiveQuit = pygame.image.load("ActiveQuit.png")
    PassiveOptions = pygame.image.load("PassiveOpt.png")
    ActiveOptions = pygame.image.load("ActiveOpt.png")
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Screen.fill(white)
        Screen.blit(Background,(0,0))
        Screen.blit(PassivePlay,(100,450))
        Screen.blit(PassiveOptions,(400,450))
        Screen.blit(PassiveQuit,(750,450))
        (x,y) = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if 120 <= x <= 230 and 455 <= y <= 495:
            Screen.blit(ActivePlay,(100,450))
            if clicked:
                intro = False
        if 405 <= x <= 593 and 455 <= y <= 499:
            Screen.blit(ActiveOptions,(400,450))
        if 765 <= x <= 885 and 455 <= y <= 497:
            Screen.blit(ActiveQuit,(750,450))
            if clicked:
                pygame.quit()
                quit()
                
        pygame.display.update()
        clock.tick(15)

def Pause_Screen():
    PauseScreen = pygame.image.load("StartPause.png")
    Resume = pygame.image.load("ToResume.png")
    Restart = pygame.image.load("RestartButton.png")
    Exit = pygame.image.load("ExitButton.png")
    PlayerFrames = []
    frame = 1
    for i in range(4):
        PlayerFrames.append(pygame.image.load("Player"+str(frame+i)+"Big.png"))
        
    CountForMovingSoldier = 0
    isPaused = True
    while isPaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Screen.blit(PauseScreen,(0,0))
        (x,y) = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if 104 <= x <= 277 and 246 <= y <= 273:
            Screen.blit(Resume,(0,0))
            if CountForMovingSoldier%5 == 0:
                frame = frame%4 + 1
            Screen.blit(PlayerFrames[frame-1],(640,420))
            if clicked:
                isPaused = False
        if 107 <= x <= 285 and 323 <= y <= 349:
            Screen.blit(Restart,(0,0))
            if clicked:
                isPaused = False
                Game_loop()
        if 109 <= x <= 209 and 399 <= y <= 424:
            Screen.blit(Exit,(0,0))
            if clicked:
                pygame.quit()
                quit()

        pygame.display.update()
    
    
def Dead_Screen(RoundNo):
    global Score
    Dead = True
    BackgroundChanger = 1
    CounttoDisplayChoices = 0
    CounttoDisplayRounds = 0
    NewGame = pygame.image.load("SelectNewGame.png")
    Leave = pygame.image.load("SelectExit.png")
    font = pygame.font.Font("Prison Tattoo.ttf",24)
    text = font.render("Survived "+str(RoundNo)+" Round(s)",1,(205,0,0))
    while Dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        BG = pygame.image.load("Dead"+str(BackgroundChanger)+".png")
        Screen.blit(BG,(0,0))
        if BackgroundChanger < 30:
            BackgroundChanger += 1
        if CounttoDisplayChoices == 50:
            if BackgroundChanger != 38:
                BackgroundChanger += 1
        else:
            CounttoDisplayChoices += 1

        (mX,mY) = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if 225 <= mX <= 400 and 525 <= mY <= 580:
            Screen.blit(NewGame,(0,0))
            if clicked:
                Dead = False
                Game_loop()
        if 570 <= mX <= 750 and 520 <= mY <= 585:
            Screen.blit(Leave,(0,0))
            if clicked:
                pygame.quit()
                quit()
        
        if CounttoDisplayRounds >70:
            Screen.blit(text,(370,610))        
        
        CounttoDisplayRounds += 1         
        pygame.display.update()

#Function to Rotate Image from its center. (@@@)
def Rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

#Function to laod relevant HealthBar depending on Percentage of Health
def HealthBar(Percentage):
    PlayerHealth = pygame.image.load(str(Percentage)+"%.png")
    return PlayerHealth

#Function to load Brain Zombie Image
def loadBZombieImg(frame):
    return pygame.image.load("BrainZombie"+str(frame)+".png")

#Function to load Cap Zombie Image
def loadCZombieImg(frame):
    return pygame.image.load("CapZombie"+str(frame)+".png")

#Function to add all the positions border positions to a list for random calling
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

#Function to initialize an instance of a type of zombie
def SummonZombie(Type,x,y,speed):
    global AllZombies
    global angle
    if Type == "Brain":
        Zombie = BrainZombie(x,y,speed)
    elif Type == "Cap":
        Zombie = CapZombie(x,y,angle)
        
    #Stores this instance in a list of active zombies.
    AllZombies.append(Zombie)

#Function to Toggle AimAssist
def AimAssistON():
    AimBot = pygame.image.load("AimAssist.png")
    return AimBot

#Function to handle Player Points
def Points(count):
    global Screen
    font = pygame.font.SysFont("comicsanms",25,bold=True)
    text = font.render("Score: "+str(count),1,(0,0,0))
    Screen.blit(text,(0,25))

#Function to display ammo remaining on the screen
def AmmoRemaining(AmmoLoaded,TotalAmmo):
    global Screen
    font = pygame.font.SysFont("comicsanms,",18,bold=True)
    Bullets = font.render(str(AmmoLoaded)+"/"+str(TotalAmmo),1,(0,0,0))
    Screen.blit(Bullets,(width-165,height-55))

#Number of Zombies remaining this round
def ZombiesRemaining(DeadZomble,TotalZomble):
    global Screen
    font = pygame.font.SysFont("comicsanms,",25,bold=True)
    text = font.render("Zombies Remaining: "+str(TotalZomble-DeadZomble)+"/"+str(TotalZomble),1,(243,155,57))
    Screen.blit(text,(0,0))

#Function to determin the Round No:
def RoundNumber(Round):
    global Screen
    font = pygame.font.SysFont("Prison Tattoo.ttf",50,bold=True)
    text = font.render(str(Round),1,(232,25,78))
    Screen.blit(text,(950,0))
    
    
#Class for the Brain Zombie Sprite
class BrainZombie(pygame.sprite.Sprite):
    global Screen
    def __init__(self,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 1
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("BrainZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.rect = self.allFrames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = 0
        self.speed = speed
        self.me = "I am roaming the screen as an undead"
        
    def move(self,Px,Py):
        global FrameCount2
        dx = self.rect.x - Px
        dy = self.rect.y - Py
        if self.rect.x>=Px and self.rect.y<Py:
            if self.rect.x == Px:
                self.angle = 0
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<Px and self.rect.y<=Py:
            if self.rect.y == Py:
                self.angle = -math.pi/2
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<=Px and self.rect.y>Py:
            if self.rect.x == Px:
                self.angle = math.pi
            else:
                self.angle = -(-math.atan2(float(dy),dx) + 3*(math.pi)/2)
        elif self.rect.x>Px and self.rect.y>=Py:
            if self.rect.y == Py:
                self.angle = math.pi/2
            else:
                self.angle = -(math.atan2(float(dx),dy)) + math.pi 
        self.rect.x -= math.sin(self.angle)*self.speed
        self.rect.y += math.cos(self.angle)*self.speed
        
        if FrameCount2%7 == 0:
            self.frame = self.frame%8 + 1
        FrameCount2 += 1

    def CheckCollide(self,Sprite1,Sprite2):
        collision = pygame.sprite.collide_rect(Sprite1,Sprite2)
        if collision:
            self.me = "Kill"
            
    def update(self):
        global Screen
        Screen.blit(self.allFrames[self.frame-1],self.rect)

#Class for the Cap Zombie Sprite
class CapZombie(pygame.sprite.Sprite):
    global Screen
    def __init__(self,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 1
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("BrainZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.rect = self.allFrames[0].get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.angle = 0
        self.me = "Meh!"
        
    def move(self,Px,Py):
        global FrameCount3
        dx = self.rect.x - Px
        dy = self.rect.y - Py
        if self.rect.x>=Px and self.rect.y<Py:
            if self.rect.x == Px:
                self.angle = 0
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<Px and self.rect.y<=Py:
            if self.rect.y == Py:
                self.angle = -math.pi/2
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<=Px and self.rect.y>Py:
            if self.rect.x == Px:
                self.angle = math.pi
            else:
                self.angle = -(-math.atan2(float(dy),dx) + 3*(math.pi)/2)
        elif self.rect.x>Px and self.rect.y>=Py:
            if self.rect.y == Py:
                self.angle = math.pi/2
            else:
                self.angle = -(math.atan2(float(dx),dy)) + math.pi 
        self.rect.x -= math.sin(self.angle)*self.speed
        self.rect.y += math.cos(self.angle)*self.speed
        if FrameCount3%7 == 0:
            self.frame = self.frame%8 + 1
        FrameCount3 += 1

    def CheckCollide(self,Sprite1,Sprite2):
        collision = pygame.sprite.collide_rect(Sprite1,Sprite2)
        if collision:
            self.me = "Kill"

    def update(self):
        global Screen
        Screen.blit(self.allFrames[self.frame-1],(self.rect.x,self.rect.y))

#Class for the Blinking Zombie Sprite
##class BlinkingZombie(pygame.sprite.Sprite):
##    global Screen
##    def __init__(self,x,y,angle):
##        pygame.sprite.Sprite.__init__(self)
##        self.frame = 1
##        self.x_pos = x
##        self.y_pos = y
##        self.angle = angle
##        self.allFrames = []
##        for i in range(8):
##            ZombieFrame = pygame.image.load("BlinkingZombie"+str(self.frame+i)+".png")
##            self.allFrames.append(ZombieFrame)
##        self.me = None
##        
##    def move(self,mX,mY):
##        global FrameCount3
##        x_Dist = mX - self.x_pos
##        y_Dist = mY - self.y_pos
##        x_change = x_Dist/float(300)
##        y_change = y_Dist/float(300)
##        self.x_pos += x_change
##        self.y_pos += y_change
##        if FrameCount3%5 == 0:
##            self.frame = self.frame%8 + 1
##        FrameCount3 += 1
##        
##    def rotate(self,mX,mY):
##        Img = self.allFrames[self.frame - 1]
##        NewImg = Rotate(Img,self.x_pos,self.y_pos)
##        self.allFrames[self.frame - 1] = NewImg
##        
##    def update(self):
##        global Screen
##        if self.me != None:
##            self.me = "Alive"
##        Screen.blit(self.allFrames[self.frame-1],(self.x_pos,self.y_pos))


#Class for the Player Sprite (That means YOU)       
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 1
        self.allFrames = []
        for i in range(4):
            PlayerFrame = pygame.image.load("Player"+str(self.frame+i)+".png")
            self.allFrames.append(PlayerFrame)
        self.rect = self.allFrames[0].get_rect()
        self.x = x
        self.y = y
        self.lives = 10
        self.Hit = 0
        self.me = None        
        
    def ChangeFrame(self):
        global FrameCount4
        if FrameCount4%20 == 0:
            self.frame = self.frame%4 + 1
        FrameCount4 += 1

    def Move(self,Letter):
        if self.x<0:
            self.x = 0
        if self.x > width-64:
            self.x = width-64
        if self.y<0:
            self.y = 0
        if self.y>height-64:
            self.y = height-64
        else:
            if Letter == "W":
                self.y -= 2
            if Letter == "S":
                self.y += 2
            if Letter == "A":
                self.x -= 2
            if Letter == "D":
                self.x += 2

    def Rotate(self,mX,mY):
        dx = self.rect.x - mX
        dy = self.rect.y - mY
        if self.rect.x>=mX and self.rect.y<mY:
            if self.rect.x == mX:
                self.angle = 0
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<mX and self.rect.y<=mY:
            if self.rect.y == mY:
                self.angle = -math.pi/2
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<=mX and self.rect.y>mY:
            if self.rect.x == mX:
                self.angle = math.pi
            else:
                self.angle = -(-math.atan2(float(dy),dx) + 3*(math.pi)/2)
        elif self.rect.x>mX and self.rect.y>=mY:
            if self.rect.y == mY:
                self.angle = math.pi/2
            else:
                self.angle = -(math.atan2(float(dx),dy)) + math.pi
        for i in range(4):
            Blit_image = Rot_center(self.allFrames[i],self.angle)
            self.allFrames[i] = Blit_image            
        
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],(self.x,self.y))
        

    def getPlayerPos(self):
        return self.x,self.y

#Class to fire a Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self,speed,P1x,P1y,MouseX,MouseY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Small Bullet.png")
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = P1x
        self.rect.y = P1y
        self.mX = MouseX
        self.mY = MouseY
        self.x_change = 0
        self.y_change = 0
        self.me = "Time to Kill a Zombie"
        
    def Change(self):
        dx = self.rect.x - self.mX
        dy = self.rect.y - self.mY
        if self.rect.x>=self.mX and self.rect.y<self.mY:
            if self.rect.x == self.mX:
                self.angle = 0
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<self.mX and self.rect.y<=self.mY:
            if self.rect.y == self.mY:
                self.angle = -math.pi/2
            else:
                self.angle = math.atan2(float(dy),dx) + math.pi/2
        elif self.rect.x<=self.mX and self.rect.y>self.mY:
            if self.rect.x == self.mX:
                self.angle = math.pi
            else:
                self.angle = -(-math.atan2(float(dy),dx) + 3*(math.pi)/2)
        elif self.rect.x>self.mX and self.rect.y>=self.mY:
            if self.rect.y == self.mY:
                self.angle = math.pi/2
            else:
                self.angle = -(math.atan2(float(dx),dy)) + math.pi
        self.x_change = math.sin(self.angle)*self.speed
        self.y_change = math.cos(self.angle)*self.speed

    def CheckCollide(self,Sprite1,Sprite2):
        collision = pygame.sprite.collide_rect(Sprite1,Sprite2)
        if collision:
            self.me = "Kill"

    def Attack(self):
        self.rect.x -= self.x_change
        self.rect.y += self.y_change
    
    def update(self):
        global Screen
        Screen.blit(self.image,(self.rect.x,self.rect.y))

#Initialize pygame and set up display
pygame.init()
width,height = 1000,650
Screen = pygame.display.set_mode((width,height))

#Initializing all the necessary variables

white = 255,255,255
AllZombies = []
AllBullets = []
FrameCount1 = 0
FrameCount2 = 0
FrameCount3 = 0
FrameCount4 = 0
gameExit = False
x_change = 0
y_change = 0
mX , mY = 0 , 0
RandomNo1 = random.randint(4,15)
Player1 = Player(width/2-32,height/2-32)
angle = -90
speed = 5
TotalZombies = 5
clock = pygame.time.Clock()

#Initialize all the necessary images
Ammo = pygame.image.load("AmmoCheck.png")

#Creating Boundary Coordinates and Storing them in a list.
ListofBoundaryCoords = []
for i in range(width):
    ListofBoundaryCoords += [(i,0)]
for i in range(width,width):
    ListofBoundaryCoords += [(i,height)]
for i in range(height):
    ListofBoundaryCoords += [(0,i)]
for i in range(height,height):
    ListofBoundaryCoords += [(width,i)]

ListofNumbers = []
for i in range(100):
    ListofNumbers += [i+1]
 
def Game_loop():
    global speed
    global MoveTime
    AimAssistCount = 0
    Score = 0
    DeadZombies = 0
    TotalZombies = 5
    RoundNo = 1
    MoveTime = 0
    ChallengeControl = 100
    Percentage = 100
    DecidingAmmount = 25
    NewZombieCount = -40
    
    gameExit = False
    #Main game while loop.
    while not gameExit:
        ListofXCoords = []   
        ListofYCoords = []
        
        #Event LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                P1x,P1y = Player1.getPlayerPos()
                (mX,mY) = pygame.mouse.get_pos()
                ZombieKiller = Bullet(10,P1x,P1y,mX,mY)
                ZombieKiller.Change()
                AllBullets.append(ZombieKiller)

        Screen.fill(white)

        #Random New Zombie Spawner Condition
        if NewZombieCount%ChallengeControl == 0 and NewZombieCount != 0:
            RandomNo2 = random.randint(1,len(ListofBoundaryCoords))
            (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
            Decider = random.choice(ListofNumbers)
            if Decider < DecidingAmmount:
                SummonZombie("Cap",x,y,speed)
            else: 
                SummonZombie("Brain",x,y,speed)
        NewZombieCount += 1
        

        #Bullets LOOP
        for Bullets in AllBullets:
            Bullets.Attack()
            for Zomb in AllZombies:
                Bullets.CheckCollide(Bullets,Zomb)
                if Bullets.me == "Kill":
                    if Bullets in AllBullets:
                        AllBullets.remove(Bullets)
                    if Zomb in AllZombies:
                        AllZombies.remove(Zomb)
                    Score += 10
                    DeadZombies += 1
                
            if Bullets.rect.x>1000 or Bullets.rect.x<0-29 or Bullets.rect.y>650 or Bullets.rect.y<0-29:
                AllBullets.remove(Bullets)
            Bullets.update()
    
        
        #Zombie LOOP
        for Zomb in AllZombies:
            P1x,P1y = Player1.getPlayerPos()
            if MoveTime%3 == 0:
                Zomb.move(P1x,P1y)                    
            Zomb.update()

        MoveTime += 1

      #Handling Pressed Keys    
        KeysPressed = pygame.key.get_pressed()
        if KeysPressed[pygame.K_TAB]:
            AimAssistCount += 1
        if AimAssistCount%2 == 1:
            Aim = AimAssistON()
            (mX,mY) = pygame.mouse.get_pos()
            Screen.blit(Aim,(mX-10,mY-10))
        KeysPressed = pygame.key.get_pressed()
        if KeysPressed[pygame.K_w]:
            Player1.Move("W")
        if KeysPressed[pygame.K_s]:
            Player1.Move("S")
        if KeysPressed[pygame.K_a]:
            Player1.Move("A")
        if KeysPressed[pygame.K_d]:
            Player1.Move("D")
        if KeysPressed[pygame.K_ESCAPE]:
            Pause_Screen()
                
        #Player1 Update Haandler
        Player1.ChangeFrame()
        for Zomb in AllZombies:
            Collide = False
            Px,Py = Player1.x + 13,Player1.y + 7
            zX,zY = Zomb.rect.x + 5,Zomb.rect.y + 3
            Azx,Azy = 54,58
            Apx,Apy = 38,50
            if zX < Px + Apx and zY + Azy > Py and zX + Azx > Px + Apx and zY > Py:
                Collide = True
            if zX + Azx > Px and zY + Azy > Py and zX < Px and zY < Py:
                Collide = True
            if zX + Azx > Px and zY < Py + Apy and zX < Px and zY + Azy > Py + Apy:
                Collide = True
            if zX < Px + Apx and zY < Py + Apy and zX + Azx > Px + Apx and zY + Azy > Py + Apy:
                Collide = True
            if Collide == True:
                if Zomb in AllZombies:
                    AllZombies.remove(Zomb)
                Percentage -= 10
        if Percentage == 0:
            Dead_Screen(RoundNo)
        (mX,mY) = pygame.mouse.get_pos()
        Player1.Rotate(mX,mY)
        Player1.update()
        
         
        #Health Bar Handler
        Screen.blit(HealthBar(Percentage),(width-210,height-140))

        #Ammo Check Handler
        Screen.blit(Ammo,(width-100,height-66))
        
        AmmoRemaining(100,1000)

        #Score Handler
        Points(Score)

        #RemainingZombies
        ZombiesRemaining(DeadZombies,TotalZombies)

        #Round Number Handler
        RoundNumber(RoundNo)

        if DeadZombies == TotalZombies:
            RoundNo += 1
            DeadZombies = 0
            TotalZombies += 5
            ChallengeControl -= 2
            if DecidingAmmount <75:
                DecidingAmmount += 5
        pygame.display.update()
        clock.tick(60)
        
Intro_Screen()
Game_loop()
pygame.quit()
quit()















    
