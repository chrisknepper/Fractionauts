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
        self.containers = []
        self.currentAnswers = []
        self.level_loaded = False

        # Game playing screen buttons
        self.menuBtn = Button(600, 500, 200, 75, 'Back to Menu')
        self.fillBtn1 = Button(600, 400, 200, 75, 'Fill it 20%')
        self.fillBtn2 = Button(600, 300, 200, 75, 'Fill it 90%')
        self.emptyBtn = Button(600, 200, 200, 75, 'Empty all containers')
        self.doneBtn = Button(600, 600, 200, 75, 'Done')
        self.buttons.append(self.menuBtn)
        self.buttons.append(self.fillBtn1)
        self.buttons.append(self.fillBtn2)
        self.buttons.append(self.emptyBtn)
        self.buttons.append(self.doneBtn)

        # Game screen text elements
        self.scoreDisplay = TextItem(100, 600, 200, 75, 'Score:')
        self.levelDisplay = TextItem(100, 800, 200, 75, 'Current Level:')
        self.gameScreenUI.append(self.scoreDisplay)
        self.gameScreenUI.append(self.levelDisplay)

        # Game screen elements
        self.mainContainer = Container(1000, 200, 0.5)
        self.containers.append(self.mainContainer)
        self.goalFill = 0.9 #temporary goal fill amount


    def listenForEvents(self):
        if self.level_loaded and 1 in pygame.mouse.get_pressed():
            #Play state buttons
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'

                    #Menu button
                    if button == self.menuBtn:
                        self.main.set_mode('menu')

                    #Fill 20% button
                    elif button == self.fillBtn1:
                        self.mainContainer.fill(0.2)

                    #Fill 90% button
                    elif button == self.fillBtn2:
                        self.mainContainer.fill(0.9)

                    #Empty button
                    elif button == self.emptyBtn:
                        for container in self.containers:
                            container.fill(0.0)

                    #Done button
                    #Evaluate the answer. If correct, return to main menu
                    # if incorrect, do nothing for now
                    elif button == self.doneBtn:
                        if self.evaluateAnswer():
                            self.main.set_mode('menu')


    def renderScreen(self):
        self.main.screen.fill((206, 156, 60))
        for container in self.containers:
            container.draw(self.main.screen)
        for button in self.buttons:
            button.draw(self.main.screen)
        for item in self.gameScreenUI:
            item.draw(self.main.screen)
        for answer in self.currentAnswers:
            answer.draw(self.main.screen)
        if not self.level_loaded:
            self.main.screen.fill((0, 0, 0))



    #Load the level-th "levels" object in the save file
    def loadLevel(self, level):
        print 'loading level'
        path = self.main.savePath
        try:
            with open(path) as saved_game:
                save_data = json.load(saved_game)
                print(save_data)
                level_data = save_data.get('levels')[level]
                self.currentAnswers = []
                counter = 0
                for answer in level_data["options"]:
                    if(counter < 3):
                        temp_y = 0
                        temp_x = 0 + (counter * 300)
                    else:
                        temp_y = 350
                        temp_x = 0 + ((counter - 3) * 300)
                    temp = Container(temp_x, temp_y, answer)
                    self.currentAnswers.append(temp)
                    counter = counter + 1
                saved_game.close()
                self.level_loaded = True
        except IOError:
            new_game = open(path, 'w')
            new_game.close()

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


    #Compare the main container's current filled percentage with the goal filled percentage
    def evaluateAnswer(self):
        return self.mainContainer.filled == self.goalFill


    def enter(self):
        print("entered play state")
        self.loadLevel(self.main.currentLevel)


