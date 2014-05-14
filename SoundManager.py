import pygame
import os

class Sound:
	background = os.path.join('assets','Sound','background04.wav')
	bttnDefault = os.path.join('assets','Sound','bttn01.wav')
	fuelUp=os.path.join('assets','Sound','fuelUp.wav')
	fuelDown = os.path.join('assets','Sound','fuelDown.wav')
	answerCorrect=os.path.join('assets','Sound','answerCorrect.wav')
	answerWrong=os.path.join('assets','Sound','answerWrong.wav')
	vibrateLow=os.path.join('assets','Sound','lowDrum.wav')
def init():
	Sound.background 	= pygame.mixer.Sound(Sound.background )
	Sound.bttnDefault 	= pygame.mixer.Sound(Sound.bttnDefault )
	Sound.fuelUp 		= pygame.mixer.Sound(Sound.fuelUp )
	Sound.fuelDown 	= pygame.mixer.Sound(Sound.fuelDown )
	Sound.answerCorrect 	= pygame.mixer.Sound(Sound.answerCorrect )
	Sound.answerWrong 	= pygame.mixer.Sound(Sound.answerWrong )
	Sound.vibrateLow 	= pygame.mixer.Sound(Sound.vibrateLow )

def EVENT_MUSIC_BACKGROUND(): 
	Sound.background .play(-1) 
	pass
def BTTN_DEFAULT():Sound.bttnDefault .play()
def FUEL_UP():Sound.fuelUp .play()
def FUEL_DOWN():Sound.fuelDown .play()
def ANSWER_CORRECT():Sound.answerCorrect .play()
def ANSWER_WRONG():Sound.answerWrong .play()
def VIBRATE_LOW():Sound.vibrateLow .play()


