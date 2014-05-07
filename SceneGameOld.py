DrawHelper.drawAspect(screen,self.textureIdBG, 0,0)
		#
		#self.background_rocket.draw(self.main.screen) idiotic rocket rising
		self.goalContainer.draw(screen)
		for button in self.buttons:
			button.draw(screen)
		for answer in self.currentAnswers:
			answer.draw(screen)

		for item in self.gameScreenUI:
			item.draw(screen)
			if(self.winScreen.drawing == True):
				self.winScreen.draw(screen)
			if(self.loseScreen.drawing == True):
				self.loseScreen.draw(screen)

		if not self.level_loaded:
			screen.fill((0, 0, 0)) #wtf idiot stop this stupid shit
		pygame.display.update()