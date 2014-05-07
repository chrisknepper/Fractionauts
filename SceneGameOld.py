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

#Arrange passed-in answers array in a grid with sensible default options
	def arrangeAnswers(self, answers, perRow , base_x,  base_y , h_spacing, v_spacing):
		#Starting our counter variables at 1 to avoid an additional if block 
		#(because we can never divide by 0 this way)
		counter = 1
		currentRow = 1
		posInCurrentRow = -1 #Initialize current row position to -1 
							 #so first answer isn't offset incorrectly
		for answer in answers:
			answer = answer.split("/")#get numerator and denominator
			if(counter > currentRow * perRow):
				currentRow = currentRow + 1
				posInCurrentRow = 0
			else:
				posInCurrentRow = posInCurrentRow + 1
			answer_x = base_x + (h_spacing * posInCurrentRow)
			answer_y = base_y + ((currentRow - 1) * v_spacing)
			temp = Container(answer_x, answer_y, int(answer[0]), int(answer[1]))
			self.currentAnswers.append(temp)
			counter = counter + 1


	def checkLevelExists(self, level):
		return os.path.exists(os.path.join('assets/levels', str(level) + '.json'))