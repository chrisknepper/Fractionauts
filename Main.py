#!/usr/bin/python
import threading
# Fractionauts Main Class
import pygame
import os
import json
#from gi.repository import Gtk

from Button import Button
from Question import Question
from SceneGameMenu import SceneGameMenu
from SceneGame import SceneGame
from SceneHelp import SceneHelp

#my calls
import TextureLoader
import DrawHelper
from SceneBasic import SceneBasic	

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

question = Question("addition")
	
class FractionautsMain(object):
	def __init__(self):
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
		self.screen = pygame.display.set_mode((1200,900))
		DrawHelper.init(1200,900)

		self.myFont = pygame.font.Font('freesansbold.ttf', 32)
		self.screen = pygame.display.get_surface()
		self.height = pygame.display.Info().current_h
		self.width = pygame.display.Info().current_w
		self.hcenter = self.width / 2 
		self.vcenter = self.height / 2

		screenSize = (pygame.display.Info().current_w,pygame.display.Info().current_h) 
		screenSize = (800,600)
		self.states = [SceneGameMenu(self,screenSize), SceneGame(self,screenSize), SceneHelp(self,screenSize)] #initialize all states
		self.registerEvents(self.states[0],self.states[1],self.states[2])

		if self.gameLoaded == False:
				print "gameLoaded"
				self.loadGame()

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
		pygame.quit()
		exit()
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

	def loopRender(self):
		while  self.isRunning:
			self.lockRender.acquire();
			self.screen.fill((255, 255, 255))  # 255 for white
			self.states[self.state].renderScreen(self.screen)
			self.clock.tick(40);
			
			label =  self.myFont.render("FPS "+str(int(self.clock.get_fps()) ) , 1, (255,255,0))
			self.screen.blit(label, (0, 0))
			pygame.display.flip()
			self.lockRender.release();

	def loopUpdate(self):
		while True:
			eventStack = pygame.event.get();
			for event in eventStack:
				if event.type == pygame.QUIT:
					return
			self.states[self.state].listenForEvents()


	#Load save file, set meta variables
	def loadGame(self):
		print 'loading game'
		path = self.savePath
		try:
			with open(path) as saved_game:
				play = self.modes.index('play')
				save_data = json.load(saved_game)
				self.score = save_data["score"]
				self.states[play].scoreDisplay.setText(['Score: ' + str(self.score)])
				self.currentLevel = int(save_data["current_level"])
				self.states[play].levelDisplay.setText(['Current Level: ' + str(self.currentLevel)])
				saved_game.close()
		except IOError:
			new_game = open(path, 'w')
			new_game.close()
		self.gameLoaded = True

	def saveLevel(self):
		print "saving level"
		path = self.savePath
		try:
			with open(path, 'r+') as saved_game:
				save_data = json.load(saved_game)
				save_data['current_level'] = str(self.currentLevel)
				save_data['score'] = str(self.score)
				json_string = json.dumps(save_data, indent=4)
				print json_string
				saved_game.seek(0)
				saved_game.write(json_string)
				saved_game.truncate()
				saved_game.close()
				print "level saved"
		except IOError as e:
			print e
			print 'Saving error'
			return



	def set_mode(self, mode):
		self.state = self.modes.index(mode)
		self.states[self.state].enter()


# This function is called when the game is run directly from the command line:
# ./FractionautsMain.py
def main():
	game = FractionautsMain()
	game.run()

if __name__ == '__main__':
	main()
