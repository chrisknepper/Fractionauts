import pygame
from IcnParticleDistort import IcnParticleDistort 

class IcnParticleDistortCustomRange(IcnParticleDistort):
	def __init__(s,x,y,w,h, texture, rangeX, rangeY ):
		IcnParticleDistort.__init__(s,x,y,w,h,texture)
		s.range = (rangeX, rangeY)
		s.velo =(0,0)
	def draw(s, screen):
		s.rect = (s.pos[0],s.pos[1], s.size[0],s.size[1])
		screen.blit(s.texture, s.rect ,(s.rect[0]+s.range[0],s.rect[1]+s.range[1],s.rect[2],s.rect[3]) )
		#distort here 
		return s.rect