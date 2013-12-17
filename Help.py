import pygame
import os
from gi.repository import Gtk
from Button import Button
from Background import Background
from TextItem import TextItem


class Help(object):

    def __init__(self, main):
        self.main = main
        self.buttons = []
        self.background_image = os.path.join('assets', 'startscreen', 'night_sunset_gradient.png')
        self.background = Background(self.background_image)
        self.tut = pygame.image.load(os.path.join('assets', 'tutorial-images', 'tut1.jpg'))
        self.menuBtn = Button(500, 750, 200, 75, 'Menu')
        self.backBtn = Button(300, 650, 200,75, 'Back')
        self.nextBtn = Button(700, 650, 200, 75, 'Next')
        self.currentScreen = 1
        # Help screen buttons
        self.buttons.append(self.menuBtn)
        self.buttons.append(self.nextBtn)
        self.buttons.append(self.backBtn)


    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            #Help state buttos
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'
                    if button == self.menuBtn:
                        self.main.set_mode('menu')

                    
                  

    def renderScreen(self):
        self.background.draw(self.main.screen)
        self.main.screen.blit(self.tut, (self.main.hcenter - 400, 50))
        for button in self.buttons:
            if button != self.backBtn:
                button.draw(self.main.screen)


    def enter(self):
        print("entered help screen")