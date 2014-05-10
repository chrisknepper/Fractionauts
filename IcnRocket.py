import pygame
import random
from IcnFuel import IcnFuel
from IcnBasic import IcnBasic
import HelperVec2
class  IcnRocket(IcnBasic):

	#textureMe=-1,textureDiv=-1, textureBar =-1,textureIdFuelWave = -1):
	def __init__(self,pos,size,fuelPos,fuelSize, textureMe = -1, textureOil=-1):
		IcnBasic.__init__(self,pos[0],pos[1],size[0],size[1],textureMe)
		self.posInit = pos
		self.posFuel = fuelPos

		self.myFuel = IcnFuel(self.posFuel ,fuelSize, textureOil)

	def fill(number):
		pass
	def displayPercent(self, percentage):
		self.myFuel.displayPercent(percentage)
		pass
	def display(self, numerator,denominator):
		self.myFuel.display(numerator,denominator)
		pass
	def updateVibrate(s, w,h):
		s.pos = HelperVec2.add(s.posInit, HelperVec2.mult ( (w,h), ( -.5 +random.random(), -.5+ random.random())) )
		
		pass
	def drawUpdate(s, timeElapsed):
		
		#s.mySurface.fill((1,1,1,1), special_flags=pygame.BLEND_ADD)
		ratio = s.myFuel.getPercentage()
		s.updateVibrate(3.0*ratio,8.0*ratio)
		#s.myFuel.pos = HelperVec2.add(s.pos, s.posFuel)
		if(s.myFuel.drawUpdate(timeElapsed)):s.myFuel.draw(s.mySurface)