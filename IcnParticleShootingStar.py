import pygame
import random
import HelperVec2
from IcnParticle import IcnParticle
class IcnParticleShootingStar(IcnParticle):
	def __init__(s,x,y,w,h, textureId, boundry):
		IcnParticle.__init__(s,x,y,w,h,textureId)
		s.boundry = boundry
		s.respawn()
	def respawn(s):
		ratio = 1+ random.random()
		s.pos = (random.random() *1.5* s.boundry[0],-50)
		s.velo = HelperVec2.mult((-50,100) ,(ratio,ratio)) 
		pass
	def drawUpdate(s, timeElapsed):
		IcnParticle.drawUpdate(s,timeElapsed)
		if (s.pos[0] <  - s.size[0] or s.pos[1] > s.boundry[1]) : s.respawn() 
