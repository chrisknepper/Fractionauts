import pygame
from IcnTextBox import IcnTextBox 

class IcnTextDisplayer(IcnTextBox):
	def __init__(me,x,y,w,h, content, color ):
		IcnTextBox.__init__(me,x,y,w,h,"", color)
		me.display(content )

	def display(me, content):
		me.setContent("")
		me.delay = 0;
		me.contentTo = content
		me.textCount = 0
		me.textCountTo = len(content)
	def reset(s):
		s.textCount = 0
	def drawUpdate(me, timeElapsed):
		if(me.textCount is me.textCountTo) : 
			#if(me.stateRender is me.STATE_RENDER_ENABLED): me.renderDisable()
			return False

		me.renderEnable()
		me.textCount = min ( (me.textCount + 20.0*timeElapsed), me.textCountTo ) 
		contentNew = me.contentTo[0:int(me.textCount)]
		IcnTextBox.setContent(me,contentNew)


		pass	