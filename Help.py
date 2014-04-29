import pygame
import os
import pygtk
import time
from Button import Button
from Background import Background
from TextItem import TextItem


class Help(object):

    def __init__(self, main):
        self.main = main
        self.buttons = []
        self.background_image = os.path.join('assets', 'startscreen', 'night_sunset_gradient.png')
        self.background = Background(self.background_image)
        self.tutImage = Background('assets/tutorial-images/tut1.jpg',self.main.hcenter - 400, 50)
        self.menuBtn = Button(500, 750, 200, 75, 'Menu')
        self.backBtn = Button(300, 650, 200,75, 'Back')
        self.nextBtn = Button(700, 650, 200, 75, 'Next')
	
	self.exitBtn = Button(900, 650, 200, 75, 'Exit')

        self.currentScreen = 1
        # Help screen buttons
        self.buttons.append(self.menuBtn)
        self.buttons.append(self.nextBtn)
        self.buttons.append(self.backBtn)
	self.buttons.append(self.exitBtn)


    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            #Help state buttos
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'
		    if button == self.exitBtn and self.currentScreen == 6:
			self.main.set_mode('menu')                    
                    if button == self.nextBtn:
                        if self.currentScreen < 6:
                            self.currentScreen+=1
                            print(self.currentScreen)
                            filepath = 'assets/tutorial-images/tut'+str(self.currentScreen)+'.jpg'
                            print 'here'
                            self.tutImage.image = pygame.image.load(filepath)
                            self.tutImage.filename = filepath
			    time.sleep(.25) #pause for second
                        else:
                            self.currentScreen = 6
			    time.sleep(.25) #pause for second
                    elif button == self.backBtn:
                        self.currentScreen-=1
                        if self.currentScreen >= 1:
                            filepath = 'assets/tutorial-images/tut'+str(self.currentScreen)+'.jpg'
                            print 'here'
                            self.tutImage.image = pygame.image.load(filepath)
                            self.tutImage.filename = filepath
			    time.sleep(.25) #pause for second
                        else:
                            self.currentScreen = 1
                            filepath = 'assets/tutorial-images/tut'+str(self.currentScreen)+'.jpg'
                            print 'here'
                            self.tutImage.image = pygame.image.load(filepath)
                            self.tutImage.filename = filepath
			    time.sleep(.25) #pause for second

                    
                  

    def renderScreen(self):
        self.background.draw(self.main.screen)
        self.tutImage.draw(self.main.screen)
        if(self.currentScreen == 1):
            for button in self.buttons:
                if button != self.backBtn and button != self.exitBtn:
                    button.draw(self.main.screen)
	elif(self.currentScreen != 1 and self.currentScreen != 6):
	    for button in self.buttons:
                if button != self.exitBtn:
                    button.draw(self.main.screen)
        elif(self.currentScreen == 6):
            for button in self.buttons:
                if button != self.nextBtn:
                    button.draw(self.main.screen)
        else:
            for button in self.buttons:
                button.draw(self.main.screen)



    def enter(self):
        print("entered help screen")
