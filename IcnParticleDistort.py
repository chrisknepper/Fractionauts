from IcnParticle import IcnParticle

class IcnParticleDistort(IcnParticle):
	def __init__(s, x,y,w,h, texture):
		s.pos = (x,y)
		s.size = (w,h)
		s.texture = texture
	def draw(s, screen):
		#distort here 
		pass
