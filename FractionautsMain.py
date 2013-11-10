#!/usr/bin/python
#Fractionauts Main Class
import pygame
from gi.repository import Gtk
import random
from fractions import Fraction
from decimal import Decimal
from Button import *
from Container import *

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

class Question:
    def __init__(self,questionType):
        numChoices = 6
        numCorrect = random.randint(2,4)
        correctAnswers = []
        incorrectAnswers =[]
        print numCorrect

        section = float(1)/float(numCorrect)

        for i in range(0,numCorrect):
            fraction = round(random.uniform(0.1,section),2)
            correctAnswers.append(fraction)
            print(fraction)

        print correctAnswers

        goal = sum(correctAnswers)
        print goal

        dummyQuestions = numChoices - numCorrect
        print dummyQuestions

        for i in range(0,dummyQuestions):
            fraction = round(random.uniform(0.1,0.9),2)
            incorrectAnswers.append(fraction)

        print incorrectAnswers



class FractionautsMain:
    def __init__(self):
        self.needsUpdate = False
        self.initialized = False
        self.screen = pygame.display.get_surface()
        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w
        self.hcenter = self.width / 2
        self.vcenter = self.height / 2
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.menuButtons = []
        self.gameScreenButtons = []
        self.helpScreenButtons = []
        self.containers = []

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0
        self.mode = 'menu'
        self.paused = False
        self.direction = 1

        #Main menu buttons
        self.playBtn = Button(self.hcenter - (75*1.5), self.vcenter - 100, 200, 75, 'Play')
        self.howBtn = Button(self.hcenter - (75*1.5), self.vcenter, 200, 75, 'How to Play')
        self.quitBtn = Button(self.hcenter - (75*1.5), self.vcenter + 100, 200, 75, 'Quit')
        self.menuButtons.append(self.playBtn)
        self.menuButtons.append(self.howBtn)
        self.menuButtons.append(self.quitBtn)

        #Game playing screen buttons
        self.menuBtn = Button(300, 500, 200, 75, 'Back to Menu')
        self.fillBtn1 = Button(300, 400, 200, 75, 'Fill it 20%')
        self.fillBtn2 = Button(300, 300, 200, 75, 'FIll it 90%')
        self.emptyBtn = Button(300, 200, 200, 75, 'Empty all containers')
        self.gameScreenButtons.append(self.menuBtn)
        self.gameScreenButtons.append(self.fillBtn1)
        self.gameScreenButtons.append(self.fillBtn2)
        self.gameScreenButtons.append(self.emptyBtn)

        #Help screen buttons
        self.helpScreenButtons.append(self.menuBtn)

        #Game screen elements
        self.mainContainer = Container(200, 200, 100, 300, 0.5)
        self.containers.append(self.mainContainer)

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.textSurfaceObj = fontObj.render('Fractionauts', True, GREEN, BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.hcenter, 150)

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.listenForEvents()
            self.renderScreen()
            pygame.display.flip()

    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            if self.mode == 'menu':
                for button in self.menuButtons:
                    if button.is_under(pygame.mouse.get_pos()):
                        print 'You clicked the ' + button.text + ' button'
                        if button == self.quitBtn:
                            self.running = False
                            pygame.quit()
                            exit()
                        elif button == self.playBtn:
                            self.mode = 'play'
                        elif button == self.howBtn:
                            self.mode = 'help'
            elif self.mode == 'play':
                for button in self.gameScreenButtons:
                    if button.is_under(pygame.mouse.get_pos()):
                        print 'You clicked the ' + button.text + ' button'
                        if button == self.menuBtn:
                            self.mode = 'menu'
                        elif button == self.fillBtn1:
                            self.mainContainer.fill(0.2)
                        elif button == self.fillBtn2:
                            self.mainContainer.fill(0.9)
                        elif button == self.emptyBtn:
                            for container in self.containers:
                                container.fill(0.0)
            elif self.mode == 'help':
                for button in self.helpScreenButtons:
                    if button.is_under(pygame.mouse.get_pos()):
                        print 'You clicked the ' + button.text + ' button'
                        if button == self.menuBtn:
                            self.mode = 'menu'

    def renderScreen(self):
        if self.mode == 'menu':
            self.screen.fill((255, 255, 255))  # 255 for white
            self.screen.blit(self.textSurfaceObj, self.textRectObj);
            for button in self.menuButtons:
                button.draw(self.screen)
        elif self.mode == 'play':
            self.screen.fill((206, 156, 60))
            for container in self.containers:
                container.draw(self.screen)
            for button in self.gameScreenButtons:
                button.draw(self.screen)
        elif self.mode == 'help':
            self.screen.fill((34, 215, 217))
            for button in self.helpScreenButtons:
                button.draw(self.screen)



# This function is called when the game is run directly from the command line:
# ./FractionautsMain.py
def main():
    question = Question("multiplication")
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = FractionautsMain()
    game.run()

if __name__ == '__main__':
    main()
