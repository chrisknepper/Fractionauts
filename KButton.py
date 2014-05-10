import pygame
import TextureLoader
import HelperTexture
from IcnBasic import IcnBasic

class KButton(IcnBasic):
	def __init__(self, x, y,w,h, textureID = -1, textureSize = ()):
		IcnBasic.__init__(self,x,y,w,h,textureID,textureSize)
		
	

	def isUnder(self,pos):
		x, y = pos
		if (self.pos[0] < x and
			self.pos[0] + self.size[0] > x and
			self.pos[1] < y and
			self.pos[1] + self.size[1] > y
			):
			return pos
		else: return None