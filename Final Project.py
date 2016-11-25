
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
#    24/11 7:51am      24/11 9:23am
#    24/11 1:34pm      24/11 6:28pm
#    25/11 10:39pm     26/11 2:01am

#(@@@) This code was taken from http://pygame.org/wiki/RotateCenter?parent=

import pygame
import math
import random
import Tkinter
from PIL import ImageTk,Image
import ImageWriter
import tkMessageBox


#**|** The relevant code was borrowed from http://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
#Function to return the Modulus of X

def Intro_Screen():
    
    intro = True
    PassivePlay = pygame.image.load("PassivePlay.png")
    ActivePlay = pygame.image.load("ActivePlay.png")
    PassiveQuit = pygame.image.load("PassiveQuit.png")
    ActiveQuit = pygame.image.load("ActiveQuit.png")
    PassiveOptions = pygame.image.load("PassiveOpt.png")
    ActiveOptions = pygame.image.load("ActiveOpt.png")
    PassiveBack = pygame.image.load("PassiveBack.png")
    ActiveBack = pygame.image.load("ActiveBack.png")
    BackgroundFrameChanger = 1
    BackgroundFrame = 1
    StopChangingBG = False
    Black = 0,0,0
    Background = []
    Controls = False
    for i in range(51):
        Background.append(pygame.image.load("BG"+str(i+1)+".png"))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Screen.fill(Black)
        Screen.blit(Background[BackgroundFrame-1],(0,0))
        if BackgroundFrameChanger%1 == 0 and not StopChangingBG:
            BackgroundFrame += 1
        if BackgroundFrame < 51:
            BackgroundFrameChanger += 1
        else:
            StopChangingBG = True
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
            if clicked:
                Controls = True
        if 765 <= x <= 885 and 455 <= y <= 497:
            Screen.blit(ActiveQuit,(750,450))
            if clicked:
                pygame.quit()
                quit()
        if Controls:
            Screen.blit(PassiveBack,(0,0))
            if 784 < x < 896 and 555 < y < 591:
                Screen.blit(ActiveBack,(0,0))
                if clicked:
                    Controls = False
            
        pygame.display.update()
        clock.tick(15)

#Function for creating an interactive pause screen.
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

#Function to Show Reload Message!
def Message():
    font = pygame.font.SysFont("comicsanms", 64)
    text = font.render("RELOAD!!!",True,(255,0,255))
    Screen.blit(text,(400,300))

#Function to alert player of pause button
def Pause():
    font = pygame.font.SysFont("comicsanms", 20)
    text = font.render("Press Esc to Pause",True,(0,0,0))
    Screen.blit(text,(450,5))
    
#Function to laod relevant HealthBar depending on Percentage of Health
def HealthBar(Life):
    PlayerHealth = pygame.image.load("HealthPic"+str(Life)+".png")
    return PlayerHealth

#Function to initialize an instance of a type of zombie
def SummonZombie(Type,x,y,speed):
    global AllZombies
    if Type == "Blinking":
        BringToLife = SpecialZombie(x,y,speed,Type)
        BringToLife.Change()
    else:
        BringToLife = Zombie(x,y,speed,Type)  
    BringToLife.Rotate()
    #Stores this instance in a list of active zombies.
    AllZombies.append(BringToLife)

#Function to Toggle AimAssist
def AimAssistON():
    AimBot = pygame.image.load("CrossHair.png")
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
    font = pygame.font.SysFont("comicsanms,",40,bold=True)
    Bullets = font.render("Ammo: "+str(AmmoLoaded)+"/"+str(TotalAmmo),1,(0,0,0))
    Screen.blit(Bullets,(width-250,height-115))

#Number of Zombies remaining this round
def ZombiesRemaining(DeadZomble,TotalZomble):
    global Screen
    font = pygame.font.SysFont("comicsanms,",25,bold=True)
    text = font.render("Zombies Remaining: "+str(TotalZomble-DeadZomble)+"/"+str(TotalZomble),1,(243,155,57))
    Screen.blit(text,(0,0))

#Function to determin the Round No:
def RoundNumber(Round):
    global Screen
    font = pygame.font.Font("Prison Tattoo.ttf",60,bold=True)
    if Round<10:
        text = font.render("0"+str(Round),1,(232,25,78))
    else:
        text = font.render(str(Round),1,(232,25,78))
    Screen.blit(text,(880,13))
    
    
