import pygame
import time
import GameBoard
from GameBoard import Gameboard
from Shape import Shape
# import a library of function called 'pygame'
from Blocks import Blocks
# initualize the game engine
pygame.init()
black=(0, 0, 0)
white=(255, 255, 255)
red=(255, 0, 0)
blue=(0, 0, 255)
green=(0, 255, 0)
orange=(255, 127, 0)
yellow=(255, 255, 0)
pink=(255, 0, 255)
turquoise=(0, 206, 209)



def drawScreen():
    screen.fill(black)
    shape.draw(screen)
    nextshape.drawnextshape(screen)
    gameboard.draw(screen)
    scoretext = myfont.render("score: " + str(gameboard.score), 1, turquoise)
    screen.blit(scoretext, (400, 400))
    linestext = myfont.render("line: " + str(gameboard.numline), 1, blue)
    screen.blit(linestext, (400, 350))
    leveltext = myfont.render("Level: " + str(gameboard.level), 1, white)
    screen.blit(leveltext, (400, 300))



    if settings_ed == False:
        settings_ed_image = pygame.image.load("settings.png")
        screen.blit(settings_ed_image, (770, 9))

    if paused == False:
        pause_image = pygame.image.load("pause.png")
        screen.blit(pause_image, (745, 10))
    else:
        play_image = pygame.image.load("play.png")
        screen.blit(play_image, (745, 9))

    if powerUpReady == False:
        poweruptext = myfont.render("Power Ups (x" + str(gameboard.numpowerup) + "): ", 1, white)
        screen.blit(poweruptext, (50, 525))
        slowtime_image = pygame.image.load("clock.png")
        screen.blit(slowtime_image, (300, 515))
        swap_image = pygame.image.load("swap.png")
        screen.blit(swap_image, (360, 515))
    else:
        poweruptext = myfont.render("Power Ups (x" + str(gameboard.numpowerup) + "): ", 1, green)
        screen.blit(poweruptext, (50, 525))
        slowtime_image = pygame.image.load("clock.png")
        screen.blit(slowtime_image, (300, 515))
        swap_image = pygame.image.load("swap.png")
        screen.blit(swap_image, (360, 515))

    nextshapetext = myfont.render("Next: ", 1, white)
    screen.blit(nextshapetext, (400, 50))
    pygame.draw.rect(screen, white, [400, 100, 6 * shape.blocklist[0].size, 6 * shape.blocklist[0].size], 1)
    # Display the high scores
    highscoretext = myfont.render("High Scores", 1, white)
    screen.blit(highscoretext, (575, 50))
    pygame.draw.rect(screen, black, [575, 100, 200, 400])
    # Display the name
    playernametext = myfont.render("Player: " + name, 1, white)
    screen.blit(playernametext, (515, 525))

    for i in range(5):
        hsnametext = HSfont.render(str(namelist[i]), 1, white)
        hsscoretext = HSfont.render(str(scorelist[i]), 1, white)
        screen.blit(hsnametext, (580, i*25 + 125))
        screen.blit(hsscoretext, (700, i * 25 + 125))
    pygame.display.flip()  # updates the screen with every thing we've drawn


def getSmallestGridxPos():
    allxPos = [shape.blocklist[0].gridxPos,shape.blocklist[1].gridxPos,shape.blocklist[2].gridxPos,shape.blocklist[3].gridxPos]
    return min(allxPos)
def getSmallestGridyPos():
    allyPos = [shape.blocklist[0].gridyPos,shape.blocklist[1].gridyPos,shape.blocklist[2].gridyPos,shape.blocklist[3].gridyPos]
    return min(allyPos)
