import pygame
import os

class Sound:
	background = os.path.join('assets','Sound','background.wav')
	bttnDefault = os.path.join('assets','Sound','bttn01.wav')
	bttnStart = os.path.join('assets','Sound','bttnStart.wav')
	bttnExit = os.path.join('assets','Sound','bttnBack.wav')
	fuelUp=os.path.join('assets','Sound','fuelUp.wav')
	fuelDown = os.path.join('assets','Sound','fuelDown.wav')
	fuelNo=os.path.join('assets','Sound','fuelNo.wav')
	answerCorrect=os.path.join('assets','Sound','answerCorrect.wav')
	answerWrong=os.path.join('assets','Sound','answerWrong.wav')
	vibrateLow=os.path.join('assets','Sound','rocketVibrating.wav')
def init():
	Sound.background 	= pygame.mixer.Sound(Sound.background )
	Sound.bttnDefault 	= pygame.mixer.Sound(Sound.bttnDefault )
	Sound.bttnStart 	= pygame.mixer.Sound(Sound.bttnStart )
	Sound.bttnExit	 	= pygame.mixer.Sound(Sound.bttnExit )
	Sound.fuelUp 		= pygame.mixer.Sound(Sound.fuelUp )
	Sound.fuelDown 	= pygame.mixer.Sound(Sound.fuelDown )
	Sound.fuelNo 	= pygame.mixer.Sound(Sound.fuelNo )
	Sound.answerCorrect 	= pygame.mixer.Sound(Sound.answerCorrect )
	Sound.answerWrong 	= pygame.mixer.Sound(Sound.answerWrong )
	Sound.vibrateLow 	= pygame.mixer.Sound(Sound.vibrateLow )

def EVENT_MUSIC_BACKGROUND(): 
	Sound.background .play(-1) 
	pass
def BTTN_DEFAULT():Sound.bttnDefault .play()
def BTTN_START():Sound.bttnStart .play()
def BTTN_EXIT():Sound.bttnExit .play()
def FUEL_UP():Sound.fuelUp .play()
def FUEL_DOWN():Sound.fuelDown .play()
def FUEL_NO():Sound.fuelNo .play()
def ANSWER_CORRECT():Sound.answerCorrect .play()
def ANSWER_WRONG():Sound.answerWrong .play()
def VIBRATE_PLAY():Sound.vibrateLow .play()
def VIBRATE_STOP():Sound.vibrateLow .stop()


