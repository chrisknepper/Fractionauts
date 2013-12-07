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

        self.menuBtn = Button(600, 500, 200, 75, 'Back to Menu')
        # Help screen buttons
        self.buttons.append(self.menuBtn)


    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            #Help state buttons
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'
                    if button == self.menuBtn:
                        self.main.set_mode('menu')
                  

    def renderScreen(self):
        self.main.screen.fill((34, 215, 217))
        for button in self.buttons:
            button.draw(self.main.screen)


    def enter(self):
        print("entered help screen")

