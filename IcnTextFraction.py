import pygame
from IcnBasic import IcnBasic
from IcnTextBox import IcnTextBox
import HelperVec2

class IcnTextFraction(IcnBasic):
	def __init__(s, x,y,w,h):
		IcnBasic.__init__(s,x,y,w,h)
		height = h*.5
		s.posDen = h * .5
		s.icnTextNum = IcnTextBox(0,0,w,height,"0")
		s.icnTextDen = IcnTextBox(0,0+s.posDen,w,height,"1")
		

	def display(s, nume,deno , colorNum = (255,255,255), colorDen = (255,255,255)):
		s.icnTextNum.setContent(str(nume),colorNum)
		s.icnTextDen.setContent(str(deno),colorDen)
		s.icnTextNum.drawUpdate(0)
		s.icnTextDen.drawUpdate(0)
		s.mySurface.fill((1,1,1,0))
		s.icnTextNum.draw(s.mySurface)
		s.icnTextDen.draw(s.mySurface)
		pygame.draw.line(s.mySurface, (255,255,255) , (0,s.size[1]*.5) , HelperVec2.mult(s.size, (1,.5) ) ,2) 
	
	def drawUpdate(s,timeElapsed):
		pass
