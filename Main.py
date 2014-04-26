#!/usr/bin/python
import threading
# Fractionauts Main Class
import pygame
import os
import json
#from gi.repository import Gtk

from Button import Button
from Question import Question
from MainMenu import MainMenu
from Game import Game
from Help import Help


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
		self.screen = pygame.display.set_mode((1200, 900))

		fontObj = pygame.font.Font('freesansbold.ttf', 32)
		self.screen = pygame.display.get_surface()
		self.height = pygame.display.Info().current_h
		self.width = pygame.display.Info().current_w
		self.hcenter = self.width / 2 
		self.vcenter = self.height / 2
		self.states = [MainMenu(self), Game(self), Help(self)] #initialize all states
		if self.gameLoaded == False:
				print "gameLoaded"
				self.loadGame()


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
			self.states[self.state].renderScreen()
			pygame.display.flip()
			self.clock.tick(40);

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
