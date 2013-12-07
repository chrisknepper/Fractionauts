import pygame
import os
from gi.repository import Gtk
from Button import Button
from Background import Background
from TextItem import TextItem
from ScrollingImage import ScrollingImage


class MainMenu(object):

    def __init__(self, main):
        self.main = main
        self.buttons = []


        # Main menu buttons
        self.playBtn = Button(
            self.main.hcenter - (75 * 1.5), self.main.vcenter - 100, 200, 75, 'Play')
        self.howBtn = Button(
            self.main.hcenter - (75 * 1.5), self.main.vcenter, 200, 75, 'How to Play')
        self.quitBtn = Button(
            self.main.hcenter - (75 * 1.5), self.main.vcenter + 100, 200, 75, 'Quit')
        self.buttons.append(self.playBtn)
        self.buttons.append(self.howBtn)
        self.buttons.append(self.quitBtn)


        #Load in Title Image and background images
        self.logo = pygame.image.load(os.path.join('assets', 'startscreen', 'Title.png'))
        self.startbg = pygame.image.load(os.path.join('assets', 'startscreen', \
                                                      'night_sunset_gradient.png'))
        self.stars_tiny =  ScrollingImage( \
                           pygame.image.load(os.path.join('assets', 'startscreen', \
                                           'stars_tiny.png')), (-50,-50), float(.004))
        self.stars_small = ScrollingImage( \
                           pygame.image.load(os.path.join('assets', 'startscreen', \
                                           'stars_small.png')), (-50,-50), float(.008))
        self.stars_medium = ScrollingImage( \
                            pygame.image.load(os.path.join('assets', 'startscreen', \
                                           'stars_medium.png')), (-50,-50), float(.012))
        self.stars_big = ScrollingImage( \
                         pygame.image.load(os.path.join('assets', 'startscreen', \
                                          'stars_big.png')), (-50,-50), float(.016))
        self.sunsetoverlay = pygame.image.load(os.path.join('assets', 'startscreen', \
                                                            'sunset_overlay.png'))


    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            #Menu state buttons
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'
                    
                    #Quit button
                    if button == self.quitBtn:
                        self.running = False
                        pygame.quit()
                        exit()
                        
                    #Play button
                    elif button == self.playBtn:
                        self.main.set_mode('play')
                        #self.loadLevel(int(self.currentLevel))

                    #How button
                    elif button == self.howBtn:
                        self.main.set_mode('help');
                         

    def renderScreen(self):
        self.main.screen.fill((255, 255, 255))  # 255 for white
        self.main.screen.blit(self.startbg, (0, 0))
        self.stars_tiny.draw(self.main.screen, pygame.time.get_ticks());
        self.stars_small.draw(self.main.screen, pygame.time.get_ticks());
        self.stars_medium.draw(self.main.screen, pygame.time.get_ticks());
        self.stars_big.draw(self.main.screen, pygame.time.get_ticks());
        #self.main.screen.blit(self.sunsetoverlay, (0, 0)) # this might make it too dim
        self.main.screen.blit(self.logo, (self.main.hcenter - 300, 150))
        for button in self.buttons:
            button.draw(self.main.screen)

    def enter(self):
        print("entered main menu")



