import pygame
from IcnBasic import IcnBasic
from IcnBars import IcnBars
import HelperVec2

class IcnOil(IcnBasic):
	def __init__(self,pos,size,posBar,sizeBar, textureMe,textureDiv, textureBar):
		IcnBasic.__init__(self,pos[0],pos[1], size[0], size[1], textureMe)
		self.myBars = IcnBars(posBar[0],posBar[1],sizeBar[0],sizeBar[1],10,textureDiv,textureBar,True) 
		self.posBars = posBar
		self.numNuno = 0
		self.numDeno = 1

	def displayFillBar(self, percentage):
		self.myBars.display(percentage)

	def display(self, numerator, denominator = -1):
		self.numNuno = numerator
		if(denominator != -1 ) : 
			self.numDeno  = denominator
			self.myBars.setCount(denominator)
		self.myBars.fillRatio = 0
		self.myBars.display(self.numNuno / float(self.numDeno) )

	def draw(self, screen):
		IcnBasic.draw(self,screen)
		self.myBars.pos =HelperVec2.add( self.pos , self.posBars)
		self.myBars.draw(screen)
	def drawEnd(self):
		IcnBasic.drawEnd(self)
		#self.myBars.drawEnd()
	def drawUpdate(self, timeElapsed):
		self.myBars.drawUpdate(timeElapsed)
