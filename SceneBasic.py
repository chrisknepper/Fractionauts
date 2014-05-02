import pygame
import os
import pygtk #Considfer removing this import call, I don't think you need this TBH 
from Button import Button
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



