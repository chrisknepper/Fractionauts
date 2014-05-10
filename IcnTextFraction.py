from IcnBasic import IcnBasic
from IcnTextBox import IcnTextBox
import HelperVec2

class IcnTextFraction(IcnBasic):
	def __init__(s, x,y,w,h):
		IcnBasic.__init__(s,x,y,w,h)
		height = h*.5
		s.posDen = h * .5
		s.icnTextNum = IcnTextBox(x,y,w,height,"0")
		s.icnTextDen = IcnTextBox(x,y+s.posDen,w,height,"1")
	def display(s, nume,deno):
		s.icnTextNum.setContent(str(nume))
		s.icnTextDen.setContent(str(deno))
	def draw(s,screen):
		s.icnTextNum.draw(screen)
		s.icnTextDen.draw(screen)
	def drawEnd(s):
		s.icnTextNum.drawEnd()
		s.icnTextDen.drawEnd()

	def drawUpdate(s,timeElapsed):
		s.icnTextNum.pos	= s.pos
		s.icnTextDen.pos	= HelperVec2.add(s.pos, (0, s.posDen) )
		s.icnTextNum.drawUpdate(timeElapsed)
		s.icnTextDen.drawUpdate(timeElapsed)
