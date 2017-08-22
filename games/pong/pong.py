#Simple Pong game by ChristGames.org for pygame tutorial

#Import Modules

import pygame #Game Engine
import random #Random Numbers
import sys #Python System
import math #Math Functions

#Initialize SubModules

pygame.init() #Intialize pygame
pygame.font.init() #Initialize Fonts
pygame.mixer.init() #Initialize Sound

#Define Globals

clock = pygame.time.Clock() #Initialize Time
black = [0, 0, 0] #Color - Black
blue = [0, 0, 255] #Color - Blue
white = [255, 255, 255] #Color - White
blip = pygame.mixer.Sound('blip.ogg') #Classic Pong Blip Sound
font40 = pygame.font.SysFont("None", 40) #Font For Splash Screen
font60 = pygame.font.SysFont("None", 60) #Font For Score
font140 = pygame.font.SysFont("None", 140) #Font For Score
    
#Set Display to FullScreen

swidth = pygame.display.Info().current_w #Get Current Screen Width
sheight = pygame.display.Info().current_h #Get Current Screen Height
screen = pygame.display.set_mode((swidth,sheight),pygame.NOFRAME+pygame.FULLSCREEN) #Set Display Mode

#----- Splash Screen -----

def SplashScreen():

    #Define Locals

    logo = pygame.image.load('cglogo02.png') #Load Logo Image Into Memory

    #Clear Screen

    screen.fill(blue) #Blue Screen

    #Draw Spash Screen Objects

    screen.blit(logo, ((swidth/2)-220,(sheight/2)-220)) #Display Logo Image
    screen.blit(font40.render("Simple Pong Game", 0, white), ((swidth/2)-100, (sheight/2)-220))
    screen.blit(font40.render("By ChristGames.org", 0, white), ((swidth/2)-100, (sheight/2)-180))
    screen.blit(font40.render("*** Game Controllers ***", 0, white), ((swidth/2)-160, (sheight/2)-50))
    screen.blit(font40.render("Left Player - [W]=Up [S]=Down", 0, white), ((swidth/2)-200, (sheight/2)+10))
    screen.blit(font40.render("Right Player - [Up/Down Arrow]", 0, white), ((swidth/2)-200, (sheight/2)+40))
    screen.blit(font40.render("Serve Ball - [Space Bar]", 0, white), ((swidth/2)-200, (sheight/2)+70))
    screen.blit(font40.render("Quit Game - [Esc]", 0, white), ((swidth/2)-200, (sheight/2)+100))
    screen.blit(font40.render("Press [space bar] to start game...", 0, white), ((swidth/2)-230, (sheight/2)+200))

    #Display Screen Buffer

    pygame.display.flip()

    #Pause for Space Bar To Be Pressed
    
    SpaceBarWait()
        
#----- Get Theta Value in Degrees For A Serve -----

def ServeBallAngle(side): #Uses Polar Coordinate System
    random.seed()
    blip.play() #Play Sound
    if side == 0: #0=Right Side Serve, 1=Left Side Serve
        if random.randint(0, 1):
            dtheta=random.randint(0, 50) #Quadrant I 
        else:
            dtheta=random.randint(310, 360) #Quadrant II
    else:
        dtheta=random.randint(130, 230) #Quadrant III & IV
    return dtheta #Return Theta In Degrees

#----- Check if Close (X) Button Pressed -----

def CheckClose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quit Game Requested
            QuitGame()

#----- Wait Until Space Bar is Pressed -----

def SpaceBarWait():
    while True: #Loop Forever
        CheckClose() #Check If Quit Game Requested
        key = pygame.key.get_pressed() #Press A Key
        if key[pygame.K_ESCAPE]:
            QuitGame() #ESC Key Pressed - Quit Game
        if key[pygame.K_SPACE]:
            return 1 #Space Bar Pressed - Start Game

#----- Quit Game and CleanUp Environment -----
 
