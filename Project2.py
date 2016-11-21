
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
#    21/11 11:21am

 
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

def PlayScreen(Entry):
    global wnd          
    global UsernameStr
    global PasswordStr
    global socket
    ItWorked = Login.login(socket,str(UsernameStr.get()),str(PasswordStr.get()))
    if ItWorked:
        initMenu()
    else:
        tkMessageBox.showinfo(title="Telepathic Trafficking",message="The dead have stopped you from entering their dimension... Try Again")
##        Entry[0].delete('1.0',"end")
##        Entry[1].delete('1.0',"end")

def Modulus(x):
    if x<0:
        x = -x
    return x

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
def SummonZombie(Type,x,y):
    global AllZombies
    global angle
    if Type == "Brain":
        Zombie = BrainZombie(x,y,angle)
    elif Type == "Cap":
        Zombie = CapZombie(x,y,angle)
        
    #Stores this instance in a list of active zombies.
    AllZombies.append(Zombie)

#Function to rotate Zombie Image (Currently not Working =P)
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

#Function to Toggle AimAssist
def AimAssistON():
    AimBot = pygame.image.load("AimAssist.png")
    return AimBot


#Class for the Brain Zombie Sprite
class BrainZombie(pygame.sprite.Sprite):
    global Screen
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 1
        self.allFrames = []
        for i in range(8):
            ZombieFrame = pygame.image.load("BrainZombie"+str(self.frame+i)+".png")
            self.allFrames.append(ZombieFrame)
        self.rect = self.allFrames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.me = None
        
    def move(self,mX,mY):
        global FrameCount1
        x_Dist = mX - self.rect.x
        y_Dist = mY - self.rect.y
        x_change = x_Dist/float(300)
        y_change = y_Dist/float(300)
        self.rect.x += x_change
        self.rect.y += y_change
        if FrameCount1%5 == 0:
            self.frame = self.frame%8 + 1
        FrameCount1 += 1
        
##    def rotate(self,mX,mY):
##        Img = self.allFrames[self.frame - 1]
##        NewImg = Rotate(Img,self.x_pos,self.y_pos)
##        self.allFrames[self.frame - 1] = NewImg
        
    def update(self):
        global Screen
        Screen.blit(self.allFrames[self.frame-1],self.rect)

            
#Class for the Cap Zombie Sprite
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
        global FrameCount2
        x_Dist = mX - self.x_pos
        y_Dist = mY - self.y_pos
        x_change = x_Dist/float(50)
        y_change = y_Dist/float(50)
        self.x_pos += x_change
        self.y_pos += y_change
        if FrameCount2%5 == 0:
            self.frame = self.frame%8 + 1
        FrameCount2 += 1
        
    def rotate(self,mX,mY):
        Img = self.allFrames[self.frame - 1]
        NewImg = Rotate(Img,self.x_pos,self.y_pos)
        self.allFrames[self.frame - 1] = NewImg
        
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],(self.x_pos,self.y_pos))

#Class for the Blinking Zombie Sprite
class BlinkingZombie(pygame.sprite.Sprite):
    global Screen
    def __init__(self,x,y,angle):
        pygame.sprite.Sprite.__init__(self)
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
        global FrameCount3
        x_Dist = mX - self.x_pos
        y_Dist = mY - self.y_pos
        x_change = x_Dist/float(300)
        y_change = y_Dist/float(300)
        self.x_pos += x_change
        self.y_pos += y_change
        if FrameCount3%5 == 0:
            self.frame = self.frame%8 + 1
        FrameCount3 += 1
        
    def rotate(self,mX,mY):
        Img = self.allFrames[self.frame - 1]
        NewImg = Rotate(Img,self.x_pos,self.y_pos)
        self.allFrames[self.frame - 1] = NewImg
        
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],(self.x_pos,self.y_pos))

