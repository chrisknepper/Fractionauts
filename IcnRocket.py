import pygame
from IcnFuel import IcnFuel
from IcnBasic import IcnBasic
import HelperVec2
class  IcnRocket(IcnBasic):
	#textureMe=-1,textureDiv=-1, textureBar =-1,textureIdFuelWave = -1):
	def __init__(self,pos,size,fuelPos,fuelSize, textureMe = -1, 
		textureOil=-1, textureDiv = -1, textureBar = -1, textureFuelWave = -1):
		IcnBasic.__init__(self,pos[0],pos[1],size[0],size[1],textureMe)
		
		self.posFuel = fuelPos
		barPos = HelperVec2.mult(fuelSize, (.1,.1))
		barSize = HelperVec2.mult(fuelSize, (.8,.8))
		self.myFuel = IcnFuel(HelperVec2.add(pos,self.posFuel) ,fuelSize,barPos,barSize, \
			textureOil,textureDiv, textureBar,textureFuelWave)
		
		#self.IcnFuel = IcnFuel(fuelPos,fuelSize,HelperVec2.mult( fuelSize, (.1,.1) ),HelperVec2(fuelSize, (.8,.8) ), textureOil,textureDiv, textureBar,textureFuelWave)
	def fill(number):
		pass
	def displayPercent(self, percentage):
		self.myFuel.displayPercent(percentage)
		pass
	def display(self, numerator,denominator):
		self.myFuel.display(numerator,denominator)
		pass
	def draw(self, screen):
		IcnBasic.draw(self,screen)
		self.myFuel.draw(screen)
		pass
	def drawUpdate(self, timeElapsed):
		self.myFuel.pos = HelperVec2.add(self.pos, self.posFuel)
		self.myFuel.drawUpdate(timeElapsed)
		pass