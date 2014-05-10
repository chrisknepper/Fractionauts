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
from IcnTextFraction import IcnTextFraction
#more for drawing helper 
#consider wrapping these classes into whole?
from EasyLine import EasyLine


class SceneGame(SceneBasic):

	def __init__(self,screenSize):
		SceneBasic.__init__(self,screenSize)

	def initOthers(self, screenSize):

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
		self.initLines(screenSize)

		self.renderScreenObjects.append(self.icnRocket)
		#self.renderScreenObjects.append(self.icnRocketLabelFraction)
		self.renderScreenObjects.append(self.icnTextBottom)

		self.renderScreenObjects.extend(self.arrIcnFuels)
		#self.renderScreenObjects.extend(self.arrIcnFuelLabelFraction)
		
			#self.renderScreenObjects.extend(self.arrLines)
		#self.renderScreenObjects.extend(self.arrButtons)
		#self.renderScreenObjects.extend(self.arrIcnText)


	def helperGetIcnFuel(self, pos,size, ratioPos,ratioSize,textureBG,textureDiv, textureFill,textureWave):
		return IcnFuel(pos, size,HelperVec2.mult(size,ratioPos), HelperVec2.mult(size, ratioSize ),textureBG,textureDiv,textureFill,textureWave )

	def initIcnFuels(s,list,screenSize):
		pos = (73,205)
		size = (94,243)
		barPos =  (10,10)
		barSize = (74, 223)
		labelSize = HelperVec2.mult( barSize , (.3, .3) )

		s.textureIdFuelBG = TextureLoader.load( os.path.join('assets', 'screenGame','fuelBG.png' ))
		s.textureIdFuelWave = TextureLoader.load( os.path.join('assets', 'screenGame','wave.png'))
		s.textureIdFuelDiv = TextureLoader.load( os.path.join('assets', 'screenGame','fuelDiv.png'))
		s.textureIdFuelFill = TextureLoader.load( os.path.join('assets', 'screenGame','fuelFill.png'))

		s.arrIcnFuelLabelFraction = []
		for i in range(0,3):
			posNew = ( pos[0] + 124  * i, pos[1])
			posLabel = HelperVec2.add(posNew, (size[0] +10, -labelSize[1] ))

			list.append(IcnFuel(posNew, size,barPos, barSize,s.textureIdFuelBG ,s.textureIdFuelDiv , s.textureIdFuelFill,s.textureIdFuelWave ))
			s.arrIcnFuelLabelFraction.append(IcnTextFraction (posLabel[0],posLabel[1],labelSize[0],labelSize[1]) )
			
			#list.append(s.helperGetIcnFuel(posNew,size, (.5-.25,.5-.2), (.5,.4) ,s.textureIdFuelBG ,s.textureIdFuelDiv , s.textureIdFuelFill,s.textureIdFuelWave ))

	def initIcnRocket(self,screenSize):
		pos = (503,73)
		size = (210,407)
		oilPos = (76,135)
		oilSize = (57,147)

		self.textureIdRocket = TextureLoader.load( os.path.join('assets', 'screenGame','icnRocket.png'))
		self.textureIdRocketFuel = TextureLoader.load( os.path.join('assets', 'screenGame','fuelBG.png'),oilSize)
		self.textureIdRocketFuelDiv = TextureLoader.load( os.path.join('assets', 'screenGame','fuelDiv.png'))
		self.textureIdRocketFuelFill = TextureLoader.load( os.path.join('assets', 'screenGame','fuelFill.png')  )
		self.textureIdRocketFuelWave = TextureLoader.load( os.path.join('assets', 'screenGame','wave.png'),(oilSize[0],oilSize[1] * .1))

		self.icnRocket =  IcnRocket( pos,size, oilPos,oilSize,\
			self.textureIdRocket ,self.textureIdRocketFuel,self.textureIdRocketFuelDiv,self.textureIdRocketFuelFill,self.textureIdRocketFuelWave)
		self.icnRocketLabelFraction = IcnTextFraction(pos[0]+size[0]+30,pos[1]+50,size[0]*.2,size[1]*.2)
	def initIcnText(s,screenSize):
		s.icnTextLevel = IcnTextBox(0.01*screenSize[0],0, .15*screenSize[0],.05*screenSize[1] ,"Level 0")
		s.icnTextScore = IcnTextBox(.85*screenSize[0],0, .15*screenSize[0],.05*screenSize[1], "Score 0 ")
		s.icnTextBottom = IcnTextBox(.1*screenSize[0], .95 * screenSize[1], .9*screenSize[0], .05* screenSize[1], "HeyBottom" )
		s.icnTextRocket = IcnTextBox(650.0,125.0, 100.0,30.0, "FILL TO")

		s.arrIcnText = [s.icnTextLevel,s.icnTextScore,s.icnTextRocket]
		pass

	def initButtons(s,screenSize):
		size = HelperVec2.mult(screenSize, (.1 ,.1 ))
		sizeLaunch = (115,32)
		s.textureIdButton = TextureLoader.load( os.path.join('assets', 'screenGame','bttn.png'),size)
		s.textureIdButtonLaunch = TextureLoader.load( os.path.join('assets', 'screenGame','bttnLaunch.png'),sizeLaunch)

		s.bttnMenu =	KButton(0*screenSize[0], .95*screenSize[1], .1*screenSize[0], .05*screenSize[1],  s.textureIdButton,True)
		s.bttnDone =	KButton(552,508, sizeLaunch[0],sizeLaunch[1], s.textureIdButtonLaunch,True)
		s.arrButtons =	[s.bttnMenu,s.bttnDone]

	def initImages(s,screenSize):
		s.textureIdBG = TextureLoader.load( os.path.join('assets', 'screenGame','background.png'),screenSize)
		s.textureIdFooter = TextureLoader.load(os.path.join('assets', 'screenGame','barBottom.png'), HelperVec2.mult( screenSize, (1, .05) ) )
	def initLines(s, screenSize):
		s.arrLines = []
		for i in range(0, 3):
			objA = s.arrIcnFuels[i]
			objB =s.arrIcnFuelLabelFraction[i]
			pointA = HelperVec2.add(objA.pos, (objA.size[0] *.5,0) )
			pointB = HelperVec2.add(objB.pos,( 0, objB.size[1]*.5 ) )
			s.arrLines.append(EasyLine( pointA,pointB, (255,255,255) , 2) )
		s.arrLines.append(EasyLine( (660,220),(700,220), (255,255,255) , 3) )
		s.arrLines.append(EasyLine( (700,220), HelperVec2.add(s.icnRocketLabelFraction.pos,(0,s.icnRocketLabelFraction.size[1] *.5) ) , (255,255,255) , 2) )

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
	def initBackground(s,screen,resolution):
		DrawHelper.drawAspect(screen,s.textureIdBG, 0,0 )
		DrawHelper.drawAspect(screen,s.textureIdFooter, 0,.95 )
		s.icnTextScore.draw(screen)
		s.icnRocketLabelFraction.draw(screen)

		s.helperRenderScreen(screen ,s.arrIcnFuelLabelFraction)
		s.helperRenderScreen(screen ,s.arrButtons)
		s.helperRenderScreen(screen ,s.arrIcnText)
		s.helperRenderScreen(screen, s.arrLines )
		pass



		#self.renderScreenObjects.append(self.icnRocket)
		#self.renderScreenObjects.append(self.icnRocketLabelFraction)
			#self.renderScreenObjects.append(self.icnTextBottom)

			#self.renderScreenObjects.extend(self.arrIcnFuels)
		#self.renderScreenObjects.extend(self.arrIcnFuelLabelFraction)
		
			#self.renderScreenObjects.extend(self.arrLines)
		#self.renderScreenObjects.extend(self.arrButtons)
		#self.renderScreenObjects.extend(self.arrIcnText)

	def loadNewQuestion(self,level,choices,answers,answerNum):
		print "LOADING NEW QUESTION "
		self.questionChoices	= choices
		self.questionAnswers	= answers

		for i in range(0,3):
			self.arrIcnFuels[i].setSelect(False)
			self.arrIcnFuels[i].display(choices[i][0],choices[i][1] )
			self.arrIcnFuelLabelFraction[i].display(choices[i][0],choices[i][1] )
		self.icnRocket.display(0,answerNum[1])
		self.icnRocketLabelFraction.display(answerNum[0],answerNum[1] )
		self.icnTextLevel.setContent("Level "+str(level) )
		pass
	
	def helperIsSameArray(self, arrA, arrB):
		if(len(arrA) is not len(arrB)): return False
		for i in range(0, len(arrA)):
			if( arrA[i] is not arrB[i]) :return False
		return True
	def questionReset(self):
		for i in range(0, 3): 
			q = self.questionChoices[i]
			self.arrIcnFuels[i].displayPercent(float(q[0])/ q[1])
			self.arrIcnFuels[i].setSelect(False)
		self.icnRocket.displayPercent(0)
	def getCurrentSum(self):
		sum = 0
		for i in range(0, 3):
			if(self.arrIcnFuels[i].isSelected):
				sum += self.questionChoices[i][0] / float(self.questionChoices[i][1])
		return sum
	def doCheckAnswer(self):
		if(self.isGameOver() ) : 
			#Submitted answer is correct advnace to the next level and raise win event
			self.questionLevel += 1
			self.score += 10
			self.helperRaiseEvent(self.EVENT_WIN)
		else : 
			print "GAME IS NOT YET OVER! DISPLAY SOME \"Lets try again GRAPHIC\" "  
			self.questionReset()

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

	def EVENT_INITIALIZE(self):
		self.questionLevel = 0 
		self.score = 0
		pass

	def EVENT_CLICK(self):
		print "EVENT_CLICK"
		if(self.CLICK_ANSWER()) : 
			self.doUpdateAnswer()
		elif (self.CLICK_BUTTONS()):pass


	def EVENT_SCENE_START(self):
		self.initLevel()


	def CLICK_ANSWER(self):
		pos = pygame.mouse.get_pos()
		for i in range(0, len( self.arrIcnFuels  )) :
			icn = self.arrIcnFuels[i]
			choice = self.questionChoices[i]
			if(icn.isUnder(pos)):
				if(icn.select()): 
					if(self.getCurrentSum() <= 1):
						icn.displayPercent(0)
						return True
					icn.setSelect(False)
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


	def renderUpdate(self, timeElapsed):
		#self.score+=1
		#self.icnRocket.pos =HelperVec2.add(self.icnRocket.pos ,(.1,0) ) 
		self.icnTextScore.setContent("Score " + str( self.score))

		for icn in self.arrIcnFuels:	icn.drawUpdate(timeElapsed)
		for icn in self.arrIcnText:	icn.drawUpdate(timeElapsed)
		for icn in self.arrIcnFuelLabelFraction:	icn.drawUpdate(timeElapsed)
		self.icnRocket.drawUpdate(timeElapsed)
		self.icnRocketLabelFraction.drawUpdate(timeElapsed)


