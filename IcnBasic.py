import pygame
import TextureLoader
import HelperTexture

class IcnBasic:
	def EVENT_STATIC_NOW(self):
		for e in self.EVENHDR_STATIC : e(self)
	def registerEvent_static(self, e):
		self.EVENHDR_STATIC.append(e)
		
	def __init__(self,x,y,w,h,textureID=-1,isTextureRescaled = False):
		self.isSelected = False
		
		self.EVENHDR_STATIC = []

		self.pos = (x,y)
		self.size = (w,h)
		self.textureID = textureID
		self.rect = (0,0,10,10);
		self.mySurface = pygame.Surface((w,h),pygame.SRCALPHA) if textureID is -1 else TextureLoader.get(textureID)
		if(isTextureRescaled ) : self.mySurface =HelperTexture.scale(self.mySurface, self.size)
		
	def setSelect(s,value):
		s.isSelected = value
		
	def isUnder(self,pos):
		x, y = pos
		if (self.pos[0] < x and
			self.pos[0] + self.size[0] > x and
			self.pos[1] < y and
			self.pos[1] + self.size[1] > y
			):
			return pos
		else: return None
		
	def select(self):
		self.isSelected = not self.isSelected
		return self.isSelected
	def draw(self,screen):
		self.rect  = screen.blit(self.mySurface,self.pos)
		return self.rect
	def drawEnd(self):
		pygame.display.update(self.rect )
		pass
	def drawUpdate(self, timeElapsed=0):
		pass