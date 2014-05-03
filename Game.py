import pygame
import os
import json
import pygtk
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
        self.failed_rocket = os.path.join('assets', 'rocket_down.png')
        self.launching_rocket = os.path.join('assets', 'rocket_launch.png')
        self.background_image = os.path.join('assets','Background.png')
        self.background = Background(self.background_image)
        self.background_rocket = Background(self.launching_rocket, 800, 675 - (self.main.currentLevel * 100))
        print 'currentLevel is ' + str(self.main.currentLevel)

        # Game playing screen buttons
        self.emptyBtn = Button(750, 725, 200, 75, 'Reset', (206, 148, 73), (109, 78, 38))
        self.menuBtn = Button(950, 725, 250, 75, 'Back to Menu', (202, 198, 82), (85, 83, 34))
        self.doneBtn = Button(915, 625, 250, 75, 'Check Answer', (7,208,226), (4,111,121))
        self.buttons.append(self.menuBtn)
        self.buttons.append(self.emptyBtn)
        self.buttons.append(self.doneBtn)

        # Game screen text elements
        self.scoreDisplay = TextItem(650, 10, 200, 75, ['Score: '], showRect = False)
        self.levelDisplay = TextItem(850, 10, 300, 75, ['Current Level: '], showRect = False)
        self.goalDisplay = TextItem(950, 240, 177, 60, ['Fill to: '], textColor= (255,255,255), showRect = False)
        self.feedback_width = 600
        self.feedback_height = 200
        self.feedback_x = (self.main.width / 2) - (self.feedback_width / 2)
        self.feedback_y = (self.main.height / 2) - (self.feedback_height / 2)
        self.gameScreenUI.append(self.goalDisplay)
        self.gameScreenUI.append(self.scoreDisplay)
        self.gameScreenUI.append(self.levelDisplay)
        self.winScreen = TextItem(self.feedback_x, self.feedback_y, self.feedback_width, self.feedback_height, ['Nice Job!', 'Click here to go on!'], (84, 194, 92), (39, 90, 43), True, Background(self.launching_rocket, self.feedback_x, self.feedback_y, self.feedback_width / 2, 100))
        self.winScreen.close()
        self.loseScreen = TextItem(self.feedback_x, self.feedback_y, self.feedback_width, self.feedback_height, ['Oops, that\'s not quite right.', 'Click here and try again.'], (209, 72, 72), (96, 33, 33), True, Background(self.failed_rocket, self.feedback_x, self.feedback_y, self.feedback_width / 2, 100))
        self.loseScreen.close()

        # Game screen elements
        self.goalContainer = Container(950, 300, 0, 1, 177, 259, False)
        self.goalFill = 1.0 #temporary goal fill amount #the number you are aiming for

        # Timer Bonus
        self.timer = 0;
        self.secondsTillNoBonus = 10; 
        

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
                    self.main.currentLevel += 1
                    self.main.set_mode('play')
                else:
                    self.main.currentLevel = 0
                    self.main.set_mode('scoreboard')
            if self.loseScreen.drawing == True and self.loseScreen.is_under(pygame.mouse.get_pos()):
                # close lose screen.
                self.loseScreen.close()

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
                    #Evaluate the answer.
                    #Scores are increased with timer bonus
                    elif button == self.doneBtn:
                        if self.evaluateAnswer():
                            if self.levelWon != True:
                                self.winScreen.open()
                                self.levelWon = True
                                addition = 50;
                                timerBonus = self.timer + self.secondsTillNoBonus * 1000 - pygame.time.get_ticks();
                                if timerBonus < 0:
                                    timerBonus = 0;
                                #add the normalized timer bonus to addition of scores
                                addition += ( timerBonus / float( self.secondsTillNoBonus * 1000 ) ) * addition;
                                self.main.score = str(int(self.main.score) + int(addition))
                        else:
                            self.loseScreen.open()
                            print 'WRONG ANSWER'
        self.last_mousepressed = pygame.mouse.get_pressed()


    def renderScreen(self):
        self.main.screen.fill((206, 156, 60))
        self.background.draw(self.main.screen)
        self.background_rocket.draw(self.main.screen)
        self.goalContainer.draw(self.main.screen)
        for button in self.buttons:
            button.draw(self.main.screen)
        for answer in self.currentAnswers:
            answer.draw(self.main.screen)
        for item in self.gameScreenUI:
            item.draw(self.main.screen)
            if(self.winScreen.drawing == True):
                self.winScreen.draw(self.main.screen)
            if(self.loseScreen.drawing == True):
                self.loseScreen.draw(self.main.screen)
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
                self.goalDisplay.setText(["Fill to: "+answer[0]+"/"+answer[1]])
                print self.goalFill
                level_file.close()
                self.level_loaded = True
                self.background_rocket.y = 600 - (self.main.currentLevel * 50)
                self.levelDisplay.setText(["Current Level: " + str(self.main.currentLevel + 1)])
                self.scoreDisplay.setText((["Score: " + str(self.main.score)]))
        except IOError:
            new_game = open(path, 'w')
            new_game.close()

    def checkLevelExists(self, level):
        return os.path.exists(os.path.join('assets/levels', str(level) + '.json'))

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
        self.timer = pygame.time.get_ticks();