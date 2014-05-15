from IcnParticleNoTexture import IcnParticleNoTexture
import random
import pygame
class IcnParticleDistort(IcnParticleNoTexture):
	def __init__(s, x,y,w,h, texture ):
		IcnParticleNoTexture.__init__(s,x,y,w,h)
		s.velo = (-10 +20* random.random(),-10+20* random.random())
		s.texture = texture
	def draw(s, screen):
		s.rect = (s.pos[0],s.pos[1], s.size[0],s.size[1])
		screen.blit(s.texture, s.rect ,(s.rect[0]+s.velo[0],s.rect[1]+s.velo[1],s.rect[2],s.rect[3])  ,pygame.BLEND_ADD)
		
		#distort here 
		return s.rect

