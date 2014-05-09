from SceneBasic import * 
import pygame
import os
import json

#Utility
import DrawHelper
import HelperVec2
import HelperTexture

#Logic
from KButton import KButton
from IcnFuel import IcnFuel
from IcnRocket import IcnRocket
from IcnTextBox import IcnTextBox

class SceneGame(SceneBasic):

	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)

		self.arrIcnFuels =[]

		self.score = 0
		self.questionLevel = 0
		self.questionChoices = []
		self.questionAnswers = []

		self.initIcnFuels(self.arrIcnFuels,screenSize);
		self.initIcnRocket(screenSize);
		self.initImages(screenSize)
		self.initIcnText(screenSize)
		self.initButtons(screenSize)

	def helperGetIcnFuel(self, pos,size, ratioPos,ratioSize,textureBG,textureDiv, textureFill,textureWave):
		return IcnFuel(pos, size,HelperVec2.mult(size,ratioPos), HelperVec2.mult(size, ratioSize ),textureBG,textureDiv,textureFill,textureWave )

	def initIcnFuels(s,list,screenSize):
		pos = HelperVec2.mult(screenSize, (.1, .3) )
		size = HelperVec2.mult(screenSize, (.1, .3) )
		barPos =  HelperVec2.mult(size, (.25, .2) )
		barSize = HelperVec2.mult(size, (.5, .4) )
		sizeBar = (size[0]*.5,size[1]*.4)

		s.textureIdFuelBG = TextureLoader.load( os.path.join('assets', 'screenGame','fuelBG.png' ),size)
		s.textureIdFuelWave = TextureLoader.load( os.path.join('assets', 'screenGame','wave.png'), (barSize[0] , 3) )
		s.textureIdFuelDiv = TextureLoader.load( os.path.join('assets', 'screenGame','fuelDiv.png'),(barSize[0] , 1))
		s.textureIdFuelFill = TextureLoader.load( os.path.join('assets', 'screenGame','fuelFill.png'),barSize)

		for i in range(0,3):
			posNew = HelperVec2.add(pos, HelperVec2.mult( size, ((1.31)*i ,0) )  )
			list.append(IcnFuel(posNew, size,barPos, barSize,s.textureIdFuelBG ,s.textureIdFuelDiv , s.textureIdFuelFill,s.textureIdFuelWave ))
			#list.append(s.helperGetIcnFuel(posNew,size, (.5-.25,.5-.2), (.5,.4) ,s.textureIdFuelBG ,s.textureIdFuelDiv , s.textureIdFuelFill,s.textureIdFuelWave ))

	def initIcnRocket(self,screenSize):
		pos = (500,100)
		size = (200,400)
		oilPos = HelperVec2.mult(size, (.5-.25,.5-.2))
		oilSize = HelperVec2.mult(size, (.5,.4) )

		self.textureIdRocket = TextureLoader.load( os.path.join('assets', 'screenGame','icnRocket.png'),size)
		self.textureIdRocketFuel = TextureLoader.load( os.path.join('assets', 'screenGame','fuelBG.png'),oilSize)
		self.textureIdRocketFuelDiv = TextureLoader.load( os.path.join('assets', 'screenGame','fuelDiv.png'),(oilSize[0],3))
		self.textureIdRocketFuelFill = TextureLoader.load( os.path.join('assets', 'screenGame','fuelFill.png'),oilSize)
		self.textureIdRocketFuelWave = TextureLoader.load( os.path.join('assets', 'screenGame','wave.png'),(oilSize[0],oilSize[1] * .1))

		self.icnRocket =  IcnRocket( pos,size, oilPos,oilSize,\
			self.textureIdRocket ,self.textureIdRocketFuel,self.textureIdRocketFuelDiv,self.textureIdRocketFuelFill,self.textureIdRocketFuelWave)
	def initIcnText(s,screenSize):
		s.icnTextLevel = IcnTextBox(0.01*screenSize[0],0, .15*screenSize[0],.05*screenSize[1] ,"Level 0")
		s.icnTextScore = IcnTextBox(.85*screenSize[0],0, .15*screenSize[0],.05*screenSize[1], "Score 0 ")

		s.arrIcnText = [s.icnTextLevel,s.icnTextScore]
		pass

	def initButtons(s,screenSize):
		size = HelperVec2.mult(screenSize, (.1 ,.1 ))
		s.textureIdButton = TextureLoader.load( os.path.join('assets', 'screenGame','bttn.png'),size)

		s.bttnMenu =	KButton(0*screenSize[0], .90*screenSize[1], .5*screenSize[0], .1*screenSize[1],  s.textureIdButton,True)
		s.bttnDone =	KButton(.5 *screenSize[0], .9*screenSize[1], .5*screenSize[0], .1*screenSize[1], s.textureIdButton,True)
		s.arrButtons =	[s.bttnMenu,s.bttnDone]

	def initImages(s,screenSize):
		s.textureIDBG = TextureLoader.load( os.path.join('assets', 'screenGame','background.png'),screenSize)

	def helperLoadData(self,path):
		file = open(path) 
		data = json.load(file)
		arr = [data["CHOICES"],data["ANSWERS"],data["ANSWER_NUM"]  ]
		file.close()
		return arr

	#Load the level-th JSON file in the levels folder
	def initLevel(self, level = -1):
		if(level is -1 ) : level = self.questionLevel
		self.levelWon = False
		self.EVENT_SCENE_CHANGE_START()

		

		try:
			data = self.helperLoadData(os.path.join('assets/levels',str(self.questionLevel)+ '.json'))
			self.loadNewQuestion(self.questionLevel, data[0],data[1],data[2])
		except :
			print "SceneGame CRITICAL ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!SOMETHING NOT RIGHT HERE. CANNOT LOAD LEVEL ! LOADING EMERGENCY LEVEL"
			try : 
				data = self.helperLoadData( os.path.join('assets/levels','0.json'))
				self.loadNewQuestion(self.questionLevel,data[0],data[1],data[2])
			except : "SceneGame I failed. I cannot load anything. We are doomed!"

		self.EVENT_SCENE_CHANGE_END()

	def registerEvent_menu(s,e):s.EVENT_MENU.append(e)
	def registerEvent_win(s,e):s.EVENT_WIN.append(e)
	def initEvents(s):
		s.EVENT_MENU=[]
		s.EVENT_WIN=[]
	def initBackground(s,surface,resolution):
		DrawHelper.drawAspect(surface,s.textureIDBG, 0,0 )
		pass

	def loadNewQuestion(self,level,choices,answers,answerNum):
		self.questionChoices	= choices
		self.questionAnswers	= answers

		for i in range(0,3):
			self.arrIcnFuels[i].setSelect(False)
			self.arrIcnFuels[i].display(choices[i][0],choices[i][1] )
		self.icnRocket.display(0,answerNum[1])
		self.icnTextLevel.setContent("Level "+str(level) )

		pass
	
	def helperIsSameArray(self, arrA, arrB):
		if(len(arrA) is not len(arrB)): return False
		for i in range(0, len(arrA)):
			if( arrA[i] is not arrB[i]) :return False
		return True

	def doCheckAnswer(self):
		if(self.isGameOver() ) : 
			#Submitted answer is correct advnace to the next level and raise win event
			self.questionLevel += 1
			self.score += 10
			self.helperRaiseEvent(self.EVENT_WIN)
		else : print "GAME IS NOT YET OVER! DISPLAY SOME \"Lets try again GRAPHIC\" "  

	def isGameOver(self):
		answerState = []
		for icn in self.arrIcnFuels:answerState.append(icn.isSelected)
		for a  in self.questionAnswers:
			if(self.helperIsSameArray(answerState, a) ) :return True
		return False
	def doUpdateAnswer(self):
		sum = 0
		for i in range(0, len( self.arrIcnFuels )):
			if(self.arrIcnFuels[i].isSelected):
				sum += self.questionChoices[i][0] / float(self.questionChoices[i][1])
		print "updating rocket "  + str(sum)
		self.icnRocket.displayPercent(sum)

		pass


	def EVENT_CLICK(self):
		print "EVENT_CLICK"
		if(self.CLICK_ANSWER()) : 
			self.doUpdateAnswer()
		elif (self.CLICK_BUTTONS()):pass

	def EVENT_SCENE_START(self):
		print("entered play state")
		self.initLevel()

	def CLICK_ANSWER(self):
		pos = pygame.mouse.get_pos()
		for i in range(0, len( self.arrIcnFuels  )) :
			icn = self.arrIcnFuels[i]
			choice = self.questionChoices[i]
			if(icn.isUnder(pos)):
				if(icn.select()): icn.displayPercent(0)
				else :  icn.displayPercent(choice[0]/float(choice[1]))
				return True
		return False

	def CLICK_BUTTON_MENU(self): self.helperRaiseEvent(self.EVENT_MENU)
	def CLICK_BUTTON_EMPTY(self):
		for answer in self.currentAnswers:
			answer.selected = False
		self.goalContainer.fill(0.0)

	def CLICK_BUTTON_DONE(self):
		#call button animation here
		self.doCheckAnswer()#then process event 

	def CLICK_BUTTONS(self):
		mousePos = pygame.mouse.get_pos()
		bttn_event = [
			[self.bttnMenu, self.CLICK_BUTTON_MENU],
			[self.bttnDone, self.CLICK_BUTTON_DONE]]
		for bttn,event in bttn_event:
			if( not bttn.isUnder(mousePos)):continue
			event()
			return  True
		return False

	def renderScreenClean(self,screen):
		self.helperClean(screen, self.icnTextLevel)
		self.helperClean(screen, self.icnTextScore)

	def renderScreen(self,screen):
		for icn in self.arrButtons:
			icn.draw(screen);
			icn.drawEnd();

		for icn in self.arrIcnFuels:
			icn.draw(screen);
			icn.drawEnd();



		for icn in self.arrIcnText:
			icn.draw(screen);
			icn.drawEnd();

		self.icnRocket.draw(screen)
		self.icnRocket.drawEnd()

	def renderUpdate(self, timeElapsed):
		self.icnTextScore.setContent("Score " + str( self.score))


		for icn in self.arrIcnFuels:icn.drawUpdate(timeElapsed)
		for icn in self.arrIcnText:icn.drawUpdate(timeElapsed)
		self.icnRocket.drawUpdate(timeElapsed)


