#!/usr/bin/python
import threading
# Fractionauts Main Class
import pygame
import os
import json
#from gi.repository import Gtk

#Logics
from SceneMenu import SceneMenu
from SceneGame import SceneGame
from SceneHelp import SceneHelp
from SceneWin import SceneWin
#for static variable initialization
from IcnTextBox import IcnTextBox
import SoundManager

#utility helpers
import TextureLoader
import DrawHelper
from SceneBasic import SceneBasic

	
class Main(object):
	STATE_MENU = 0
	STATE_GAME = 1
	STATE_WIN_SCREEN =2
	STATE_HELP = 3

	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 1, 512*2)
		pygame.init()
		pygame.mixer.init(22100)
		pygame.mouse.set_visible(False)
		
		width = pygame.display.Info().current_w
		height = pygame.display.Info().current_h
		if(float(width)/float(height) == float(4)/float(3)):
			screenSize = (width,height)
		else:
			screenSize = (800,600)
		TextureLoader.screenSize =screenSize
		self.screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)

		SoundManager.init()
		SoundManager.EVENT_MUSIC_BACKGROUND()
		DrawHelper.init(screenSize[0],screenSize[1])
		self.myFont = pygame.font.Font(os.path.join('assets', 'Minecraftia.ttf') , 24)
		IcnTextBox.setFont( self.myFont)


		self.isRunning = True
		self.isRenderFirstFrame = True

		self.myState = self.STATE_MENU
		self.lockRender = threading.Lock()
		self.savePath = os.path.join('assets', 'save.json') 
		self.clock = pygame.time.Clock()# Set up a clock for managing the frame rate.

		self.scnMenu 	= SceneMenu(screenSize)
		self.scnGame 	= SceneGame(screenSize)
		self.scnWin 	= SceneWin(screenSize)
		self.scnHelp 	= SceneHelp(screenSize)

		self.registerEvents(self.scnMenu,self.scnGame,self.scnWin,self.scnHelp)
		self.dicScenes ={self.STATE_MENU: self.scnMenu,
				self.STATE_GAME: self.scnGame ,
				self.STATE_WIN_SCREEN: self.scnWin,
				self.STATE_HELP:  self.scnHelp}

	def EVENTHDR_SCENE_START_MENU(self):
		SoundManager.BTTN_EXIT()
		self.changeState(self.STATE_MENU)

	def EVENTHDR_SCENE_START_GAME(self):
		SoundManager.BTTN_START()
		self.scnGame.EVENT_INITIALIZE()
		self.changeState(self.STATE_GAME)

	def EVENTHDR_SCENE_CONTINUE_GAME(self):
		self.changeState(self.STATE_GAME)

	def EVENTHDR_SCENE_START_HELP(self):
		self.changeState(self.STATE_HELP)
	def EVENTHDR_SCENE_START_WIN(self):
		self.changeState(self.STATE_WIN_SCREEN)

	def EVENTHDR_QUIT(self):
		self.isRunning = False
		pass

	def EVENTHDR_SCENE_CHANGE_START(self):
		self.lockRender.acquire()
		pass
	def EVENTHDR_SCENE_CHANGE_END(self):
		self.lockRender.release()
		pass

	def registerEvents(self, sceneMenu,sceneGame,sceneWin, sceneHelp):
		SceneBasic.registerEvent_sceneChangeStart(self.EVENTHDR_SCENE_CHANGE_START)
		SceneBasic.registerEvent_sceneChangeEnd(self.EVENTHDR_SCENE_CHANGE_END)
		
		sceneMenu.registerEvent_play(self.EVENTHDR_SCENE_START_GAME)
		sceneMenu.registerEvent_help(self.EVENTHDR_SCENE_START_HELP)
		sceneMenu.registerEvent_quit(self.EVENTHDR_QUIT)

		sceneGame.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		sceneGame.registerEvent_win(self.EVENTHDR_SCENE_START_WIN)

		sceneWin.registerEvent_finished(self.EVENTHDR_SCENE_CONTINUE_GAME)

		sceneHelp.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		pass

	def set_paused(self, paused):
		self.paused = paused

	# The main game loop.
	def run(self):
		self.isRunning = True
		threadRender = threading.Thread(target = self.loopRender);
		self.scnMenu.EVENT_SCENE_START()
		threadRender.start();
		self.loopUpdate();
		threadRender.join();#wait for the thread to complete, then game over

	def displayFPS(self,myFont):
		label =  myFont.render("FPS "+str(int(self.clock.get_fps()) ) , 1, (255,255,0))
		rectFPS = pygame.draw.rect(self.screen, (0,0,0) , (0,0, 230,30))
		self.screen.blit(label,(0, 0))
		pygame.display.update(rectFPS)

	def helperRenderScene(self, scene):
		if(self.isRenderFirstFrame):
			scene.renderScreenBegin(self.screen)
			self.isRenderFirstFrame = False
		scene.render(self.screen)

	def loopRender(self):
		try :
			while  self.isRunning:
				self.lockRender.acquire();
				self.helperRenderScene( self.dicScenes[self.myState])
				
				#self.displayFPS(self.myFont);
				self.lockRender.release();
				self.clock.tick(60);
				self.dicScenes[self.myState].renderUpdate(self.clock.get_time() * .001)
		except :
			print "CRITICAL ERROR : RESTARTING LOOP loopRender"
			self.loopRender()
		self.isRunning = False


	def loopUpdate(self):
		try :
			while self.isRunning:
				eventStack = pygame.event.get();
				for event in eventStack:
					if event.type == pygame.QUIT:
						self.EVENTHDR_QUIT()
						return
				self.dicScenes[self.myState].listenForEvents()
		except :
			print "CRITICAL ERROR : RESTARTING LOOP loopUpdate"
			self.loopUpdate()
		self.isRunning = False
		#self.isRunning = False

	def changeState(self, stateNew):
		self.dicScenes[stateNew].EVENT_SCENE_START()
		#stop rendering whenever "potential" rendering process related process
		self.lockRender.acquire()
		self.myState = stateNew
		self.isRenderFirstFrame = True;
		self.lockRender.release()


# This function is called when the game is run directly from the command line:
# ./Main.py
def main():
	game = Main()
	game.run()

if __name__ == '__main__':
	main()


#garbage


		#self.height = pygame.display.Info().current_h
		#self.width = pygame.display.Info().current_w
		#self.hcenter = self.width / 2 
		#self.vcenter = self.height / 2
