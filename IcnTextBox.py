from IcnBasic import IcnBasic 

class IcnTextBox(IcnBasic):
	@staticmethod 
	def setFont(font):
		IcnTextBox.FONT =  font

	def __init__(s,x,y,w,h, content):
		IcnBasic.__init__(s,x,y,w,h)
		s.content = str(content)
		s.mySurface =  IcnTextBox.FONT.render(s.content , 1, (255,255,0))

