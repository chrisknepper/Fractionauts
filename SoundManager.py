import pygame
import os
import wave

class Sound:
	background = os.path.join('assets','Sound','background01.wav')
	bttnDefault = os.path.join('assets','Sound','bttn01.wav')
	bttnStart = os.path.join('assets','Sound','bttnStart.wav')
	bttnExit = os.path.join('assets','Sound','bttnBack.wav')
	fuelUp=os.path.join('assets','Sound','fuelUp.wav')
	fuelDown = os.path.join('assets','Sound','fuelDown.wav')
	fuelNo=os.path.join('assets','Sound','fuelNo.wav')
	answerCorrect=os.path.join('assets','Sound','answerCorrect.wav')
	answerWrong=os.path.join('assets','Sound','answerWrong.wav')
	vibrateLow=os.path.join('assets','Sound','vibration.wav')
def helperLoadSound(s):
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


