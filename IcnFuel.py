import pygame
from IcnBasic import IcnBasic
from IcnBars import IcnBars
import HelperVec2

#for future whoever works on this maybe.
#I tried to make it run faster, I can't OTL
#maybe you are better than me.... hopefully 
class IcnFuel(IcnBasic):
	def getPercentage(self):
		return self.myBars.fillRatio

	def __init__(self,pos,size, \
			textureMe=-1,textureDiv=-1, textureBar =-1,textureIdFuelWave = -1):
		IcnBasic.__init__(self,pos[0],pos[1], size[0], size[1], textureMe, True)
		self.isRendered = False
		barPos = HelperVec2.mult(size, (.073,.0308))
		barSize = HelperVec2.mult(size, (.878,.940))
		self.myBars = IcnBars(barPos[0],barPos[1],barSize[0],barSize[1],10,True) 
		self.posBars = barPos
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
	
	def drawUpdate(self, timeElapsed):
		if(self.myBars.drawUpdate(timeElapsed,self.mySurface)):
			self.renderEnable()
			return True
		if( self.stateRender is self.STATE_RENDER_ENABLED): self.renderDisable()
		return False
