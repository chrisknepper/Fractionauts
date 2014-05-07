import pygame
import HelperVec2
from IcnBasic import IcnBasic
import TextureLoader
import HelperTexture

class IcnBars (IcnBasic):
	def __init__(self, x, y, w, h, count=10 ,textureID=-1, isTextureNeedResize = False):
		IcnBasic.__init__(self,x,y,w,h)
		self.count = count;
		self.mySurface = pygame.Surface((w,h))
		self.cellHeight = h/ count
		self.textureBar = pygame.Surface((0,0)) if textureID is -1 else TextureLoader.get(textureID);
		if(isTextureNeedResize): self.textureBar = HelperTexture.scale(self.textureBar,(w,self.cellHeight) )
		pass
	def helperFillBars(self,surface, height, texture , indexFrom,indexTo):
		for i in range(indexFrom,indexTo):
			surface.blit(texture, (0,   height * self.count -height* (i+1) ) )
			#pygame.draw.rect(surface,(200,100,0), (0, height* i, 1000, height ))
		pass

	#potential loss of detail of texture due to rescale
	#work on it if issue rises
	def setCount(self, n ):
		self.count = n
		self.cellHeight = self.size[1] / n
		self.textureBar = HelperTexture.scale(self.textureBar,(self.size[0],self.cellHeight) )

	def display(self, n ):

		#in case n is greater than self.count, limit.
		n = max(min( n, self.count),0)
		print "OHHHHHH " + str(n)
		self.mySurface.fill((0, 0, 0)) 
		self.helperFillBars(self.mySurface, self.cellHeight, self.textureBar, 0, n)
		pass