#Class for the Player Sprite (That means YOU)       
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 1
        self.allFrames = []
        for i in range(3):
            PlayerFrame = pygame.image.load("Player"+str(self.frame+i)+".png")
            self.allFrames.append(PlayerFrame)
        self.rect = self.allFrames[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.me = None        
        
    def ChangeFrame(self):
        global FrameCount4
        if FrameCount4%20 == 0:
            self.frame = self.frame%3 + 1
        FrameCount4 += 1

    def Move(self,Letter):
        (mX,mY) = pygame.mouse.get_pos()
        ModDist = math.sqrt((self.rect.x-mX)**2 + (self.rect.x-mY)**2)
        Vect1 = (1,0)
        Vect2 = (mX-self.rect.x,mY-self.rect.y)
        Angle = math.acos((Vect1[0]*Vect2[0] + Vect1[1]*Vect2[1])/(math.sqrt((mX-self.rect.x)**2 + (mY-self.rect.y)**2)))
        DegAngle = math.degrees(Angle)
        if mY<self.rect.y:
            angle = DegAngle
        else:
            angle = -DegAngle
        
        Ratio =ModDist*math.sin(angle)/ModDist*math.cos(angle)
        if self.rect.x<0:
            self.rect.x = 0
        if self.rect.x > width-64:
            self.rect.x = width-64
        if self.rect.y<0:
            self.rect.y = 0
        if self.rect.y>height-64:
            self.rect.y = height-64
        else:
            if Letter == "W":
                self.rect.y -= 2
            if Letter == "S":
                self.rect.y += 2
            if Letter == "A":
                self.rect.x -= 2
            if Letter == "D":
                self.rect.x += 2
            
    def update(self):
        global Screen
        if self.me != None:
            self.me = "Alive"
        Screen.blit(self.allFrames[self.frame-1],self.rect)

    def getPlayerPos(self):
        return self.rect.x,self.rect.y

#Class to fire a Bullet
class Bullet():
    def __init__(self,speed,x,y):
        self.img = pygame.image.load("Small Bullet.png")
        self.speed = speed
        self.x_pos = x
        self.y_pos = y
        self.x_change = 0
        self.y_change = 0

    def Change(self,x1,y1):
        (mX,mY) = pygame.mouse.get_pos()
        ModDist = math.sqrt((x1-mX)**2 + (y1-mY)**2)
        Vect1 = (1,0)
        Vect2 = (mX-x1,mY-y1)
        Angle = math.acos((Vect1[0]*Vect2[0] + Vect1[1]*Vect2[1])/(math.sqrt((mX-x1)**2 + (mY-y1)**2)))
        DegAngle = math.degrees(Angle)
        if mY<self.y_pos:
            angle = DegAngle
        else:
            angle = -DegAngle
        Ratio = (mY-y1)/float(mX-x1)
        if mX>x1:
            self.x_change = self.speed*1
        else:
            self.x_change = self.speed*(-1)
        if Modulus(angle)>75 and Modulus(angle)<105:
            if Ratio>self.speed:
                Ratio = self.speed
            if Ratio<-self.speed:
                Ratio = -self.speed
            if Ratio>0 and Ratio<self.speed/2:
                Ratio = self.speed/2
            if Ratio<=0 and Ratio>-self.speed/2:
                Ratio = -self.speed/2
        self.y_change = self.x_change*Ratio
        
    def Move(self):
        self.x_pos += self.x_change
        self.y_pos += self.y_change
    def update(self):
        global Screen
        Screen.blit(self.img,(self.x_pos,self.y_pos))

###Initializes a socket connection.
##socket = Login.StartConnection("86.36.33.206", 15112)
##
###Initializes a Tkinter Login Window
##wnd = Tkinter.Tk()
##wnd.geometry("250x250")
##wnd.title("Enter The Undead Realm")
##UsernameStr = Tkinter.StringVar()      #Gets the value in entrybox and stores it in UsernameStr.
##PasswordStr = Tkinter.StringVar()      #Gets the value in the entrybox 2 and stores it in PasswordStr.
##Username = Tkinter.Label(wnd,text="Username")           #Label - Username
##FillSpace1 = Tkinter.Entry(wnd,textvariable=UsernameStr)      #Entry Box
##Password = Tkinter.Label(wnd,text="Password")           #Label - Password
##FillSpace2 = Tkinter.Entry(wnd,show="*",textvariable=PasswordStr)    #Entry Box
##Username.pack()                    # |
##FillSpace1.pack()                  # |
##Password.pack()                    # | =   Shows them on the window
##FillSpace2.pack()                  # |
##Okay = Tkinter.Button(text="Enter the Realm!",command=lambda x= [FillSpace1,FillSpace2]: PlayScreen(x))   #Button - OK
##Okay.pack()    
##wnd.mainloop()

#Initialize pygame and set up display
pygame.init()
width,height = 900,500
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
NewZombieCount = -40
x_change = 0
y_change = 0
mX , mY = 0 , 0
RandomNo1 = random.randint(4,15)
Percentage = 100
Player1 = Player(width/2-32,height/2-32)
AimAssistCount = 0
angle = -90
clock = pygame.time.Clock()


#Creating Boundary Coordinates and Storing them in a list.
ListofBoundaryCoords = []
for i in range(width/2):
    ListofBoundaryCoords += [(i,0)]
for i in range(width/2,width):
    ListofBoundaryCoords += [(i,height)]
for i in range(height/2):
    ListofBoundaryCoords += [(0,i)]
for i in range(height/2,height):
    ListofBoundaryCoords += [(width,i)]

    
for i in range(RandomNo1):
    RandomNo2 = random.randint(1,(width+height))
    (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
    SummonZombie("Brain",x,y)


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
            ZombieKiller = Bullet(5,P1x,P1y)
            ZombieKiller.Change(P1x,P1y)
            AllBullets.append(ZombieKiller)

                
    #Zombie LOOP
    Screen.fill(white)
    for Zomb in AllZombies:
        P1x,P1y = Player1.getPlayerPos()
        Zomb.move(P1x,P1y)                
        Zomb.update()

    #Random New Zombie Spawner Condition
    if NewZombieCount%1250 == 0 and NewZombieCount != 0:
        RandomNo2 = random.randint(1,(width+height))
        (x,y) = ListofBoundaryCoords[RandomNo2 - 1]
        Decider = random.choice([1,2,3,4,5,6,7,8,9,10])
        if Decider < 4:
            SummonZombie("Cap",x,y)
        else: 
            SummonZombie("Brain",x,y)
    NewZombieCount += 1


    #Handling Pressed Keys    
    KeysPressed = pygame.key.get_pressed()
    if KeysPressed[pygame.K_TAB]:
        AimAssistCount += 1
    if AimAssistCount%2 == 1:
        Aim = AimAssistON()
        (mX,mY) = pygame.mouse.get_pos()
        Screen.blit(Aim,(mX-7,mY-7))
    KeysPressed = pygame.key.get_pressed()
    if KeysPressed[pygame.K_w]:
        Player1.Move("W")
    if KeysPressed[pygame.K_s]:
        Player1.Move("S")
    if KeysPressed[pygame.K_a]:
        Player1.Move("A")
    if KeysPressed[pygame.K_d]:
        Player1.Move("D")
    
    for Bullets in AllBullets:
        Bullets.Move()
        Bullets.update()
            
    #Player1 Update Haandler    
    Player1.ChangeFrame()
    Player1.update()
     
    #Health Bar Handler
    Screen.blit(HealthBar(Percentage),(width-210,height-140))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()

##Newwnd = Tkinter.Tk()
##Newwnd.title("Realm Updater")
##Newwnd.geometry("1000x700")
##background = Image.open("ZombieBackground.jpg")
##background_image = ImageTk.PhotoImage(background)
##Background_label = Tkinter.Label(Newwnd,image=background_image)
##Background_label.place(x=0,y=0,relwidth=1,relheight=1)
##Canvas = Tkinter.Canvas(Newwnd,width=20,height=7)
##Canvas.grid(row=5,column=1)    
##PlayImg = Image.open("PassivePlay.png")
##ActivePlayImg = Image.open("ActivePlay.png")
##Play = ImageTk.PhotoImage(PlayImg)
##ActivePlay = ImageTk.PhotoImage(ActivePlayImg)
##PlayButton = Tkinter.Label(Newwnd,image=Play)
##PlayButton.grid(padx=500,pady=300)
##Newwnd.mainloop()
##










    
