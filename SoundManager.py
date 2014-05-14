import pygame
import os
import wave

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
def helperLoadSound(s):
	file = wave.open(s,'rb')
	return pygame.mixer.Sound(s)
def init():
	Sound.background 	= helperLoadSound(Sound.background )
	Sound.bttnDefault 	= helperLoadSound(Sound.bttnDefault )
	Sound.bttnStart 	= helperLoadSound(Sound.bttnStart )
	Sound.bttnExit	 	= helperLoadSound(Sound.bttnExit )
	Sound.fuelUp 		= helperLoadSound(Sound.fuelUp )
	Sound.fuelDown 	= helperLoadSound(Sound.fuelDown )
	Sound.fuelNo 		= helperLoadSound(Sound.fuelNo )
	Sound.answerCorrect 	= helperLoadSound(Sound.answerCorrect )
	Sound.answerWrong 	= helperLoadSound(Sound.answerWrong )
	Sound.vibrateLow 	= helperLoadSound(Sound.vibrateLow )

def EVENT_MUSIC_BACKGROUND(): 
	Sound.background .play(-1) 
	pass
def BTTN_DEFAULT():pass#Sound.bttnDefault .play()
def BTTN_START():pass#Sound.bttnStart .play()
def BTTN_EXIT():pass#Sound.bttnExit .play()
def FUEL_UP():pass#Sound.fuelUp .play()
def FUEL_DOWN():pass#Sound.fuelDown .play()
def FUEL_NO():pass#Sound.fuelNo .play()
def ANSWER_CORRECT():pass#Sound.answerCorrect .play()
def ANSWER_WRONG():pass#Sound.answerWrong .play()
def VIBRATE_PLAY():pass#Sound.vibrateLow .play()
def VIBRATE_STOP():pass#Sound.vibrateLow .stop()


