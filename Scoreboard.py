# Displays player score and 
import pygame
import os
import pygtk
import time
from Button import Button
from Background import Background
from TextItem import TextItem

class Scoreboard(object):
	
	def __init__(self, main):
		self.main = main;
		self.background_image = os.path.join('assets', 'startscreen', 'night_sunset_gradient.png');
		self.background = Background(self.background_image);
		self.menuBtn = Button(500, 500, 200, 75, 'Menu');
		self.scoreDisplay = TextItem(400, 200, 400, 150, [''], showRect = False, fontSize = 72);

	def listenForEvents(self):
		if 1 in pygame.mouse.get_pressed():
			if self.menuBtn.is_under(pygame.mouse.get_pos()):
				self.main.set_mode('menu');


	def renderScreen(self):
		self.background.draw(self.main.screen);
		self.menuBtn.draw(self.main.screen);
		self.scoreDisplay.draw(self.main.screen);

	def enter(self):
		print("entered Scoreboard");
		self.scoreDisplay.setText(['You did it! Score: ' + str(self.main.score)]);