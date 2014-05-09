import pygame
import os
#import pygtk #Considfer removing this import call, I don't think you need this TBH 
from Button import Button
from KButton import KButton
from Background import Background
from TextItem import TextItem
from ScrollingImage import ScrollingImage
import TextureLoader

class SceneBasic(object):
	
	@staticmethod
	def helperRaiseEvent(events): 
		for e in events: e();

	event_scene_change_start =[]
	event_scene_change_end =[]

	@staticmethod
	def registerEvent_sceneChangeStart(e): SceneBasic.event_scene_change_start.append(e);
	@staticmethod
	def registerEvent_sceneChangeEnd(e):SceneBasic.event_scene_change_end.append(e);

	@staticmethod
	def EVENT_SCENE_CHANGE_START():
		SceneBasic.helperRaiseEvent(SceneBasic.event_scene_change_start)
	@staticmethod
	def EVENT_SCENE_CHANGE_END():
		SceneBasic.helperRaiseEvent(SceneBasic.event_scene_change_end)

	
	#init methods
	def __init__(self,  resolution):
		self.initBase()
		self.initEvents();
		self.initImages(resolution);
		self.initButtons(resolution)
		self.initOthers(resolution)

		self.myBackground = pygame.Surface( resolution)
		self.initBackground(self.myBackground,resolution)

	def initButtons(s,screenSize):
		pass
	def initImages(s,screenSize):
		pass;
	def initEvents(s):
		pass
	def initOthers(s,screenSize):
		pass
	def initBase(s):
		s.isMosueReleased = False

	def initBackground(s,surface,resolution):
		pass


	def updateStatic(self):
		pass

	#in a thread 
	def renderScreenBegin(self,screen):
		screen.fill((255, 255, 255)) 
		screen.blit(self.myBackground,(0,0))
		pygame.display.update()
		pass
	def render(self,screen):
		self.renderScreenClean(screen)
		self.renderScreen(screen)

	def renderScreen(self,screen):
		pass

	def renderScreenClean(self,screen):
		pass
	def updateRender(self):
		pass

	#BasicEvents
	def listenForEvents(s):
		mousePressed = pygame.mouse.get_pressed()
		if(s.isMosueReleased and mousePressed[0] is 1) :
			s.isMosueReleased = False
			s.EVENT_CLICK()
		elif(not s.isMosueReleased and mousePressed[0] is 0):
			s.isMosueReleased = True

	def EVENT_CLICK(self):
		pass

	def EVENT_SCENE_START(self):
		print("SCENE_BASIC_ENTER")



