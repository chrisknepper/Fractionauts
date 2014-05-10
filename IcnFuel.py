import pygame
from IcnBasic import IcnBasic
from IcnBars import IcnBars
import HelperVec2

class IcnFuel(IcnBasic):
	def getPercentage(self):
		return self.myBars.fillRatio

	def __init__(self,pos,size,posBar,sizeBar, \
			textureMe=-1,textureDiv=-1, textureBar =-1,textureIdFuelWave = -1):
		IcnBasic.__init__(self,pos[0],pos[1], size[0], size[1], textureMe, True)
		self.isRendered = False
		self.posBars = posBar[0]
		self.myBars = IcnBars(posBar[0],posBar[1],sizeBar[0],sizeBar[1],10,textureDiv,textureBar,textureIdFuelWave,True) 
		self.posBars = posBar
		self.numNuno = 0
		self.numDeno = 1
		self.isChanged = True
		self.displayPercentage = 0

	def displayPercent(self, percentage):
		self.displayPercentage =percentage
		self.myBars.display(percentage)

	def display(self, numerator, denominator = -1):
		self.numNuno = numerator
		if(denominator != -1 ) : 
			self.numDeno  = denominator
			self.myBars.setCount(denominator)
		self.myBars.fillRatio = 0
		self.myBars.display(self.numNuno / float(self.numDeno) )
	def draw(self, screen):	
		if(self.isChanged):
			self.isChanged = False
			return IcnBasic.draw(self,screen)
		elif(not self.isRendered) :
			self.isRendered = True
			self.EVENT_STATIC_NOW()
			return IcnBasic.draw(self,screen)
		return self.rect
		#self.myBars.drawEnd()
	def drawUpdate(self, timeElapsed):
		#isUpdated =  self.myBars.drawUpdate(timeElapsed)
		#self.myBars.pos = HelperVec2.add(self.pos,self.posBars)
		if(self.myBars.drawUpdate(timeElapsed)):
			self.isChanged= True
			self.isRendered = False
			self.myBars.draw(self.mySurface)
			return True
		return False