#Class for the Brain Zombie Sprite
class Zombie(pygame.sprite.Sprite):
    global Screen
    def __init__(self,x,y,speed,Type):
        pygame.sprite.Sprite.__init__(self)
        self.type = Type
        self.frame = 1
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load(str(self.type)+"Zombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.rect = self.allFrames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orgX = x
        self.orgY = y
        self.angle = 0
        self.speed = speed
        self.me = "I am roaming the screen as an undead"
        
    def move(self,Px,Py):
        global FrameCount2
        if self.type == "Brain" or self.type == "Cap":
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
        if FrameCount2%2 == 0:
            self.frame = self.frame%8 + 1
        FrameCount2 += 1

    def CheckCollide(self,Sprite1,Sprite2):
        collision = pygame.sprite.collide_rect(Sprite1,Sprite2)
        if collision:
            self.me = "Kill"

    def Rotate(self):
        if self.orgX == 0:
            for i in range(8):
                temp = self.allFrames[i]
                self.allFrames[i] = pygame.transform.rotate(temp,-90)
        if self.orgY == 0:
            for i in range(8):
                temp = self.allFrames[i]
                self.allFrames[i] = pygame.transform.rotate(temp,180)
        if self.orgX == width:
            for i in range(8):
                temp = self.allFrames[i]
                self.allFrames[i] = pygame.transform.rotate(temp,90)
            
    def update(self):
        global Screen
        Screen.blit(self.allFrames[self.frame-1],self.rect)

#Class for the Blinking Zombie Sprite
class SpecialZombie(pygame.sprite.Sprite):
    global Screen
    global width
    global height
    def __init__(self,x,y,speed,Type):
        pygame.sprite.Sprite.__init__(self)
        self.type = Type
        self.frame = 1
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("BlinkingZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.rect = self.allFrames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orgX = x
        self.orgY = y
        self.x_change = 0
        self.y_change = 0
        self.angle = 0
        self.speed = speed
        self.me = "I am roaming the screen as an undead"
        
    def Change(self):
        if self.rect.x >= width-64:
            self.x_change -= 0.75*self.speed
        if self.rect.y >= height-64:
            self.y_change -= 0.75*self.speed
        if self.rect.x <= 0:
            self.x_change += 0.75*self.speed
        if self.rect.y == 0:
            self.y_change += 0.75*self.speed

    def move(self):
        global FrameCount3
        if FrameCount3%1 == 0:
            self.frame = self.frame%8 + 1
        FrameCount3 += 1
        self.rect.x += self.x_change
        self.rect.y += self.y_change

    def CheckCollide(self,Sprite1,Sprite2):
        collision = pygame.sprite.collide_rect(Sprite1,Sprite2)
        if collision:
            self.me = "Blink"

    def Rotate(self):
        if self.orgX == 0:
            for i in range(8):
                temp = self.allFrames[i]
                self.allFrames[i] = pygame.transform.rotate(temp,-90)
        if self.orgY == 0:
            for i in range(8):
                temp = self.allFrames[i]
                self.allFrames[i] = pygame.transform.rotate(temp,180)
        if self.orgX == width:
            for i in range(8):
                temp = self.allFrames[i]
                self.allFrames[i] = pygame.transform.rotate(temp,90)
                
    def update(self):
        global Screen
        Screen.blit(self.allFrames[self.frame-1],self.rect)

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
        self.speed = 1
        self.Lives = 24
        self.Hit = 0
        self.me = None        
        
    def ChangeFrame(self):
        global FrameCount4
        if FrameCount4%10 == 0:
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
                self.y -= 4*self.speed
            if Letter == "S":
                self.y += 4*self.speed
            if Letter == "A":
                self.x -= 4*self.speed
            if Letter == "D":
                self.x += 4*self.speed

    def update(self):
        global Screen
        Screen.blit(self.allFrames[self.frame-1],(self.x,self.y))
        
    def getPlayerPos(self):
        return self.x,self.y
    
#Class to have Ammo Spawns
class DeliveryAmmo():
    def __init__(self,x,y):
        self.frame = 1
        self.allFrames = []
        for i in range(11):
            AmmoFrame = pygame.image.load("BulletPower"+str(self.frame+i)+".png")
            self.allFrames.append(AmmoFrame)
        self.rect = self.allFrames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        global Screen
        global FrameCount4
        if FrameCount4%2 == 0:
            self.frame = self.frame%11 + 1
        FrameCount4 += 1
        Screen.blit(self.allFrames[self.frame-1],self.rect)

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
clock = pygame.time.Clock()

#Initialize all the necessary images
Ammo = pygame.image.load("AmmoCheck.png")

#Creating Boundary Coordinates and Storing them in a list.
ListofBoundaryCoords = []
for i in range(width):
    ListofBoundaryCoords += [(i,0)]
##for i in range(width):
##    ListofBoundaryCoords += [(i,height)]
for i in range(height):
    ListofBoundaryCoords += [(0,i)]
for i in range(height):
    ListofBoundaryCoords += [(width,i)]
ListofBoundaryCoords.remove((0,0))

ListofNumbers = []
for i in range(0,1000):
    ListofNumbers += [i+1]
 
def Game_loop():

    #Initializing the necessary variables for the game.
    BackGround1 = pygame.image.load("BG.png")
    ReloadOccurence = 0
    AmmoPowerUpList = []
    DecidingAmount = 350
    SpeedCap = 24
    SpeedBrain = 14
    SpeedBlinking = 50
    AimAssistCount = 1
    Score = 0
    AmmoLoaded = 45
    AmmoInMag = 190
    DeadZombies = 0
    TotalZombies = 5
    RoundNo = 1
    MoveTime = 0
    Player1.Lives = 24
    ChallengeControl = 50
    DecidingAmmount = 350
    NewZombieCount = -40
    Threshold = 50
    SpawnTime = 0
    IsAimAssist = False
    ShowMessage = False
    GiveAmmo = False
    Wave = False
    gameExit = False
    OnceNotOver = True
    
    #Main game while loop.
    while not gameExit:
        ListofXCoords = []   
        ListofYCoords = []
        
        #Event LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if AmmoLoaded >0:
                    P1x,P1y = Player1.getPlayerPos()
                    (mX,mY) = pygame.mouse.get_pos()
                    ZombieKiller = Bullet(50,P1x,P1y,mX,mY)
                    ZombieKiller.Change()
                    AllBullets.append(ZombieKiller)
                    AmmoLoaded -= 1
                    
        Screen.blit(BackGround1,(0,0))
     
        #Random New Zombie Spawner Condition
        if NewZombieCount%ChallengeControl == 0 and NewZombieCount != 0:
            RandomNo2 = random.randint(1,len(ListofBoundaryCoords))
            (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
            Decider = random.choice(ListofNumbers)
            if DecidingAmount < Decider <= 1000:
                SummonZombie("Brain",x,y,SpeedBrain)
            elif Threshold < Decider <= DecidingAmount: 
                SummonZombie("Cap",x,y,SpeedCap)
            else:
                SummonZombie("Blinking",x,y,SpeedBlinking)
        NewZombieCount += 1

        if Wave:
            for i in range(RoundNo + 5):
                RandomNo2 = random.randint(1,len(ListofBoundaryCoords))
                (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
                SummonZombie("Brain",x,y,SpeedBrain)
            Wave = False
                
        #Zombie LOOP
        for Zomb in AllZombies:
            P1x,P1y = Player1.getPlayerPos()
            if MoveTime%1 == 0:
                if Zomb.type == "Blinking":
                    Zomb.move()
                else:
                    Zomb.move(P1x,P1y)
            Zomb.update()


        #Bullets LOOP
        for Bullets in AllBullets:
            Bullets.Attack()
            for Zomb in AllZombies:
                Zomb.me = "Meh!"
                Bullets.CheckCollide(Bullets,Zomb)
                if Bullets.me == "Kill":
                    if Bullets in AllBullets:
                        AllBullets.remove(Bullets)
                    if Zomb in AllZombies:
                        if Zomb.type == "Blinking":
                            Player1.Lives = 24
                        AllZombies.remove(Zomb)
                    Score += 10
                    DeadZombies += 1   
            if Bullets.rect.x>1000 or Bullets.rect.x<0-29 or Bullets.rect.y>650 or Bullets.rect.y<0-29:
                if Bullets in AllBullets:
                    AllBullets.remove(Bullets)
            Bullets.update()
    
        MoveTime += 1

      #Handling Pressed Keys    
        KeysPressed = pygame.key.get_pressed()
        if KeysPressed[pygame.K_TAB]:
            print AimAssistCount
            AimAssistCount += 1
        
        if AimAssistCount%3 == 0:
            Aim = AimAssistON()
            x,y = Player1.getPlayerPos()
            (mX,mY) = pygame.mouse.get_pos()
            Screen.blit(Aim,(mX-16,mY-16))
            pygame.draw.line(Screen,(0,0,255),(x+32,y+32),(mX,mY))
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
        #Functionality for the reloading the ammo.
        if KeysPressed[pygame.K_r]:
            if AmmoLoaded<45:
                if AmmoLoaded == 0:
                    if AmmoInMag >= 45:
                        AmmoInMag -= 45
                        AmmoLoaded += 45
                    elif AmmoInMag == 0:
                        OutOfAmmo()
                    else:
                        AmmoLoaded = AmmoInMag
                        AmmoInMag = 0
                else:
                    if AmmoInMag >= 45:
                        AddedAmmo = 45 - AmmoLoaded
                        AmmoLoaded += AddedAmmo
                        AmmoInMag -= AddedAmmo
                    elif AmmoInMag == 0:
                        AmmoLoaded = AmmoLoaded
                    else:
                        if AmmoLoaded + AmmoInMag <= 45:
                            AmmoLoaded += AmmoInMag
                            AmmoInMag = 0
                        else:
                            RequiredAmmo = 45 - AmmoLoaded
                            AmmoInMag -= RequiredAmmo
                            AmmoLoaded += RequiredAmmo
                
        #Ammo Spawner
        if RoundNo >= 10 and OnceNotOver: 
            if RoundNo%2 == 0:
                GiveAmmo = True
                OnceNotOver = False
            else:
                OnceNotOver = False

        if GiveAmmo:
            x = random.randint(200,800)
            y = random.randint(60,550)
            AmmoPowerUp = DeliveryAmmo(x,y)
            AmmoPowerUpList.append(AmmoPowerUp)
            GiveAmmo = False

        for Replenish in AmmoPowerUpList:
            if len(AmmoPowerUpList) > 0:
                Collide = False
                Px,Py = Player1.x + 13,Player1.y + 7
                zX,zY = Replenish.rect.x,Replenish.rect.y
                Apx,Apy = 38,50
                Azx,Azy = 32,32
                if zX < Px + Apx and zY + Azy > Py and zX + Azx > Px + Apx and zY > Py:
                    Collide = True
                if zX + Azx > Px and zY + Azy > Py and zX < Px and zY < Py:
                    Collide = True
                if zX + Azx > Px and zY < Py + Apy and zX < Px and zY + Azy > Py + Apy:
                    Collide = True
                if zX < Px + Apx and zY < Py + Apy and zX + Azx > Px + Apx and zY + Azy > Py + Apy:
                    Collide = True
                if Collide == True:
                    AmmoInMag = 250
                    AmmoPowerUpList.remove(Replenish)
                SpawnTime += 1
                if SpawnTime > 500:
                    AmmoPowerUpList.remove(Replenish)
                    SpawnTime = 0
                Replenish.update()    
            
        #Player1 Update Haandler
        Player1.ChangeFrame()
        for Zomb in AllZombies:
            Zomb.me = "Meh!"
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
                    if Zomb.type != "Blinking":
                        if Zomb.type == "Cap":
                            Player1.Lives -= 3
                        else:
                            Player1.Lives -= 1
                        AllZombies.remove(Zomb)
        if Player1.Lives == 0:
            gameExit = True
            Dead_Screen(RoundNo)
            
        Player1.update()
        
         
        #Health Bar Handler
        if Player1.Lives < 0:
            Player1.Lives = 0
        Screen.blit(HealthBar(Player1.Lives),(width-400,height-100))

        #Ammo Check Handler
        AmmoRemaining(AmmoLoaded,AmmoInMag)

        #Reload Message
        if AmmoLoaded == 0:
            if ReloadOccurence%10 == 0:
                ShowMessage = not ShowMessage
            ReloadOccurence += 1
            if ShowMessage == True:
                Message()
                            
        #Score Handler
        Points(Score)

        #To Blit Pause Helper
        Pause()
        
        #RemainingZombies
        ZombiesRemaining(DeadZombies,TotalZombies)

        #Round Number Handler
        RoundNumber(RoundNo)

        if DeadZombies >= TotalZombies:
            NewZombieCount = -40
            RoundNo += 1
            OnceNotOver = True
            if RoundNo%5 == 0:
                Wave = True
            
            DeadZombies = 0
            TotalZombies += 5
            if ChallengeControl >20:
                ChallengeControl -= 4
            if DecidingAmmount <750:
                DecidingAmmount += 10
            if Threshold > 10:
                Threshold -= 4
        pygame.display.update()
        clock.tick(60)
        
Intro_Screen()
Game_loop()
pygame.quit()
quit()















    
