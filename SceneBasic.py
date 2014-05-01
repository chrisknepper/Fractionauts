import pygame
import os
import pygtk #Considfer removing this import call, I don't think you need this TBH 
from Button import Button
from Background import Background
from TextItem import TextItem
from ScrollingImage import ScrollingImage
import TextureLoader

class SceneBasic(object):
	#init methods
	
	def __init__(self, main,  resolution):
		self.main = main
		self.initEvents();
		self.initImages(resolution);
		self.initButtons(resolution)
		self.initOthers(resolution)

	def initButtons(s,screenSize):
		pass
	def initImages(s,screenSize):
		pass;
	def initEvents(s):
		pass
	def initOthers(s,screenSize):
		pass

	#in main loop
	def listenForEvents(self):
		pass
	def updateStatic(self):
		pass

	#in a thread 
	def renderScreen(self,screen):
		pass
	def updateRender(self):
		pass

	def enter(self):
		print("entered main menu")



