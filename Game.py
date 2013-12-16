import pygame
import os
import json
from gi.repository import Gtk
from Button import Button
from Container import *
from Question import Question
from AnswerButton import AnswerButton
from Background import Background
from TextItem import TextItem


class Game(object):

    def __init__(self, main):
        self.main = main
        self.buttons = []
        self.gameScreenUI = []
        self.currentAnswers = []
        self.level_loaded = False
        self.last_mousepressed = []
        self.levelWon = False

        # Game playing screen buttons
        self.emptyBtn = Button(750, 825, 200, 75, 'Reset')
        self.menuBtn = Button(950, 825, 250, 75, 'Back to Menu')
        self.doneBtn = Button(915, 625, 250, 75, 'Check Answer')
        self.buttons.append(self.menuBtn)
        self.buttons.append(self.emptyBtn)
        self.buttons.append(self.doneBtn)

        # Game screen text elements
        self.scoreDisplay = TextItem(700, 0, 200, 75, 'Score: ')
        self.levelDisplay = TextItem(900, 0, 300, 75, 'Current Level: ')
        self.goalDisplay = TextItem(950, 240, 177, 60, 'Fill to: ')
        self.gameScreenUI.append(self.goalDisplay)
        self.gameScreenUI.append(self.scoreDisplay)
        self.gameScreenUI.append(self.levelDisplay)
        self.winScreen = TextItem(self.main.width / 2 - 400, 100, 800, 600, 'You Beat the Level! Click inside this box to go on!', (152, 151, 151), (59, 59, 59), True)
        self.winScreen.close()
        # Game screen elements
        self.goalContainer = Container(950, 300, 0, 1, 177, 259, False)
        self.goalFill = 1.0 #temporary goal fill amount #the number you are aiming for


    def listenForEvents(self):
        if self.level_loaded and 1 in pygame.mouse.get_pressed()\
            and not (1 in self.last_mousepressed):
            for answer in self.currentAnswers:
                if answer.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + answer.text + ' answer'
                    answer.selected = not answer.selected
                    if answer.selected:
                        self.goalContainer.fill(self.goalContainer.filled+answer.filled)
                    else:
                        self.goalContainer.fill(self.goalContainer.filled-answer.filled)

            if self.winScreen.drawing == True and self.winScreen.is_under(pygame.mouse.get_pos()):
                self.winScreen.close()
                if(self.checkLevelExists(self.main.currentLevel + 1)):
                    self.main.currentLevel = self.main.currentLevel + 1
                    self.main.set_mode('play')
                else:
                    self.main.currentLevel = 0
                    self.main.set_mode('menu')

            #Play state buttons
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'

                    #Menu button
                    if button == self.menuBtn:
                        self.main.set_mode('menu')

                    #Empty button
                    elif button == self.emptyBtn:
                        for answer in self.currentAnswers:
                            answer.selected = False
                        self.goalContainer.fill(0.0)

                    #Done button
                    #Evaluate the answer. If correct, return to main menu
                    # if incorrect, do nothing for now
                    elif button == self.doneBtn:
                        if self.evaluateAnswer():
                            self.winScreen.open()
                            self.levelWon == True
        self.last_mousepressed = pygame.mouse.get_pressed()


    def renderScreen(self):
        self.main.screen.fill((206, 156, 60))
        self.goalContainer.draw(self.main.screen)
        for button in self.buttons:
            button.draw(self.main.screen)
        for answer in self.currentAnswers:
            answer.draw(self.main.screen)
        for item in self.gameScreenUI:
            item.draw(self.main.screen)
            if(self.winScreen.drawing == True):
                self.winScreen.draw(self.main.screen)
        if not self.level_loaded:
            self.main.screen.fill((0, 0, 0))



    #Load the level-th JSON file in the levels folder
    def loadLevel(self, level):
        print 'loading level'
        load_file = str(level) + '.json'
        path = os.path.join('assets/levels', load_file)
        try:
            with open(path) as level_file:
                level_data = json.load(level_file)
                self.currentAnswers = []
                self.arrangeAnswers(level_data["options"], 3, 75, 125, 225, 375)
                answer = level_data["answer"].split("/")
                self.goalFill = float(answer[0])/float(answer[1])
                self.goalDisplay.setText("Fill to: "+answer[0]+"/"+answer[1])
                print self.goalFill
                level_file.close()
                self.level_loaded = True
                self.levelDisplay.setText("Current Level: " + str(self.main.currentLevel + 1))
        except IOError:
            new_game = open(path, 'w')
            new_game.close()

    def checkLevelExists(self, level):
        return os.path.exists(os.path.join('assets/levels', str(level) + '.json'))

    def saveLevel(self):
        path = self.main.savePath
        try:
            with open(path, 'w') as saved_game:
                save_data = json.load(saved_game)
                save_data['current_level'] = self.main.currentLevel
                json.dump(save_data, save_data)
        except IOError:
            new_game = open(path, 'w')
            save_data['current_level'] = self.main.currentLevel
            new_game.close()

    #Arrange passed-in answers array in a grid with sensible default options
    def arrangeAnswers(self, answers, perRow = 3, base_x = 100, \
                       base_y = 50, h_spacing = 200, v_spacing = 350):
        #Starting our counter variables at 1 to avoid an additional if block 
        #(because we can never divide by 0 this way)
        counter = 1
        currentRow = 1
        posInCurrentRow = -1 #Initialize current row position to -1 
                             #so first answer isn't offset incorrectly
        for answer in answers:
            answer = answer.split("/")#get numerator and denominator
            if(counter > currentRow * perRow):
                currentRow = currentRow + 1
                posInCurrentRow = 0
            else:
                posInCurrentRow = posInCurrentRow + 1
            answer_x = base_x + (h_spacing * posInCurrentRow)
            answer_y = base_y + ((currentRow - 1) * v_spacing)
            temp = Container(answer_x, answer_y, int(answer[0]), int(answer[1]))
            self.currentAnswers.append(temp)
            counter = counter + 1


    #Compare the main container's current filled percentage with the goal filled percentage
    def evaluateAnswer(self):
        #later we should have a more solid way to deal with float errors
        print str(round(self.goalContainer.filled, 5))+" == "+str(round(self.goalFill, 5))
        print round(self.goalContainer.filled, 5) == round(self.goalFill, 5)
        return round(self.goalContainer.filled, 5) == round(self.goalFill, 5)


    def enter(self):
        print("entered play state")
        self.levelWon = False
        self.loadLevel(self.main.currentLevel)
        self.goalContainer.fill(0)


