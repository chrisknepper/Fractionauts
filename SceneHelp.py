import pygame
import os
import pygtk
from Button import Button
from Background import Background
from TextItem import TextItem
from SceneBasic import SceneBasic

class SceneHelp(SceneBasic):

    def __init__(self,screenSize):
        self.buttons = []
        self.background_image = os.path.join('assets', 'startscreen', 'night_sunset_gradient.png')
        self.background = Background(self.background_image)
        self.tutImage = Background('assets/tutorial-images/tut1.jpg',(0.05)*screenSize[0], .05*screenSize[1])
        self.menuBtn = Button(.41*screenSize[0], .83*screenSize[1], .16*screenSize[0], .08*screenSize[1], 'Menu')
        self.backBtn = Button(.25*screenSize[0], .72*screenSize[1], .16*screenSize[0],.08*screenSize[1], 'Back')
        self.nextBtn = Button(.58*screenSize[0], .72*screenSize[1], .16*screenSize[0], .08*screenSize[1], 'Next')
        self.currentScreen = 1
        # Help screen buttons
        self.buttons.append(self.menuBtn)
        self.buttons.append(self.nextBtn)
        self.buttons.append(self.backBtn)

        self.EVENT_MENU =[]
    
    def registerEvent_menu(self,e):self.EVENT_MENU.append(e)

    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            #Help state buttos
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'
                    if button == self.menuBtn:
                        self.helperRaiseEvent(self.EVENT_MENU)

                    if button == self.nextBtn:
                        if self.currentScreen < 6:
                            self.currentScreen+=1
                            print(self.currentScreen)
                            filepath = 'assets/tutorial-images/tut'+str(self.currentScreen)+'.jpg'
                            print 'here'
                            self.tutImage.image = pygame.image.load(filepath)
                            self.tutImage.filename = filepath
                        else:
                            self.currentScreen = 6
                    elif button == self.backBtn:
                        self.currentScreen-=1
                        if self.currentScreen >= 1:
                            filepath = 'assets/tutorial-images/tut'+str(self.currentScreen)+'.jpg'
                            print 'here'
                            self.tutImage.image = pygame.image.load(filepath)
                            self.tutImage.filename = filepath
                        else:
                            self.currentScreen = 1
                            filepath = 'assets/tutorial-images/tut'+str(self.currentScreen)+'.jpg'
                            print 'here'
                            self.tutImage.image = pygame.image.load(filepath)
                            self.tutImage.filename = filepath

                    
                  

    def renderScreen(self,screen):
        self.background.draw(screen)
        self.tutImage.draw(screen)
        if(self.currentScreen == 1):
            for button in self.buttons:
                if button != self.backBtn:
                    button.draw(screen)
        elif(self.currentScreen == 7):
            for button in self.buttons:
                if button != self.nextBtn:
                    button.draw(screen)
        else:
            for button in self.buttons:
                button.draw(screen)



    def EVENT_SCENE_START(self):
        print("entered help screen")