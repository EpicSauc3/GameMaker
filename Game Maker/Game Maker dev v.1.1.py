import pygame, sys
from pygame.locals import *
pygame.init()

##for x in [WindowSizes(Main,Load,Save,View,Zoom,Run,NPC,Block),ToolbarPositions(Tool,File,Edit,View,Run,FileClick),

display = pygame.display.set_mode((1024, 768), 0, 32)
##display = pygame.display.set_mode((Main[0], Main[1]), 0, 32)
pygame.display.set_caption('Game Maker')

clock = pygame.time.Clock()

#Main Menu Pictures
MainMenu = pygame.image.load('Pictures/Menu/MainMenu.png')
##MainMenu = pygame.transform.scale(MainMenu, (Main[0], Main[1]))

##File Pictures
File = pygame.image.load('Pictures/Menu/File/File.png')
##File = pygame.transform.scale(File, (Filesx, Filesy))
###File Clicked Pictures
Load = pygame.image.load('Pictures/Menu/File/Load.png')
##Save = pygame.image.load('Pictures/Menu/File/Save.png')
##Exit = pygame.image.load('Pictures/Menu/File/Exit.png')

##Edit Pictures
Edit = pygame.image.load('Pictures/Menu/Edit/Edit.png')
###Edit Clicked Pictures
##Cut = pygame.image.load('Pictures/Menu/Edit/Cut.png')
##Copy = pygame.image.load('Pictures/Menu/Edit/Copy.png')
##Paste = pygame.image.load('Pictures/Menu/Edit/Paste.png')
##KeyBindings = pygame.image.load('Pictures/Menu/Edit/KeyBindings.png')

##View Pictures
View = pygame.image.load('Pictures/Menu/View/View.png')
###View Clicked Pictures
##ZoomIn = pygame.image.load('Pictures/Menu/View/ZoomIn.png')
##ZoomOut = pygame.image.load('Pictures/Menu/View/ZoomOut.png')
##ZoomOptions = pygame.image.load('Pictures/Menu/View/ZoomOptions.png')
##ViewOptions = pygame.image.load('Pictures/Menu/View/ViewOptions.png')

##Run Pictures
Run = pygame.image.load('Pictures/Menu/Run/Run.png')
###Run Clicked Pictures
##Compile = pygame.image.load('Pictures/Menu/Run/Compile.png')
##CompileRun = pygame.image.load('Pictures/Menu/Run/CompileRun.png')

#Highlight
Highlight = pygame.image.load('Pictures/Menu/In.png')

#Colors
white = (255,255,255)

#Variables
##Mouse
posx = 0
posy = 0
##Click
click = 0
###Toolbar Click Variable
click1 = 0
###Block Click Variable
click2 = 0

#Defined Functions
##Checks If The Mouse Is Clicked
def Click():
    global click
    if click == 0:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ToolbarClick()
            click = 1
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        click = 0
##Checks If Anything On The Toolbar Is Clicked
def ToolbarClick():
    global click1
    if posx >= 1 and posx <= 53 and posy >= 1 and posy <= 17:
        click1 = 1
    elif posx >= 54 and posx <= 105 and posy >= 1 and posy <= 17:
        click1 = 2
    elif posx >= 106 and posx <= 165 and posy >= 1 and posy <= 17:
        click1 = 3
    elif posx >= 166 and posx <= 201 and posy >= 1 and posy <= 17:
        click1 = 4
    else:
        click1 = 0
##    global click1
##    if posx >= File[0] and posx <= File[1] and posy >= Tool[0] and posy <= Tool[1]:
##        click1 = 1
##    elif posx >= Edit[0] and posx <= Edit[1] and posy >= File[0] and posy <= File[1]:
##        click1 = 2
##    elif posx >= View[0] and posx <= View[1] and posy >= posy >= File[0] and posy <= File[1]:
##        click1 = 3
##    elif posx >= Run[0] and posx <= Run[1] and posy >= posy >= File[0] and posy <= File[1]:
##        click1 = 4
##    else:
##        click1 = 0
##Displays If User Clicks Toolbar
def Toolbar():
    global click,click1
    ###File
    if click1 == 1:
        display.blit(File,(1,1))
##        display.blit(File,(File[0],Tool[0]))
        if posx >= 1 and posx <= 126 and posy >= 18 and posy <= 34:
##        if posx >= 1 and posx <= 126 and posy >= 18 and posy <= 34:
            display.blit(Highlight,(1,18))
##            display.blit(Highlight,(File[0],Tool[1]+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    LoadClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 1 and posx <= 126 and posy >= 35 and posy <= 51:
##        if posx >= 1 and posx <= 126 and posy >= 35 and posy <= 51:
            display.blit(Highlight,(1,35))
