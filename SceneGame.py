from SceneBasic import * 
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
import DrawHelper
import HelperVec2
from IcnBars import IcnBars
#class Background keeps rescaling itself
#instances of holder for temporary values being saved as class componenet
#having fucking long ridiculous listen function call idiotic


class SceneGame(SceneBasic):
	STATE_READY = 0
	STATE_WINSCREEN = 1
	def __init__(self,screenSize):
		self.myState = self.STATE_READY
		self.initEvents();
		self.currentAnswers = []
		self.last_mousepressed = []
		self.level_loaded = False
		self.levelWon = False
		self.initBase()
		self.initImages(screenSize)
		#self.failed_rocket = os.path.join('assets', 'rocket_down.png')
		#self.launching_rocket = os.path.join('assets', 'rocket_launch.png')
		#self.background_image = os.path.join('assets','Background.png')


		# Game playing screen buttons
		self.initButtons(screenSize);
		# Game screen text elements
		self.initOthers(screenSize)
		# Game screen elements

	def initOthers(self,screenSize):
		self.scoreDisplay = TextItem(.5 *screenSize[0],	0, .14*screenSize[0], .08*screenSize[1], ['Score: '], showRect = False)
		self.levelDisplay = TextItem(.64*screenSize[0],	0  , .21*screenSize[0], .08*screenSize[1], ['Current Level: '], showRect = False)
		self.goalDisplay = TextItem(.67 *screenSize[0],.26*screenSize[1], .12*screenSize[0], .08*screenSize[1], ['Fill to: '], textColor= (255,255,255), showRect = False)
		self.feedback_width = .42 *screenSize[0]
		self.feedback_height = .22*screenSize[1]
		self.feedback_x = (screenSize[0] / 2) - (self.feedback_width / 2)
		self.feedback_y = (screenSize[1] / 2) - (self.feedback_height / 2)
		self.gameScreenUI = []
		self.gameScreenUI.append(self.goalDisplay)
		self.gameScreenUI.append(self.scoreDisplay)
		self.gameScreenUI.append(self.levelDisplay)
		
		self.goalContainer = Container(.67 * screenSize[0], .33*screenSize[1], 0, 1, .12*screenSize[0], .28*screenSize[1], False)
		self.goalFill = 1.0 #temporary goal fill amount #the number you are aiming for

		self.winScreen = TextItem(self.feedback_x, self.feedback_y, self.feedback_width, self.feedback_height, ['Nice Job!', 'Click here to go on!'])
		self.winScreen.close()
		self.loseScreen = TextItem(self.feedback_x, self.feedback_y, self.feedback_width, self.feedback_height, ['Oops, that\'s not quite right.', 'Click here and try again.'])
		self.loseScreen.close()

		self.IcnBars = IcnBars(0,0, 100,300,10)

		#self.winScreen = TextItem(self.feedback_x, self.feedback_y, self.feedback_width, self.feedback_height, ['Nice Job!', 'Click here to go on!'], (84, 194, 92), (39, 90, 43), True, Background(self.launching_rocket, self.feedback_x, self.feedback_y, self.feedback_width / 2, 100))
		#self.winScreen.close()
		#self.loseScreen = TextItem(self.feedback_x, self.feedback_y, self.feedback_width, self.feedback_height, ['Oops, that\'s not quite right.', 'Click here and try again.'], (209, 72, 72), (96, 33, 33), True, Background(self.failed_rocket, self.feedback_x, self.feedback_y, self.feedback_width / 2, 100))
		#self.loseScreen.close()
		pass

	def initButtons(s,screenSize):
		s.bttnEmpty = Button(.53*screenSize[0],.80*screenSize[1], .15*screenSize[0], .08*screenSize[1], 'Reset', (206, 148, 73), (109, 78, 38))
		s.bttnMenu = Button(.76*screenSize[0], .80*screenSize[1], .17*screenSize[0], .08*screenSize[1], 'Back to Menu', (202, 198, 82), (85, 83, 34))
		s.bttnDone = Button(.66 *screenSize[0], .70*screenSize[1], .17*screenSize[0], .08*screenSize[1], 'Check Answer', (7,208,226), (4,111,121))
		s.buttons = []
		s.buttons.append(s.bttnMenu)
		s.buttons.append(s.bttnEmpty)
		s.buttons.append(s.bttnDone)

	def initImages(self,screenSize):
		self.textureIdBG =		TextureLoader.load(os.path.join('assets','Background.png') ,screenSize)
		self.textureIdRocketFail =	TextureLoader.load( os.path.join('assets', 'rocket_down.png'))
		self.textureIdRocketLaunch =	TextureLoader.load(os.path.join('assets', 'rocket_launch.png'))
		#self.failed_rocket = os.path.join('assets', 'rocket_down.png')
		#self.launching_rocket = os.path.join('assets', 'rocket_launch.png')
		#self.background_image = os.path.join('assets','Background.png')

		#self.background = Background(self.background_image)
		#self.background_rocket = Background(self.launching_rocket, 800, 675 - (self.main.currentLevel * 100))
		
		
		pass;
	def initBase(s):
		s.isMosueReleased = True

	def listenForEvents(s):
		mousePressed = pygame.mouse.get_pressed()
		if(s.isMosueReleased and mousePressed[0] is 1) :
			s.isMosueReleased = False
			s.EVENT_CLICK()
		elif(not s.isMosueReleased and mousePressed[0] is 0):
			s.isMosueReleased = True

	def EVENT_CLICK_ANSWER(self):
		pos = pygame.mouse.get_pos()
		for answer in self.currentAnswers:
			if answer.is_under(pos):
				if(answer.helperSelect()):
					self.goalContainer.fill(self.goalContainer.filled+answer.filled)
				else: self.goalContainer.fill(self.goalContainer.filled-answer.filled)
		pass
	


	def EVENT_CLICK_WINSCREEN(self):
		print "WINSCREEN"
		pos = pygame.mouse.get_pos()
		if(self.winScreen.is_under(pos) or self.loseScreen.is_under(pos)):
			self.winScreen.close()
			self.loseScreen.close()
			self.myState = self.STATE_READY
			if(self.evaluateAnswer()):
				self.EVENT_NEW_GAME();
			#if user won
			#if(self.checkLevelExists(self.main.currentLevel + 1)):
			#	self.main.currentLevel += 1
			#	self.main.set_mode('play')
			#else:
			#	self.main.currentLevel = 0
			#	self.main.set_mode('menu')

	

	def registerEvent_menu(s,e):s.EVENT_MENU.append(e)
	def initEvents(s):
		s.EVENT_MENU=[]

	def EVENT_CLICK_BUTTON_MENU(self):
		self.helperRaiseEvent(self.EVENT_MENU)
	def EVENT_CLICK_BUTTON_EMPTY(self):
		for answer in self.currentAnswers:
			answer.selected = False
		self.goalContainer.fill(0.0)

	def EVENT_CLICK_BUTTON_DONE(self):
		self.myState = self.STATE_WINSCREEN
		if self.evaluateAnswer():
			self.winScreen.open()
			self.levelWon = True
			#self.main.score = str(int(self.main.score) + 5)
		else:
			self.loseScreen.open()
			print 'WRONG ANSWER'

	def EVENT_CLICK_BUTTONS(self):
		mousePos = pygame.mouse.get_pos()
		bttn_event = [
			[self.bttnMenu, self.EVENT_CLICK_BUTTON_MENU],
			[self.bttnEmpty, self.EVENT_CLICK_BUTTON_EMPTY],
			[self.bttnDone, self.EVENT_CLICK_BUTTON_DONE]]
		for bttn,event in bttn_event:
			if( not bttn.is_under(mousePos)):continue
			event();
			break


	def EVENT_CLICK(self):
		print "EVENT_CLICK"
		if (self.myState  is self.STATE_READY):
			self.EVENT_CLICK_ANSWER()
			self.EVENT_CLICK_BUTTONS()
			pass
		elif (self.myState is self.STATE_WINSCREEN):
			self.EVENT_CLICK_WINSCREEN()
			pass
	def renderScreenBegin(self,screen):
		screen.fill((255, 255, 255)) 
		pygame.display.update()
		print "HI SCREEN BEGIN HERE "
		pass

	def renderScreen(self,screen):
		self.IcnBars.draw(screen)
		self.IcnBars.drawEnd()
		pass





	#Load the level-th JSON file in the levels folder
	def loadLevel(self, level):
		print 'loading level'
		load_file = str(level) + '.json'
		path = os.path.join('assets/levels', load_file)
		try:
			with open(path) as level_file:
				level_data = json.load(level_file)
				self.currentAnswers = []
				self.arrangeAnswers(level_data["options"], 3, 10,50, 150, 210)
				answer = level_data["answer"].split("/")
				self.goalFill = float(answer[0])/float(answer[1])
				self.goalDisplay.setText(["Fill to: "+answer[0]+"/"+answer[1]])
				print self.goalFill
				level_file.close()
				self.level_loaded = True
				#self.background_rocket.y = 600 - (self.main.currentLevel * 50)
				#self.levelDisplay.setText(["Current Level: " + str(self.main.currentLevel + 1)])
				#self.scoreDisplay.setText((["Score: " + str(self.main.score)]))
		except IOError:
			new_game = open(path, 'w')
			new_game.close()

	def checkLevelExists(self, level):
		return os.path.exists(os.path.join('assets/levels', str(level) + '.json'))

	#Arrange passed-in answers array in a grid with sensible default options
	def arrangeAnswers(self, answers, perRow , base_x,  base_y , h_spacing, v_spacing):
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


	def EVENT_NEW_GAME(self, level =0):
		self.EVENT_SCENE_CHANGE_START()
		self.levelWon = False
		self.loadLevel(level)
		self.goalContainer.fill(0)
		self.EVENT_SCENE_CHANGE_END()

	def EVENT_SCENE_START(self):
		print("entered play state")
		self.EVENT_NEW_GAME()


