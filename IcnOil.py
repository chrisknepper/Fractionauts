import pygame
from IcnBasic import IcnBasic
from IcnBars import IcnBars
import HelperVec2
class IcnOil(IcnBasic):
	def __init__(self,pos,size,posBar,sizeBar, textureMe, textureBar):
		IcnBasic.__init__(self,pos[0],pos[1], size[0], size[1], textureMe)
		self.myBars = IcnBars(posBar[0],posBar[1],sizeBar[0],sizeBar[1],10,textureBar,True) 
		self.posBars = posBar

	def display(self, numDisplay, numTotal = -1):
		if(numTotal != -1 ) : self.posBars.setCount(numTotal)
		self.myBars.display(numDisplay)

	def draw(self, screen):
		IcnBasic.draw(self,screen)
		self.myBars.pos =HelperVec2.add( self.pos , self.posBars)
		self.myBars.draw(screen)
	def drawEnd(self):
		IcnBasic.drawEnd(self)
		#self.myBars.drawEnd()