##            display.blit(Highlight,(File[0],(Tool[1]*2)+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    SaveClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 1 and posx <= 126 and posy >= 52 and posy <= 68:
##        if posx >= 1 and posx <= 126 and posy >= 52 and posy <= 68:
            display.blit(Highlight,(1,52))
##            display.blit(Highlight,(File[0],(Tool[1]*3)+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ExitClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        display.blit(Load,(3,20))
        display.blit(Load,(3,37))
        display.blit(Load,(3,54))
    ###Edit
    if click1 == 2:
        display.blit(Edit,(54,1))
##        display.blit(Edit,(Edit[0],Tool[0]))
        if posx >= 54 and posx <= 179 and posy >= 18 and posy <= 34:
##        if posx >= 54 and posx <= 179 and posy >= 18 and posy <= 34:
            display.blit(Highlight,(54,18))
##            display.blit(Highlight,(File[0],Tool[1]+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    LoadClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 54 and posx <= 179 and posy >= 35 and posy <= 51:
##        if posx >= 54 and posx <= 179 and posy >= 35 and posy <= 51:
            display.blit(Highlight,(54,35))
##            display.blit(Highlight,(File[0],(Tool[1]*2)+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    SaveClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 54 and posx <= 179 and posy >= 52 and posy <= 68:
##        if posx >= 54 and posx <= 179 and posy >= 52 and posy <= 68:
            display.blit(Highlight,(54,52))
##            display.blit(Highlight,(File[0],(Tool[1]*3)+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ExitClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 54 and posx <= 179 and posy >= 69 and posy <= 85:
##        if posx >= 54 and posx <= 179 and posy >= 69 and posy <= 85:
            display.blit(Highlight,(54,69))
##            display.blit(Highlight,(File[0],(Tool[1]*4)+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ExitClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        display.blit(Load,(56,20))
        display.blit(Load,(56,37))
        display.blit(Load,(56,54))
        display.blit(Load,(56,71))
    ###View
    if click1 == 3:
        display.blit(View,(106,1))
##        display.blit(View,(View[0],Tool[0]))
        if posx >= 106 and posx <= 231 and posy >= 18 and posy <= 34:
##        if posx >= 106 and posx <= 231 and posy >= 18 and posy <= 34:
            display.blit(Highlight,(106,18))
##            display.blit(Highlight,(File[0],Tool[1]+1))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    LoadClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 106 and posx <= 231 and posy >= 35 and posy <= 51:
##        if posx >= 106 and posx <= 231 and posy >= 35 and posy <= 51:
            display.blit(Highlight,(106,35))
##            display.blit(Highlight,(File[0],(Tool[1]*4)+1)))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    SaveClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 106 and posx <= 231 and posy >= 52 and posy <= 68:
##        if posx >= 106 and posx <= 231 and posy >= 52 and posy <= 68:
            display.blit(Highlight,(106,52))
##            display.blit(Highlight,(File[0],(Tool[1]*4)+1)))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ExitClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 106 and posx <= 231 and posy >= 69 and posy <= 85:
##        if posx >= 106 and posx <= 231 and posy >= 69 and posy <= 85:
            display.blit(Highlight,(106,69))
##            display.blit(Highlight,(File[0],(Tool[1]*4)+1)))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ExitClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        display.blit(Load,(106,20))
        display.blit(Load,(106,37))
        display.blit(Load,(106,54))
        display.blit(Load,(106,69))
    ###Run
    if click1 == 4:
        display.blit(Run,(166,1))
##        display.blit(Run,(Run[0],Tool[0]))
        if posx >= 166 and posx <= 291 and posy >= 18 and posy <= 34:
##        if posx >= 166 and posx <= 291 and posy >= 18 and posy <= 34:
            display.blit(Highlight,(166,18))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    LoadClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        if posx >= 166 and posx <= 291 and posy >= 35 and posy <= 51:
##        if posx >= 166 and posx <= 291 and posy >= 35 and posy <= 51:
            display.blit(Highlight,(166,35))
            if click == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    SaveClick()
                    click = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = 0
        display.blit(Load,(166,20))
        display.blit(Load,(166,37))
def LoadClick():
    print "1"
def SaveClick():
    print "1"
def ExitClick():
    pygame.quit()
    sys.exit()

#Main Loop
while True:
    #Quit Function
    for event in pygame.event.get():
        if event.type == QUIT:
            ExitClick()
    
    #Gets Mouse X And Y
    posx, posy = pygame.mouse.get_pos()
    
    #All Things That Will Be Displayed
    ##Refresh the screen
    display.fill(white)
    ##Main Menu
    display.blit(MainMenu,(0,0))
        
    #User Defined Functions
    ##Displays If User Clicks Toolbar
    Toolbar()
    
    #Click Check
    Click()
    
    clock.tick(50)
    pygame.display.flip()