def QuitGame():
    pygame.quit() #CleanUp pygame objects
    sys.exit() #CleanUp Python objects
    
#----- Main Program Function -----

def main():

    SplashScreen() #Display Splash Screen

    #Define Locals

    p1score = 0 #Player #1 Score
    p2score = 0 #Player #2 Score
    lpad = ((sheight/2)-35) #left Paddle Top Starting Position
    rpad = ((sheight/2)-35) #Right Paddle Top Starting Position
    radiald = 0 #Balll Radial Distance From Starting Point
    speed = 10 #Speed Ball Travels
    spacelock = 0 #Lock Space Bar During A Play, 0=Unlocked

    random.seed()
    if random.randint(0, 1): #Random Toss For First Serve
        side=1 #1=Left Side Serve
    else:
        side=0 #0=Right Side Serve

    while True: #Loop Forever
        
        clock.tick(60) #Set Game Refresh Rate To 60 Frames Per Second
        CheckClose() #Check If Quit Game Requested

        #Keyboard Input

        key = pygame.key.get_pressed() #Press A Key
        if key[pygame.K_SPACE] or loss==1: #Check Key Press and Loss
            if spacelock==0 or loss==1: #Serve A New Ball
                dtheta = ServeBallAngle(side) #Get Ball Angle On Serve
                radiald = 0 #Balll Radial Distance From Starting Point
                polex = (swidth/2) #X Position For Starting Point For Ball
                poley = (sheight/2) #Y Position For Starting Point For Ball
                loss = 0 #0=Ball Is In Play, 1=Player Lost A Server
                spacelock = 1 #Lock Space Bar During A Play, 1=Locked
        if key[pygame.K_w]: #W Key=Paddle Up Key For Left Player
            if lpad <=10: #Top Of Screen Reached
                lpad=10 #Set Left Paddle Top Boundary
            else:
                lpad-=10 #Move Left Paddle Up
        if key[pygame.K_s]: #S Key=Paddle Down Key For Left Player
            if lpad >=sheight-80: #Bottom Of Screen Reached
                lpad=sheight-80 #Set Left Paddle Bottom Boundary
            else:
                lpad+=10 #Move Left Paddle Down
        if key[pygame.K_UP]: #Up Arrow Key=Paddle Up Key For Right Player
            if rpad <=10: #Top Of Screeen Reached
                rpad=10 #Set Right Paddle Top Boundary
            else:
                rpad-=10 #Move Right Paddle Up
        if key[pygame.K_DOWN]: #Down Arrow Key=Paddle Down Key For Right Player
            if rpad >=sheight-80: #Bottom Of Screen Reached
                rpad=sheight-80 #Set Right Paddle Bottom Boundary
            else:
                rpad+=10 #Move Right Paddle Down
        if key[pygame.K_ESCAPE]:
            QuitGame() #ESC Key Pressed - Quit Game

        #Move Ball

        radiald=radiald+speed #Increment Radial Distance + Speed
        rtheta=dtheta*(math.pi/180) #Convert Theta From Degrees To Radians
        ballx=(radiald*math.cos(rtheta))+polex #Calculate X Ball Location
        bally=(-radiald*math.sin(rtheta))+poley #Calculate Y Ball Location
            
        #Check Collision

        if bally <=10: #Top Of Screen Reached
            blip.play() #Play Sound
            dtheta = -dtheta #Reverse Ball Angle
            polex = ballx #Set New Ball X Starting Position
            poley = 10 #Set New Ball Y Starting Position
            bally = 10 #Set New Ball Y Starting Position
            radiald = 0 #Balll Radial Distance From Starting Point

        if bally >=sheight-20: #Bottom Of Screen Reached
            blip.play() #Play Sound
            dtheta = -dtheta #Reverse Ball Angle
            polex = ballx #Set New Ball X Starting Position
            poley = sheight-20 #Set New Ball Y Starting Position
            bally = sheight-20 #Set New Ball Y Starting Position
            radiald = 0 #Balll Radial Distance From Starting Point
        if ballx <=50: #Left Side Reached
            if bally>=lpad and bally<=lpad+70: #Ball Hits Paddle
                blip.play() #Play Sound
                dtheta = 180-dtheta #Reverse Ball Angle
                polex = 50 #Set New Ball X Starting Position
                poley = bally #Set New Ball Y Starting Position
                radiald = 0 #Balll Radial Distance From Starting Point
            else: #Ball Misses Paddle
                if ballx<-20: #Let Ball Fall Off Screen
                    p2score+=1 #Right Player Wins A Point
                    loss=1 #0=Ball Is In Play, 1=Player Lost A Server
                    side=0 #Serve Next Ball To Right Side
        if ballx >=swidth-50: #Right Side Reached
            if bally>=rpad and bally<rpad+70: #Ball Hits Paddle
                blip.play() #Play Sound
                dtheta = 180-dtheta #Reverse Ball Angle
                polex = swidth-50 #Set New Ball X Starting Position
                poley = bally #Set New Ball Y Starting Position
                radiald = 0 #Balll Radial Distance From Starting Point
            else: #Ball Misses Paddle
                if ballx>swidth+20: #Let Ball Fall Off Screen
                    p1score+=1 #Left Player Wins A Point
                    loss=1 #0=Ball Is In Play, 1=Player Lost A Server
                    side=1 #Serve Next Ball To Left Side
        
        #Clear Screen

        screen.fill(black)

        #Draw Court

        pygame.draw.rect(screen, white, (0, 0, swidth, 10)) #Top
        pygame.draw.rect(screen, white, (swidth/2, 0, 10, sheight)) #Center
        pygame.draw.rect(screen, white, (0, sheight-10, swidth, swidth)) #Bottom

        #Draw Paddles

        pygame.draw.rect(screen, white, (40, lpad, 10, 70)) #Left
        pygame.draw.rect(screen, white, (swidth-40, rpad, 10, 70)) #Right

        #Draw Score

        if p1score<10:
            tleft=(swidth/2)-70 #Left Score Position For Single Digits
        else:
            tleft=(swidth/2)-130 #Left Score Position For Multiple Digits
        screen.blit(font140.render(str(p1score), 0, white), (tleft, 10)) #Left
        screen.blit(font140.render(str(p2score), 0, white), ((swidth/2)+25, 10)) #Right

        #Draw Ball

        pygame.draw.rect(screen, white, (ballx, bally, 10, 10))

        #Draw If Game Over

        if p1score==11 or p2score==11: #Someone Won
            pygame.draw.rect(screen, black, (swidth/2, 150, 10, sheight-300)) #Black Out Center Line
            if p1score==11: #Left Player Got Score Of 11
                screen.blit(font60.render("Left Player Wins!", 0, white), ((swidth/2)-175, (sheight/2)-80)) #Left Winner Message
            if p2score==11: #Right Player Got Score Of 11
                screen.blit(font60.render("Right Player Wins!", 0, white), ((swidth/2)-180, (sheight/2)-80)) #Right Winner Message
            screen.blit(font40.render("Quit Game - [Esc]", 0, white), ((swidth/2)-120, (sheight/2)-10)) #Quit Game Message
            screen.blit(font40.render("Press [space bar] to start game...", 0, white), ((swidth/2)-230, (sheight/2)+50)) #Press Spacebar Message
            pygame.display.flip() #Display Screen Buffer
            p1score = 0 #Set Left Player Score For A New Game
            p2score = 0 #Set Right Player Score For A New Game
            spacelock = 0 #Lock Space Bar During A Play, 0=Unlocked
            SpaceBarWait() #Pause for Space Bar To Be Pressed

        else: #Continue Playing

            pygame.display.flip() #Display Screen Buffer
    
#----- Main Program Entry -----
            
if __name__ == "__main__":
    main() #Load Main Program Function