def checkhighscore():
    newhighscore = False
    tempnamelist = [0 for y in range(5)]
    tempscorelist = [0 for y in range(5)]
    for i in range(5):
        if gameboard.score > int(scorelist[i]) and newhighscore == False:
            newhighscore = True
            tempscorelist[i] = gameboard.score
            tempnamelist[i] = name
        elif newhighscore == True:
            tempscorelist[i] = scorelist[i-1]
            tempnamelist[i] = namelist[i - 1]
        else:
            tempscorelist[i] = scorelist[i]
            tempnamelist[i] = namelist[i]

    for i in range(5):
        scorelist[i] = tempscorelist[i]
        namelist[i] = tempnamelist[i]

        HSfile = open("HighScores.txt", 'w')
        for i in range(5):
            HSfile.write(namelist[i] + '\n')

        for i in range(5):
            HSfile.write(str(scorelist[i]) + '\n')
        HSfile.close()


def title_screen():
    global started
    global name
    while not started:
        titlescreen = pygame.image.load("Backdrop.png")
        enterednametext = myfont.render("Your Name:", 1, white)
        screen.blit(enterednametext, (200, 200))
        nametext = myfont.render(name, 1, white)
        screen.blit(nametext, (300, 250))
        pygame.display.flip()
        screen.blit(titlescreen, (0, 0))

        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key >= 32 and event.key <= 126 and len(name) < 10:
                    name = name + chr(event.key)  # adds another character to the name
                if event.key == pygame.K_BACKSPACE:  # removes last character in the name
                    name = name[:-1]
                if event.key == pygame.K_RETURN:
                    if name == "":  # if it's blank set it to Unknown
                        name = "Unknown"
                    started = True  # start the game



if __name__ == "__main__":
    nextshape = Shape(0,0,None)
    shape = Shape(0,0,nextshape)

def restart():
    for i in range(GameBoard.gameboardwidth):
        for j in range(GameBoard.gameboardheight):
            GameBoard.activeBoardSpot[i][j] = False  # initializes it to inactive
            GameBoard.activeBoardColour[i][j] = (0, 0, 0)  # initializes it to black

    global nextshape
    nextshape = Shape(0,0,None)
    global shape
    shape = Shape(0,0,nextshape)

    gameboard.score = 0
    gameboard.numline = 0
    gameboard.level = 1
    gameboard.numpowerup = 0

    drawScreen()



if __name__=="__main__":
    # size of the game board
    pygame.mixer.init()
    size = (800, 600)
    xPosition = 200
    yPosition = 120
    blocksize = 25
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche")
    myfont = pygame.font.Font('freesansbold.ttf', 30)
    HSfont = pygame.font.Font('freesansbold.ttf', 20)
    infont = pygame.font.Font('freesansbold.ttf', 15)
    block = Blocks(yellow,4,5)

    nextshape = Shape(0,0,None)
    shape = Shape(0,0,nextshape)
    gameboard = Gameboard(green, block.size)
    name = ""  # used for storing the player's name by default it is empty
    delay = 0
    slowtimedelay = 0
    pygame.mixer.music.load('AvalancheBGM.mp3')
    pygame.mixer.music.play(-1)  # use -1 to make it loop
    namelist = [0 for y in range(5)]
    scorelist = [0 for y in range(5)]
    HSfile = open("HighScores.txt", "r")
    for i in range(5):
        namelist[i] = HSfile.readline().rstrip('\n')
    for i in range(5):
        scorelist[i] = HSfile.readline().rstrip('\n')
    HSfile.close()
    done = False
    started = False
    diffButton = pygame.image.load("emh.png").convert_alpha()
    diffButtonRect = diffButton.get_rect()
    back2Button = pygame.image.load("back.png").convert_alpha()
    back2ButtonRect = back2Button.get_rect()
    helpButton = pygame.image.load("help.png").convert_alpha()
    helpButtonRect = helpButton.get_rect()
    restartButton = pygame.image.load("restart.png").convert_alpha()
    restartButtonRect = restartButton.get_rect()
    homeButton = pygame.image.load("home.png").convert_alpha()
    homeButtonRect = homeButton.get_rect()
    backButton = pygame.image.load("back.png").convert_alpha()
    backButtonRect = backButton.get_rect()
    settingsButton = pygame.image.load("settings.png").convert_alpha()
    settingsButtonRect = settingsButton.get_rect()
    pauseButton = pygame.image.load("pause.png").convert_alpha()
    pauseButtonRect = pauseButton.get_rect()
    playButton = pygame.image.load("play.png").convert_alpha()
    playButtonRect = playButton.get_rect()
    clockPowerUp = pygame.image.load("clock.png").convert_alpha()
    clockPowerUpRect = clockPowerUp.get_rect()
    swapPowerUp = pygame.image.load("swap.png").convert_alpha()
    swapPowerUpRect = swapPowerUp.get_rect()
    powerUpReady = False
    paused = False
    settings_ed = False
    backed = False
    homed = False
    restarted = False
    helped = False
    backed2 = False
    emhed = False

