import pygame
from IcnTextBox import IcnTextBox 

class IcnTextDisplayer(IcnTextBox):
	def __init__(s,x,y,w,h):
		IcnTextBox.__init__(s,x,y,w,h)
		
	def drawUpdate(s, timeElapsed):
		pass