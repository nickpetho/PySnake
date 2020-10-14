import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Sneaky Snake')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)#best size is 32x32px

headImg = pygame.image.load('head.png')
appleImg = pygame.image.load('apple.png')
bodyImg = pygame.image.load('body.png')

clock = pygame.time.Clock()
block_size = 20
AppleThickness = 30
FPS = 12
direction = 0
creditsFont = pygame.font.SysFont("timesnewroman", 15)
smallFont = pygame.font.SysFont("timesnewroman", 25)
medFont = pygame.font.SysFont("timesnewroman", 35)
largeFont = pygame.font.SysFont("magneto", 50)

def pause():
    paused = True
    while(paused):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
              pygame.quit()
              quit()
            if(event.type == pygame.KEYDOWN):
               if(event.key == pygame.K_c):
                  paused = False
               elif(event.key == pygame.K_q):
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
        message_to_screen("Paused", blue, -100, size = "large")
        message_to_screen("Press C to continue or Q to quit", black, 25)
        pygame.display.update()
        clock.tick(12)
        

def score(score):
    text = medFont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [5,5])

def randAppleGen():
    randAppleX = random.randrange(0, display_width-AppleThickness, block_size)
    randAppleY = random.randrange(0, display_height-AppleThickness, block_size)
    return randAppleX, randAppleY

def game_intro():
    intro = True
    while(intro):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_c):
                    intro = False
                if(event.key == pygame.K_q):
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        gameDisplay.blit(appleImg, [200, 10])
        gameDisplay.blit(headImg, [205, 60])
        gameDisplay.blit(bodyImg, [205, 80])
        gameDisplay.blit(bodyImg, [205, 100])
        gameDisplay.blit(bodyImg, [205, 120])
        gameDisplay.blit(bodyImg, [225, 120])
        gameDisplay.blit(bodyImg, [245, 120])
        gameDisplay.blit(bodyImg, [245, 100])
        gameDisplay.blit(bodyImg, [265, 100])
        gameDisplay.blit(bodyImg, [285, 100])
        gameDisplay.blit(bodyImg, [305, 100])
        gameDisplay.blit(bodyImg, [305, 120])
        gameDisplay.blit(bodyImg, [325, 120])
        gameDisplay.blit(bodyImg, [345, 120])
        gameDisplay.blit(bodyImg, [345, 140])
        gameDisplay.blit(bodyImg, [345, 160])
        message_to_screen("Welcome to Sneaky Snake", green, -100, "large")
        message_to_screen("The objective of the game is to eat the red apples.", black, -30)
        message_to_screen("The more apples you eat the longer your snake gets.", black, 10)
        message_to_screen("If you run into yourself or the edges, you die!", black, 50)
        message_to_screen("Press C to play, P to pause, or Q to quit.", black, 180)
        message_to_screen("Developed by Nick Petho. Art by Matthew Luonuansuu. 2017.", black, 280, size = "credits")
        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakeList):
    if(direction == 1):
        head = pygame.transform.rotate(headImg, 270)
    if(direction == 3):
        head = pygame.transform.rotate(headImg, 90)
    if(direction == 0):
        head = headImg
    if(direction == 2):
        head = pygame.transform.rotate(headImg, 180)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        gameDisplay.blit(bodyImg, [XnY[0], XnY[1], block_size, block_size])
        #pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if(size == "credits"):
        textSurface = creditsFont.render(text, True, color)
    elif(size == "small"):
        textSurface = smallFont.render(text, True, color)
    elif(size == "medium"):
        textSurface = medFont.render(text, True, color)
    elif(size == "large"):
        textSurface = largeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    direction = 0
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = -10
    snakeList = []
    snakeLength = 1
    randAppleX, randAppleY = randAppleGen()
    
    while not(gameExit):
        while(gameOver == True):
            #gameDisplay.fill(white)
            message_to_screen("GAME OVER, LOSER", red, y_displace = -50, size = "large")
            message_to_screen("Press C to play again or Q to quit", black, 50, size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    gameExit = True
                    gameOver = False
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        gameExit = True
                        gameOver = False
                    if(event.key == pygame.K_c):
                        gameLoop()
            
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameExit = True
            if(event.type == pygame.KEYDOWN):      
                if(event.key == pygame.K_LEFT and direction != 1):
                    direction = 3
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif(event.key == pygame.K_RIGHT and direction != 3):
                    direction = 1
                    lead_x_change = block_size
                    lead_y_change = 0
                elif(event.key == pygame.K_UP and direction != 2):
                    direction = 0
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif(event.key == pygame.K_DOWN and direction != 0):
                    direction = 2
                    lead_y_change = block_size
                    lead_x_change = 0
                elif(event.key == pygame.K_p):
                    pause()
            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #lead_x_change = 0
                #if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #lead_y_change = 0

        if(lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0):
            gameOver = True
            
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)                             #x-axis,y-axis,w,h
##        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
##        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness]) 
        gameDisplay.blit(appleImg, (randAppleX, randAppleY))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if(len(snakeList) > snakeLength):
               del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if(eachSegment == snakeHead):
                gameOver = True
        
        snake(block_size, snakeList)
        score(snakeLength-1)
        if(snakeLength == 26):
            message_to_screen("YOU SCORED 25!!", red, size = "large")
        if(snakeLength == 51):
            message_to_screen("YOU SCORED 50!!", red, size = "large")
        if(snakeLength == 76):
            message_to_screen("YOU SCORED 75!!", red, size = "large")
        if(snakeLength == 101):
            message_to_screen("YOU SCORED 100!!!!", red, size = "large")
        pygame.display.update()

        if(lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness):
            if(lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness):
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                
        clock.tick(FPS)

    pygame.quit()
    quit()

#MAIN
game_intro()
gameLoop()