title_screen()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shape.MoveLeft()
            elif event.key == pygame.K_RIGHT:
                shape.MoveRight()
            elif event.key == pygame.K_d:
                shape.MoveDown()
            elif event.key == pygame.K_UP:
                shape.rotateCW()
            elif event.key == pygame.K_DOWN:
                shape.rotateCCW()
            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                shape.drop()
            elif event.key  == pygame.K_p:
                if powerUpReady == False and gameboard.numpowerup > 0:
                    powerUpReady = True
            elif event.key  == pygame.K_f:
                if paused == False:
                    paused = True
            elif event.key  == pygame.K_s:
                if settings_ed == False:
                    settings_ed = True
            elif event.key  == pygame.K_f:
                if backed == False:
                    backed = True
            elif event.key  == pygame.K_w:
                if homed == False:
                    homed = True
            elif event.key == pygame.K_r:
                if restarted == False:
                    restarted = True
            elif event.key == pygame.K_i:
                if helped == False:
                    helped = True
            elif event.key  == pygame.K_c:
                if backed2 == False:
                    backed2 = True
            elif event.key == pygame.K_e:
                if emhed == False:
                    emhed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] > 300 and pos[0] < (300 + clockPowerUpRect.width):
                if pos[1] > 515 and pos[1] < (515 + clockPowerUpRect.height):
                    if powerUpReady == True:
                        if gameboard.numpowerup > 0:
                            gameboard.slowtimeon = True
                            powerUpReady = False
                            gameboard.numpowerup -= 1
            if pos[0] > 360 and pos[0] < (360 + swapPowerUpRect.width):
                if pos[1] > 515 and pos[1] < (515 + swapPowerUpRect.height):
                    if powerUpReady == True:
                        if gameboard.numpowerup > 0:
                            gameboard.swapon = True
                            powerUpReady = False
                            gameboard.numpowerup -= 1
            if pos[0] > 770 and pos[0] < (770 + settingsButtonRect.width):
                if pos[1] > 9 and pos[1] < (9 + settingsButtonRect.height):
                    if settings_ed == False:
                        settings_ed = True
            if pos[0] > 745 and pos[0] < (745 + pauseButtonRect.width):
                if pos[1] > 10 and pos[1] < (10 + pauseButtonRect.height):
                    if paused == False:
                      paused = True

    paused_old = False
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                paused = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    paused = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 745 and pos[0] < (745 + playButtonRect.width):
                    if pos[1] > 9 and pos[1] < (9 + playButtonRect.height):
                         paused = False
                if pos[0] > 770 and pos[0] < (770 + settingsButtonRect.width):
                    if pos[1] > 9 and pos[1] < (9 + settingsButtonRect.height):
                        if settings_ed == False:
                            settings_ed = True
                            paused_old = paused
                            paused = False

        drawScreen()

    while settings_ed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                settings_ed = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 10 and pos[0] < (10 + backButtonRect.width):
                    if pos[1] > 9 and pos[1] < (9 + backButtonRect.height):
                        settings_ed = False
                        paused = paused_old
                if pos[0] > 200 and pos[0] < (200 + homeButtonRect.width):
                    if pos[1] > 200 and pos[1] < (200 + homeButtonRect.height):
                        settings_ed = False
                        started = False
                        title_screen()
                if pos[0] > 550 and pos[0] < (550 + restartButtonRect.width):
                    if pos[1] > 200 and pos[1] < (200 + restartButtonRect.height):
                        settings_ed = False
                        restart()
                if pos[0] > 385 and pos[0] < (385 + helpButtonRect.width):
                    if pos[1] > 450 and pos[1] < (450 + helpButtonRect.height):
                        if helped == False:
                            helped = True
                            settings_ed = False
                if pos[0] > 255 and pos[0] < (255 + diffButtonRect.width):
                    if pos[1] > 300 and pos[1] < (300 + diffButtonRect.height):
                        if helped == False:
                            helped = True
                            settings_ed = False
                if pos[0] > 255 and pos[0] < (255 + diffButtonRect.width):
                    if pos[1] > 300 and pos[1] < (300 + diffButtonRect.height):
                        if helped == False:
                            helped = True
                            settings_ed = False
                if pos[0] > 255 and pos[0] < (255 + diffButtonRect.width/3):
                    if pos[1] > 300 and pos[1] < (300 + diffButtonRect.height):
                        if helped == False:
                            helped = True
                            settings_ed = False

        titlescreen = pygame.image.load("blackbackground.jpg")
        enterednametext = myfont.render("SETTINGS", 1, white)
        screen.blit(titlescreen, (0, 0))
        screen.blit(enterednametext, (335, 50))
        backed_image = pygame.image.load("back.png")
        screen.blit(backed_image, (10, 9))
        homed_image = pygame.image.load("home.png")
        screen.blit(homed_image, (200, 200))
        restarted_image = pygame.image.load("restart.png")
        screen.blit(restarted_image, (550, 200))
        helped_image = pygame.image.load("help.png")
        screen.blit(helped_image, (385, 450))
        emhed_image = pygame.image.load("emh.png")
        screen.blit(emhed_image, (255, 300))
        pygame.display.flip()

    while helped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                helped = False
            elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > 10 and pos[0] < (10 + back2ButtonRect.width):
                        if pos[1] > 9 and pos[1] < (9 + back2ButtonRect.height):
                            helped = False
                            settings_ed = True
        titlescreen = pygame.image.load("yellowBackground.jpg")
        enterednametext = myfont.render("INSTRUCTION(GUIDE)", 1, orange)
        screen.blit(titlescreen, (0, 0))
        screen.blit(enterednametext, (250, 50))
        backed2_image = pygame.image.load("back.png")
        screen.blit(backed2_image, (10, 9))
        pic = pygame.image.load("arrowkeys.png")
        screen.blit(pic, (20, 20))
        enterednametext = infont.render("1). Left and Right keys to move shape", 1, orange)
        screen.blit(enterednametext, (175, 90))
        enterednametext = infont.render("2). Up and Down keys to rotate shape", 1, orange)
        screen.blit(enterednametext, (175, 110))
        enterednametext = infont.render("3). The Shape in the box below 'NEXT:' is the next shape coming up", 1, orange)
        screen.blit(enterednametext, (20, 135))
        pygame.display.flip()

    if gameboard.checkLost():
        checkhighscore()
        delay = 0
        slowtimedelay = 0
        gameboard = Gameboard(green, shape.blocklist[0].size)
        shape = Shape(0,0,None)
        nextshape = Shape(0,0,None)
    if gameboard.swapon:
        shape = Shape(getSmallestGridxPos(), getSmallestGridyPos(),shape)
        gameboard.swapon = False
    if gameboard.slowtimeon:
        slowtimedelay += 1
        if slowtimedelay > 50:
            slowtimedelay = 0
            gameboard.slowtimeon = False

    drawScreen()
    if (0.11 - gameboard.level * 0.001 >= 0):
        time.sleep(0.11 - gameboard.level * 0.001 + gameboard.slowtimeon * 0.1)
    delay += 1
    if delay >= 10:
       shape.falling()
       delay = 0
    if shape.active == False:
        gameboard.clearFullRow()
        shape = Shape(0,0,None)
        shape = nextshape
        nextshape = Shape(0,0,None)
    time.sleep(0.01)