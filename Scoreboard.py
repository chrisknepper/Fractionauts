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
		self.highScores = [];
		self.highScoreDisplays = [];
		# populate the highscores and displays
		for i in range(0, 5):
			self.highScores.append(0);
			tScore = TextItem(400, 250 + i * 50, 400, 150, [str(i+1)+': ' + str(self.highScores[i])], showRect = False);
			self.highScoreDisplays.append(tScore);

		self.background_image = os.path.join('assets', 'startscreen', 'night_sunset_gradient.png');
		self.background = Background(self.background_image);
		self.menuBtn = Button(500, 600, 200, 75, 'Menu');
		self.playerScoreDisplay = TextItem(400, 100, 400, 150, [''], showRect = False, fontSize = 72);

	def listenForEvents(self):
		if 1 in pygame.mouse.get_pressed():
			if self.menuBtn.is_under(pygame.mouse.get_pos()):
				self.main.set_mode('menu');

	def renderScreen(self):
		self.background.draw(self.main.screen);
		self.menuBtn.draw(self.main.screen);
		self.playerScoreDisplay.draw(self.main.screen);
		for displays in self.highScoreDisplays:
			displays.draw(self.main.screen);

	def enter(self):
		print("entered Scoreboard");
		self.playerScoreDisplay.setText(['You did it! Score: ' + self.main.score]);
		# append the player score to highScores
		print self.highScores
		self.highScores.append(int(self.main.score));
		print self.highScores
		# sort highScore
		self.highScores.sort();
		print self.highScores
		# remove the minimum and display the rest in sorted order
		self.highScores.pop(0);
		print self.highScores
		for i in range(0, 5):
			self.highScoreDisplays[i].setText([str(i+1)+': ' + str(self.highScores[5 - 1 - i])])
