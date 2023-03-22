import pygame
import random
import sys
from pygame.locals import *

# Global variables
FPS = 32
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width,screen_height))
ground_y = 466
game_images = {}
game_sound = {}

pygame.init()     # initialize all module 
fps_clock = pygame.time.Clock()   #used for fps control 
pygame.display.set_caption('Flappy Bird By Nikunj')
# storing all images
game_images['welcomescreen'] = pygame.image.load(r"img\welcome.png").convert()
game_images['background'] = pygame.image.load(r"img\bg.png").convert()
game_images['bird'] = pygame.image.load(r"img\bird.png").convert_alpha()
game_images['base'] = pygame.image.load(r"img\base.png").convert_alpha()
game_images['pipe'] = (pygame.transform.rotate(pygame.image.load(r"img\pipe.png").convert_alpha(),180),
                        pygame.image.load(r"img\pipe.png").convert_alpha()
)
game_images['numbers'] = (
    pygame.image.load(r'img\0.png').convert_alpha(),
    pygame.image.load(r'img\1.png').convert_alpha(),
    pygame.image.load(r'img\2.png').convert_alpha(),
    pygame.image.load(r'img\3.png').convert_alpha(),
    pygame.image.load(r'img\4.png').convert_alpha(),
    pygame.image.load(r'img\5.png').convert_alpha(),
    pygame.image.load(r'img\6.png').convert_alpha(),
    pygame.image.load(r'img\7.png').convert_alpha(),
    pygame.image.load(r'img\8.png').convert_alpha(),
    pygame.image.load(r'img\9.png').convert_alpha()
    )

# storing all sounds
game_sound['hit']= pygame.mixer.Sound(r"sounds\hit.wav")
game_sound['flap']= pygame.mixer.Sound(r"sounds\flap.wav")
game_sound['point']= pygame.mixer.Sound(r"sounds\point.wav")


def main():
    while True:
        welcomescreen()   # for welcome screen or home screen
        maingame()


def welcomescreen():
    """
    Shows the homescreen or welcome screen
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key== K_SPACE:
                return
            else:
                screen.blit(game_images['welcomescreen'],(0,0))
                pygame.display.update()
                fps_clock.tick(FPS)




def maingame():
    groun_x = 0
    player_x = int(screen_width/8)
    player_y = int((screen_height-game_images['bird'].get_height())/2)
    score = 0

    #creating two pipes
    newpipe1 = getrandompipe()
    newpipe2 = getrandompipe()

    #list of upper pipes   
    upperPipes = [
        {'x': screen_width+200, 'y': newpipe1[0]['y']},
        {'x': screen_width+200+(screen_width/2), 'y': newpipe2[0]['y']}
    ]  # here 200 is distance of first pipe from the screen

    #list of lower pipes
    lowerPipes = [
        {'x': screen_width+200, 'y': newpipe1[1]['y']},
        {'x': screen_width+200+(screen_width/2), 'y': newpipe2[1]['y']}
    ]

    pipeVelX = -4  #pipe velocity (x cordinate)
    playerVelY = -9    # player velocity (y cordinate)
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1     #player acceleration (y cordinate)
 
    playerFlapVel = -8        #velocity of bird while flapping
    playerFlapped = False   # true when bird do flapping
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if player_y > 0:
                    playerVelY = playerFlapVel 
                    playerFlapped = True
                    game_sound['flap'].play()

        #check crash test
        crashTest = isCollide(player_x, player_y, upperPipes, lowerPipes)
        if crashTest:
            return
        
        #check for score
        playerMidPos = player_x + game_images['bird'].get_width()/2   # mid position of player
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + game_images['pipe'][0].get_width()/2  # mid position of pipe
            if pipeMidPos<= playerMidPos < pipeMidPos + 4:  # 4 is a little band
                score +=1
                # print(f"Your Score is {score}")
                game_sound['point'].play()

        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        
        if playerFlapped:
            playerFlapped = False
        playerHeight = game_images['bird'].get_height()
        player_y = player_y + min(playerVelY, ground_y - player_y - playerHeight)

        #move pipes to left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x']  += pipeVelX

        # add new pipe when one is about to remove from screen
        if 0 < upperPipes[0]['x']<5:
            newPipe = getrandompipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1]) 

        # if pipe is going out screen then to remove it
        if upperPipes[0]['x'] < -game_images['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        #print everything
        screen.blit(game_images['background'],(0,0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            screen.blit(game_images['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(game_images['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        screen.blit(game_images['bird'],(player_x,player_y))
        screen.blit(game_images['base'],(groun_x,ground_y))   

        # to print score
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += game_images['numbers'][digit].get_width()  # will give the total width of numbers
        Xoffset = (screen_width - width)/2   # to get x cordinate of score to print it in middle
        for digit in myDigits:
            screen.blit(game_images['numbers'][digit], (Xoffset, screen_height*0.12))
            Xoffset += game_images['numbers'][digit].get_width()

        pygame.display.update()
        fps_clock.tick(FPS)




def getrandompipe():
    """
    get two randome pipe and return the cordinates of them in list (lower and upper pipe)
    """
    pipe_height = game_images['pipe'][0].get_height()
    offset = screen_height/3        # this is the minimum distance from the top of the screen and lower pipe can be
    y2 = offset + random.randrange(0, int(screen_height - game_images['base'].get_height() - 1.2*offset))                    
    pipeX = screen_width + 20    # 20 is Distance between pipes
    y1 = pipe_height - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe




def isCollide(player_x, player_y, upperPipes, lowerPipes):
    """
    Function return True if player hit the pipe
    """
    # for sky and ground
    if player_y > ground_y - 37 or player_y<0:
        game_sound['hit'].play()
        return True
    
    # for upper pipes
    for pipe in upperPipes:
        pipeHeight = game_images['pipe'][0].get_height()
        if (player_y < pipeHeight + pipe['y']) and (abs(player_x - pipe['x']) < game_images['pipe'][0].get_width()):
            game_sound['hit'].play()
            return True
    # for lower pipes 
    for pipe in lowerPipes:
        pipeHeight = game_images['pipe'][1].get_height()
        if (player_y + game_images['bird'].get_height() > pipe['y']) and (abs(player_x- pipe['x'])<game_images['pipe'][1].get_width() ):
            game_sound['hit'].play()
            return True
    return False

        
        
if __name__ == "__main__":
    main()