import pygame
import random
import HelperVec2
from IcnParticle import IcnParticle
class IcnParticleShootingStar(IcnParticle):
	textureBG = ""
	@staticmethod
	def SET_TEXTURE_BG(texture):
		IcnParticleShootingStar.textureBG = texture

	def __init__(s,x,y,w,h, textureId, boundry, veloInit = (-45,100)):
		IcnParticle.__init__(s,x,y,w,h,textureId)
		s.boundry = boundry
		s.veloInit = veloInit
		s.respawn()
	def respawn(s):
		ratio = 1.2+ 3.5*random.random()
		s.pos = (random.random() *1.5* s.boundry[0],-100)
		s.velo = HelperVec2.mult(s.veloInit ,(ratio,ratio)) 
		pass
	def drawUpdate(s, timeElapsed):
		IcnParticle.drawUpdate(s,timeElapsed)
		if (s.pos[0] <  - s.size[0] or s.pos[1] > s.boundry[1]) : s.respawn() 
		pass
	def draw(s, surface):
		#surface.blit(IcnParticleShootingStar.textureBG,s.rect ,(s.rect[0]-2.5,s.rect[1]+10,s.rect[2],s.rect[3]),pygame.BLEND_MAX  )
		#surface.blit(IcnParticleShootingStar.textureBG,s.pos ,(s.pos[0]-2.5,s.pos[1]+10,s.size[0],s.size[1]),pygame.BLEND_MAX  )
		
		rect = IcnParticle.draw(s,surface)
		#size =( s.rect[2] * .8 , s.rect[3] *.8)
		#pos = (s.rect[0] , s.rect[1] + size[1] *.5)

		#surface.blit(IcnParticleShootingStar.textureBG,pos ,(pos[0]-2.5,pos[1]+10,size[0],size[1]),pygame.BLEND_MAX  )
		
		#surface.blit(surface,s.rect ,(s.rect[0],s.rect[1],s.rect[2],s.rect[3]),pygame.BLEND_MIN)
		return rect

