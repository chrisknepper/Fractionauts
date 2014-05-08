from SceneBasic import * 
import pygame
import os
import json

#Utility
import DrawHelper
import HelperVec2

#Logic
from KButton import KButton
from IcnOil import IcnOil
from IcnRocket import IcnRocket


class SceneGame(SceneBasic):
	STATE_READY = 0
	STATE_WINSCREEN = 1
	ICN_RATIO_BARS = (.1, .3)

	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)

		self.myState = self.STATE_READY
		self.currentAnswers = []
		self.last_mousepressed = []
		self.level_loaded = False
		self.levelWon = False
		self.arrIcnOils =[]

		self.questionLevel = 0
		self.questionChoices = []
		self.questionAnswers = []

		self.initIcnOils(self.arrIcnOils,screenSize);
		self.initIcnRocket(screenSize);
		self.initImages(screenSize)


		# Game playing screen buttons
		self.initButtons(screenSize);
		# Game screen text elements
		self.initOthers(screenSize)
		# Game screen elements

	def initOthers(self,screenSize):
		pass

	def helperGetIcnOil(self, pos,size, ratioPos,ratioSize,textureOil,textureBar):
		return IcnOil(pos, size,HelperVec2.mult(size,ratioPos), HelperVec2.mult(size, ratioSize ),textureOil,textureBar )

	def initIcnOils(self,list,screenSize):
		pos = (50,100)
		size = (100,300)
		sizeBar = (size[0]*.5,size[1]*.4)

		self.textureOil = TextureLoader.load( os.path.join('assets', 'screenGame','icnOil.png'),size)
		self.textureBar = TextureLoader.load( os.path.join('assets', 'screenGame','bar.png'),(100,30))

		for i in range(0,3):
			posNew = HelperVec2.add(pos, HelperVec2.mult( size, ((1.11)*i ,0) )  )
			list.append(self.helperGetIcnOil(posNew,size, (.5-.25,.5-.2), (.5,.4) ,self.textureOil ,self.textureBar ))

	def initIcnRocket(self,screenSize):
		pos = (500,100)
		size = (200,400)

		self.textureIdRocket = TextureLoader.load( os.path.join('assets', 'screenGame','icnRocket.png'),size)
		self.textureIdRocketBar = TextureLoader.load( os.path.join('assets', 'screenGame','bar.png'),(100,30))

		self.icnRocket =  IcnRocket( pos,size, HelperVec2.mult(size, (.5-.25,.5-.2)),HelperVec2.mult(size, (.5,.4) ),self.textureIdRocket ,self.textureIdRocketBar)

	def initButtons(s,screenSize):
		size = HelperVec2.mult(screenSize, (.1 ,.1 ))
		s.textureIdButton = TextureLoader.load( os.path.join('assets', 'screenGame','bttn.png'),size)

		s.bttnEmpty =	KButton(.0*screenSize[0],.10*screenSize[1], .15*screenSize[0], .08*screenSize[1],  s.textureIdButton,True)
		s.bttnMenu =	KButton(0*screenSize[0], .90*screenSize[1], .5*screenSize[0], .1*screenSize[1],  s.textureIdButton,True)
		s.bttnDone =	KButton(.5 *screenSize[0], .9*screenSize[1], .5*screenSize[0], .1*screenSize[1], s.textureIdButton,True)
		s.arrButtons = []
		s.arrButtons.append(s.bttnMenu)
		s.arrButtons.append(s.bttnEmpty)
		s.arrButtons.append(s.bttnDone)

	def initImages(self,screenSize):
		self.textureIdBG =		TextureLoader.load(os.path.join('assets','Background.png') ,screenSize)
		self.textureIdRocketFail =	TextureLoader.load( os.path.join('assets', 'rocket_down.png'))
		self.textureIdRocketLaunch =	TextureLoader.load(os.path.join('assets', 'rocket_launch.png'))

	def listenForEvents(s):
		mousePressed = pygame.mouse.get_pressed()
		if(s.isMosueReleased and mousePressed[0] is 1) :
			s.isMosueReleased = False
			s.EVENT_CLICK()
		elif(not s.isMosueReleased and mousePressed[0] is 0):
			s.isMosueReleased = True

	def EVENT_SUBMITT_ANSWER(self):
		if(self.isGameOver() ) : 
			#Submitted answer is correct advnace to the next level and raise win event
			self.questionLevel += 1
			self.helperRaiseEvent(self.EVENT_WIN)
		else : print "GAME IS NOT YET OVER! DISPLAY SOME \"Lets try again GRAPHIC\" "  


	def EVENT_CLICK_ANSWER(self):
		pos = pygame.mouse.get_pos()
		for i in range(0, len( self.arrIcnOils  )) :
			icn = self.arrIcnOils[i]
			if(icn.isUnder(pos)):
				if(icn.select()): 
					icn.display(0)
				else :  icn.display(self.questionChoices[i][0])
				return True
		return False
	

	
	

	def registerEvent_menu(s,e):s.EVENT_MENU.append(e)
	def registerEvent_win(s,e):s.EVENT_WIN.append(e)
	def initEvents(s):
		s.EVENT_MENU=[]
		s.EVENT_WIN=[]

	def EVENT_CLICK_BUTTON_MENU(self):
		self.helperRaiseEvent(self.EVENT_MENU)
	def EVENT_CLICK_BUTTON_EMPTY(self):
		for answer in self.currentAnswers:
			answer.selected = False
		self.goalContainer.fill(0.0)

	def EVENT_CLICK_BUTTON_DONE(self):
		#call button animation here
		self.EVENT_SUBMITT_ANSWER()#then process event 


	def EVENT_CLICK_BUTTONS(self):
		mousePos = pygame.mouse.get_pos()
		bttn_event = [
			[self.bttnMenu, self.EVENT_CLICK_BUTTON_MENU],
			[self.bttnEmpty, self.EVENT_CLICK_BUTTON_EMPTY],
			[self.bttnDone, self.EVENT_CLICK_BUTTON_DONE]]
		for bttn,event in bttn_event:
			if( not bttn.isUnder(mousePos)):continue
			event()
			return  True
		return False


	def EVENT_CLICK(self):
		print "EVENT_CLICK"
		if (self.myState  is self.STATE_READY):
			if(self.EVENT_CLICK_ANSWER()) : pass
			elif (self.EVENT_CLICK_BUTTONS()):pass
		elif (self.myState is self.STATE_WINSCREEN): pass
	def renderScreenBegin(self,screen):
		screen.fill((255, 255, 255)) 
		pygame.display.update()
		print "HI SCREEN BEGIN HERE "
		pass

	def renderScreen(self,screen):
		for icn in self.arrButtons:
			icn.draw(screen);
			icn.drawEnd();

		for icn in self.arrIcnOils:
			icn.draw(screen);
			icn.drawEnd();
		self.icnRocket.draw(screen)
		self.icnRocket.drawEnd()
		pass



	def loadNewQuestion(self,choices,answers,answerNum):
		self.questionChoices	= choices
		self.questionAnswers	= answers

		for i in range(0,3):
			self.arrIcnOils[i].display(choices[i][0],choices[i][1])
		self.icnRocket.display(answerNum[0],answerNum[1])

		pass

	#Load the level-th JSON file in the levels folder
	def loadLevel(self, level):
		print 'loading level' + str(level)
		path = os.path.join('assets/levels', str(level) + '.json')
		try:
			with open(path) as fileQuestion:
				data = json.load(fileQuestion)
				self.loadNewQuestion(data["CHOICES"],data["ANSWERS"],data["ANSWER_NUM"]  )
				fileQuestion.close()
		except IOError:
			new_game = open(path, 'w')
			new_game.close()

	
	
	def helperIsSameArray(self, arrA, arrB):
		if(len(arrA) is not len(arrB)): return False
		for i in range(0, len(arrA)):
			if( arrA[i] is not arrB[i]) :return False
		return True


	def isGameOver(self):
		answerState = []
		for icn in self.arrIcnOils:answerState.append(icn.isSelected)
		for a  in self.questionAnswers:
			if(self.helperIsSameArray(answerState, a) ) :return True
		return False


	def EVENT_NEW_GAME(self, level =-1):
		self.EVENT_SCENE_CHANGE_START()
		self.levelWon = False
		if(level is -1 ) : level = self.questionLevel
		self.loadLevel(level)
		self.EVENT_SCENE_CHANGE_END()

	def EVENT_SCENE_START(self):
		print("entered play state")
		self.EVENT_NEW_GAME()


