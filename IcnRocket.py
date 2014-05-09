import pygame
from IcnOil import IcnOil
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
		self.icnOil = IcnOil(HelperVec2.add(pos,self.posFuel) ,fuelSize,barPos,barSize, \
			textureOil,textureDiv, textureBar,textureFuelWave)
		
		#self.icnOil = IcnOil(fuelPos,fuelSize,HelperVec2.mult( fuelSize, (.1,.1) ),HelperVec2(fuelSize, (.8,.8) ), textureOil,textureDiv, textureBar,textureFuelWave)
	def fill(number):
		pass
	def display(self, numerator,denominator):
		self.icnOil.display(numerator,denominator)
		pass
	def draw(self, screen):
		IcnBasic.draw(self,screen)
		self.icnOil.draw(screen)
		pass
	def drawUpdate(self, timeElapsed):
		self.icnOil.pos = HelperVec2.add(self.pos, self.posFuel)
		self.icnOil.drawUpdate(timeElapsed)
		pass