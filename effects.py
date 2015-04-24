import lights

class Effects :

	def __init__(self, lights) :
		self._lights = lights

	def changeColorGamma(self, note, group) :
		if note == 0 :
			self._lights.setColor([245, 135, 10], group)
		elif note == 1 : 
			self._lights.setColor([245, 10, 159], group)
		elif note == 2 : 
			self._lights.setColor([9, 237, 237], group)
		else : 
			self._lights.setColor([123, 9, 237], group)

	def changeIntensity(self, velocity, group) : 
		brightness = int(velocity * 100 / 127.0)
		self._lights.setBrightness(brightness, group)

    #def colorFlicker(self, note, group) : pass



