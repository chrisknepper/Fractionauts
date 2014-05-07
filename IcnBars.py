import pygame
import HelperVec2
from IcnBasic import IcnBasic

class IcnBars (IcnBasic):
	def __init__(self, x, y, w, h, count ):
		IcnBasic.__init__(self,x,y,w,h)
		self.count = count;
		self.mySurface = pygame.Surface((w,h))
		self.cellHeight = h/ count

		self.helperInitSurface(self.mySurface, self.cellHeight, (255,0,0), 0, 1)
		pass
	def helperInitSurface(self,surface, height, color , indexFrom,indexTo):
		for i in range(indexFrom,indexTo):
			pygame.draw.rect(surface,color, (0, height* i, 1000, height ))
		pass
	def dispaly(self, n ):
		pass
