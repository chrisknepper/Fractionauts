#!/usr/bin/python
import threading
# Fractionauts Main Class
import pygame
import os
import json
#from gi.repository import Gtk

from Button import Button
from Question import Question
from SceneMenu import SceneMenu
from SceneGame import SceneGame
from SceneHelp import SceneHelp

#my calls
import TextureLoader
import DrawHelper
from SceneBasic import SceneBasic	

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

#question = Question("addition")
	
class FractionautsMain(object):
	def __init__(self):

		self.isRunning = True
		self.isRenderFirstFrame = True

		self.gameLoaded = False
		self.savePath = os.path.join('assets', 'save.json')
		# Set up a clock for managing the frame rate.
		self.clock = pygame.time.Clock()
		self.lockRender = threading.Lock()

		self.currentLevel = 0;
		self.score = 0;

		self.x = -100
		self.y = 100

		self.vx = 10
		self.vy = 0
		self.modes = ['menu', 'play', 'help']
		self.state = 0
		self.paused = False
		self.direction = 1



		pygame.init()
		screenSize = (800,600)
		self.screen = pygame.display.set_mode(screenSize)
		DrawHelper.init(screenSize[0],screenSize[1])

		self.myFont = pygame.font.Font('freesansbold.ttf', 32)
		self.screen = pygame.display.get_surface()
		self.height = pygame.display.Info().current_h
		self.width = pygame.display.Info().current_w
		self.hcenter = self.width / 2 
		self.vcenter = self.height / 2

		self.states = [SceneMenu(screenSize), SceneGame(screenSize), SceneHelp(screenSize)] #initialize all states
		self.registerEvents(self.states[0],self.states[1],self.states[2])


	def EVENTHDR_SCENE_START_MENU(self):
		self.set_mode('menu');
		pass
	def EVENTHDR_SCENE_START_GAME(self):
		self.set_mode('play');
		pass
	def EVENTHDR_SCENE_START_HELP(self):
		self.set_mode('help');
		pass
	def EVENTHDR_QUIT(self):
		self.saveLevel()
		self.isRunning = False
		pass

	def EVENTHDR_SCENE_CHANGE_START(self):
		self.lockRender.acquire()
		pass
	def EVENTHDR_SCENE_CHANGE_END(self):
		self.lockRender.release()
		pass

	def registerEvents(self, sceneMenu,sceneGame,sceneHelp):
		SceneBasic.registerEvent_sceneChangeStart(self.EVENTHDR_SCENE_CHANGE_START)
		SceneBasic.registerEvent_sceneChangeEnd(self.EVENTHDR_SCENE_CHANGE_END)
		sceneMenu.registerEvent_play(self.EVENTHDR_SCENE_START_GAME)
		sceneMenu.registerEvent_help(self.EVENTHDR_SCENE_START_HELP)
		sceneMenu.registerEvent_quit(self.EVENTHDR_QUIT)

		sceneGame.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		sceneHelp.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		pass

	def set_paused(self, paused):
		self.paused = paused

	# The main game loop.
	def run(self):
		self.isRunning = True
		threadRender = threading.Thread(target = self.loopRender);
		threadRender.start();
		self.loopUpdate();
		self.isRunning = False;
		threadRender.join();#wait for the thread to complete, then game over
	def displayFPS(self,myFont):
		label =  myFont.render("FPS "+str(int(self.clock.get_fps()) ) , 1, (255,255,0))
		pygame.draw.rect(self.screen, (0,0,0) , (0,0, 300,200))
		rectFPS = self.screen.blit(label,(0, 0))
		pygame.display.update(rectFPS)

	def helperRenderScene(self, scene):
		if(self.isRenderFirstFrame):
			scene.renderScreenBegin(self.screen)
			self.isRenderFirstFrame = False
		scene.renderScreen(self.screen)

	def loopRender(self):
		while  self.isRunning:
			self.lockRender.acquire();
			self.helperRenderScene( self.states[self.state])
			
			self.clock.tick(100);
			self.displayFPS(self.myFont);
			self.lockRender.release();

	def loopUpdate(self):
		while True:
			eventStack = pygame.event.get();
			for event in eventStack:
				if event.type == pygame.QUIT:
					return
			self.states[self.state].listenForEvents()





	def set_mode(self, mode):
		self.isRenderFirstFrame = True;
		self.state = self.modes.index(mode)
		self.states[self.state].EVENT_SCENE_START()


# This function is called when the game is run directly from the command line:
# ./FractionautsMain.py
def main():
	game = FractionautsMain()
	game.run()

if __name__ == '__main__':
	main()
