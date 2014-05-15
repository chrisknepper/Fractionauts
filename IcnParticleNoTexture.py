import pygame
from IcnBasic import IcnBasic
import HelperVec2

class IcnParticleNoTexture(IcnBasic):
	def __init__(s,x,y,w,h, mass = 1.0, velo = (0.0, 0.0)):
		s.pos = (x,y)
		s.size =(w,h)
		s.rect = (x,y,w,h)
		s.mass =	mass
		s.force =	(0.0,0.0)
		s.velo =		velo
	def draw(s, screen):
		s.rect = (x,y,w,h)
		return s.rect

	def drawUpdate(s, timeElapsed):
		s.velo =HelperVec2.add(s.velo,  (s.force[0]/s.mass ,s.force[1]/s.mass ))
		s.pos = HelperVec2.add(s.pos, HelperVec2.mult (s.velo ,(timeElapsed,timeElapsed) )) 
		s.force = (0.0, 0.0)
		pass

